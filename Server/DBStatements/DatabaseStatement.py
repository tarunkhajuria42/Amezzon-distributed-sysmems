class DatabaseStatement(object):

	def __init__(self):
		return

	def get_password(self,username=None):
		statement='SELECT person_passwordhash from person where person_username= "{0}"'.format(username)
		return statement

	def get_user(self,username=None):
		statement='SELECT COUNT(*) from person where person_username="{0}"'.format(username)
		return statement

	def set_user(self):
		return

	def get_user_details(self,username=None):
		statement='SELECT person_id,person_firstName,person_lastName,person_mail \
		from person where person_username="{0}"'.format(username)
		return statement

	def transaction(self,username):
		return

	def transaction_record(self):
		return

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

	def set_user(self):
		return

	def register(self,username=None,password=None,firstname=None,lastname=None,mail=None):
		statement='INSERT INTO person(person_username,person_passwordhash,person_firstName,person_lastName,person_mail) \
		VALUES("{0}","{1}","{2}","{3}","{4}")'.format(username,password,firstname,lastname,mail)
		return statement 
		
	def commit(self):
		statement="commit"