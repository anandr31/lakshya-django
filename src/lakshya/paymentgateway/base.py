from django.http.response import Http404


class BaseGateway:
    """Base class for different payment gateway classes"""
    def update_from_account(self, account):
        self.__init__(account.get_metadata_object())

    def get_txn_details_from_server(self, *args, **kwargs):
        return None

    def process_server_post(self, *args, **kwargs):
        raise Http404

    def verify_response(self, data, txn):
        return True
