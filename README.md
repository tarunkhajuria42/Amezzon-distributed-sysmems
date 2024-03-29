# Distributed Systems Project #

## Team members ##
* Aleksei Kop�lov
* Cedric De Donder 
* Tarun Khajuria
* Tek Raj Chhetri

## Team tools##
* [Drive](https://drive.google.com/drive/folders/1E4KhN9Q_ASr_p6-0iwQXxvGoVNMOeEoO)
* [Project Documentation](https://docs.google.com/document/d/1_FYtaMBkz3X2jvTtq3LkN7ntc4-EUExfeoFuS4Wp3JI/edit#heading=h.oije7prghzkl)

## Python Libraries ##

### Will Use ###
+ [Socket](https://docs.python.org/2/library/socket.html) ([Quick Guide](https://www.tutorialspoint.com/python/python_networking.htm), [More on Socket](https://realpython.com/python-sockets/)) 
+ More:https://www.binarytides.com/python-socket-programming-tutorial/
### Under Consideration ###
* **Encryption, Keys and Certificates**
	* [OpenSSl](https://pyopenssl.org/en/stable/api.html) 
		+ [Self Signed Key Generation OpenSSL Commands](https://devcenter.heroku.com/articles/ssl-certificate-self)
			+ openssl genrsa -des3 -out server.orig.key 2048
			+ openssl rsa -in server.orig.key -out server.key
			+ openssl req -new -key server.key -out server.csr
			+ openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt	
			
	* [Paramiko](http://www.paramiko.org/)
* **Data Structures and Analysis**
	* [Pandas](http://pandas.pydata.org/)

## Some of the python resources for reading ##

* [Distributed Computing with Python](https://drive.google.com/open?id=115Hs4O6-BiMrb40p58haebFY4W0GpdcH)
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)