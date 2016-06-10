

# Currencies
C_USD = 1
C_INR = 2
C_EUR = 3
C_AED = 4
C_GBP = 5

#3 character ISO format currency codes
CURRENCY_ISO_CODES = {C_USD: 'USD', C_INR: 'INR', C_EUR: 'EUR', C_AED: 'AED', C_GBP: 'GBP'}

CURRENCIES = ((C_USD, "USD"),
              (C_INR, "INR"),
              (C_EUR, "EUR"),
              (C_AED, "AED"),
              (C_GBP, "GBP"))

BASE_CURRENCY = C_USD  # Used for conversions

CURRENCY_SYMBOLS = {C_USD: '$', 'USD': '$',
                    C_INR: '&#x20B9;', 'INR': '&#x20B9;',
                    C_EUR: '&#x20AC;', 'EUR': '&#x20AC;',
                    C_AED: 'AED ', 'AED': 'AED ',
                    C_GBP: '&#163;', 'GBP': '&#163;'}
