from service.DatabaseService import DatabaseService
db=DatabaseService()
token=db.init_transaction()
statement="INSERT INTO person (person_username,person_passwordhash,person_firstname,person_lastname,person_mail)"\
+" VALUES('tarun','dsdas','asdas','dasdasd','tarun@gmail.com')"
result=db.make_transaction_commit(data=statement,token=token)
