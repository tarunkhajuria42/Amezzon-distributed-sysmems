from dataobjects import *

session = Session()

engine.execute("DELETE FROM product_type WHERE TRUE")

product_type = ProductType("testType")

session.add(product_type)
session.commit()

q = session.query(Person).all()

print(q)
