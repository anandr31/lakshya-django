from common.utils import slugify
# from paymentgateway.payu import PayUGateway
# from paymentgateway.bluepay import BluePayGateway
# from paymentgateway.paypal import PayPalGateway
# from paymentgateway.authorizenet import AuthorizeNetGateway
from paymentgateway.ccavenue import CCAvenueGateway
# from paymentgateway.hdfc import HDFCGateway

#All other constants and maps are built based on this. Make sure all new gateways are added to this list.
#That should be sufficient to make it reflect everywhere
ALL_PGS = [CCAvenueGateway]

# Payment gateways
PG_CHOICES = []
PG_KEY_CLASS_MAP = {}
for pg in ALL_PGS:
    PG_CHOICES.append((slugify(pg.name), pg.name))
    PG_KEY_CLASS_MAP[slugify(pg.name)] = pg
