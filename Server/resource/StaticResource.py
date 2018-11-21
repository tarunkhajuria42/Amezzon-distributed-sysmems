import os

# Docker and Server Config
SERVER_CONFIG = 'local' if os.getenv("CONF") is None else os.getenv("CONF")

# CLIENT <---> SERVER
ACTION_LOGIN = 'login'
ACTION_REGISTRATION = 'registration'
ACTION_USER_INFORMATION = 'user_information'


# SERVER <---> DATABASE
ACTION_INIT_TRANSACTION = 'init_transaction'
ACTION_DB_STATEMENT = 'database statement'

# JSON PARSER
ACTION = 'action'
DATA = 'data'
LOGIN = 'login'
TOKEN = 'token'

# USER
USERNAME = 'username'
PASSWORD = 'password'
FIRST_NAME = 'first_name'
LAST_NAME = 'last_name'
MAIL = 'mail'
ID_CODE = 'id_code'

#transaction
ACTION = 'action'
PRODUCT_ID = 'product_id'
PRODUCT_PRICE = 'product_price'
PRODUCT_QUANTITY= 'product_quantity'

#products
PRODUCT_ID = "product_id"
PRODUCT_NAME = "product_name"
PRODUCT_TYPE = "product_type"
PRODUCT_DESCRIPTION = "product_description"
PRODUCT_QUANTITY = "product_quantity"
BUY_PRICE = "buy_price"
SELL_PRICE = "sell_price"

