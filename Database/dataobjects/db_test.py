from dataobjects import *

session = Session()

ENGINE.execute("DELETE FROM product_type WHERE TRUE")

product_type = ProductType("testType")

session.add(product_type)
session.commit()

q = session.query(ProductType).all()

print(q)
