import json
import urlparse
import md5
from Crypto.Cipher import AES
from urllib import urlencode

from django.conf import settings
from django.core.urlresolvers import reverse

from lakshya.util import get_currency_iso_code, slugify
from paymentgateway.base import BaseGateway


class CCAvenueGateway(BaseGateway):
    name = 'CCAvenue'
    merchant_id = ''
    working_key = ''
    access_code = ''
    pg_form_template = 'paymentgateway/ccavenue_form.html'
    payment_url = settings.CCAVENUE_PAYMENT_URL

    def __init__(self):
        self.merchant_id = settings.CCAVENUE_MERCHANT_ID
        self.working_key = settings.CCAVENUE_WORKING_KEY
        self.access_code = settings.CCAVENUE_ACCESS_CODE

    def set_form_context(self, context, request, txn):
        context['encoded_request_data'] = self.get_encoded_request_data(request, txn)
        context['access_code'] = self.access_code
        context['pgform_request_url'] = self.payment_url
        context['pg_form_template'] = self.pg_form_template
        return

    def get_encoded_request_data(self, request, txn):
        redirect_url = 'http://' + request.get_host() + '/pg/response/' + slugify(self.name)
        params = [('merchant_id', self.merchant_id),
                ('order_id', txn.txnid),
                ('currency', get_currency_iso_code(txn.currency)),
                ('amount', txn.amount),
                ('redirect_url', redirect_url),
                ('cancel_url', redirect_url),
                ('language', 'en'),
                ('billing_name', txn.name),
                ('billing_tel', txn.phone),
                ('billing_email', txn.email),
                ('delivery_name', txn.name),
                ('delivery_tel', txn.phone)]
        request_data = urlencode(params)
        encoded_data = CCAvenueAESCipher().encrypt(request_data, self.working_key)
        return encoded_data

    def get_txn_id_from_response_data(self, data):
        return data.get('orderNo', '')

    def update_txn(self, data, txn):
        response_string = self.get_decoded_response_data(data, txn)
        response_data = dict(urlparse.parse_qsl(response_string))
        try:
            original_response_data = json.loads(txn.response_data)
            original_response_data.update(response_data)
            txn.response_data = json.dumps(original_response_data)
        except ValueError:
            pass
        txn.pg_txnid = response_data.get('tracking_id', '')
        txn.error = '. '.join(filter(None, [response_data.get('failure_message', ''),
                                            response_data.get('status_message', '')]))
        txn.mode = response_data.get('payment_mode', '')
        txn.status = self._get_status(response_data)
        txn.save()

    def get_decoded_response_data(self, data, txn):
        encoded_response = data.get('encResp', '')
        if not encoded_response:
            return ''
        decoded_response = CCAvenueAESCipher().decrypt(encoded_response, self.working_key)
        return decoded_response

    def _get_status(self, data):
        from accounts.models import PGTransaction
        status_map = {'success': PGTransaction.TS_SUCCESS,
                      'failure': PGTransaction.TS_FAILED,
                      'invalid': PGTransaction.TS_PENDING,
                      'aborted': PGTransaction.TS_PENDING,
                      }
        return status_map.get(data.get('order_status', '').lower(), None)


class CCAvenueAESCipher:
    """This is taken from their integration kit code for python. We are using it as is."""
    iv = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'

    def pad(self, data):
        length = 16 - (len(data) % 16)
        data += chr(length) * length
        return data

    def encrypt(self, plainText, workingKey):
        plainText = self.pad(plainText)
        encDigest = md5.new()
        encDigest.update(workingKey)
        enc_cipher = AES.new(encDigest.digest(), AES.MODE_CBC, self.iv)
        encryptedText = enc_cipher.encrypt(plainText).encode('hex')
        return encryptedText

    def decrypt(self, cipherText, workingKey):
        decDigest = md5.new()
        decDigest.update(workingKey)
        encryptedText = cipherText.decode('hex')
        dec_cipher = AES.new(decDigest.digest(), AES.MODE_CBC, self.iv)
        decryptedText = dec_cipher.decrypt(encryptedText)
        return decryptedText
