class DatabaseStatement(object):

	def __init__(self):
		return

	def get_password(self,username=None):
		statement='SELECT person_passwordhash from person where person_username= "{0}"'.format(username)
		return statement

	def get_user(self,username=None):
		statement='SELECT COUNT(*) from person where person_username="{0}"'.format(username)
		return statement

	def get_user_details(self,username=None):
		statement='SELECT person_id,person_firstName,person_lastName,person_mail \
		from person where person_username="{0}"'.format(username)
		return statement

	def set_transaction(self,user_id=None,price=None,transaction_type=None,product_id=None,quantity=None,timestamp=None):
		print(transaction_type)
		print("Done")
		statement='INSERT into transaction(transaction_type,transaction_client,transaction_product,transaction_price,\
		transaction_quantity,transaction_timestamp) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}")'.format(transaction_type,
			user_id,
			product_id,
			price,
			quantity,
			timestamp)
		return statement

	def set_product_history(self,product_id=None,buy_price=None,sell_price=None,quantity=None,timestamp=None):
		statement='INSERT into product_history(product_history_product_id,product_history_buy,product_history_sell,\
		product_history_quantity,product_history_timestamp) VALUES("{0}","{1}","{2}","{3}","{4}")'.format(int(product_id),
			float(buy_price),
			float(sell_price),
			int(quantity),
			timestamp)
		return statement

	def get_user_id(self,username=None):
		statement='SELECT person_id from person where person_username="{0}"'.format(username)
		return statement

	def get_prices_quantity(self,product_id=None):
		statement='SELECT product.product_base_sell, product.product_base_buy,product_price.product_history_quantity,\
		product_price.product_history_sell, product_price.product_history_buy from product INNER JOIN product_price ON \
		product.product_id=product_price.product_history_product_id where product.product_id="{0}"'.format(product_id)
		return statement


	def get_one_product(self,product_id=None):
		statement='SELECT product.product_id,product.product_name,product.product_type,product.product_description,product_price.product_history_quantity,\
		product_price.product_history_sell, product_price.product_history_buy from product INNER JOIN product_price ON \
		product.product_id=product_price.product_history_product_id where product.product_id="{0}"'.format(product_id)
		return statement
		
	def get_products(self):
		statement='SELECT product.product_id,product.product_name,product.product_type,product.product_description,product_price.product_history_quantity,\
		 product_price.product_history_sell, product_price.product_history_buy from product INNER JOIN product_price ON \
		product.product_id=product_price.product_history_product_id'
		return statement

	def register(self,username=None,password=None,firstname=None,lastname=None,mail=None):
		statement='INSERT INTO person(person_username,person_passwordhash,person_firstName,person_lastName,person_mail) \
		VALUES("{0}","{1}","{2}","{3}","{4}")'.format(username,
			password,
			firstname,
			lastname,
			mail)
		return statement 
