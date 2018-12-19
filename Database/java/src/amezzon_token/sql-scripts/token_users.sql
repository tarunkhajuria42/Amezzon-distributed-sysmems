CREATE
USER
'tokenuser'
@
'localhost'
IDENTIFIED
WITH
mysql_native_password
BY
'userpassword';
GRANT UPDATE, INSERT, SELECT, DELETE ON tokens.* TO 'tokenuser'@'localhost';
CREATE
USER
'tokenuser'
@
'%'
IDENTIFIED
WITH
mysql_native_password
BY
'userpassword';
GRANT UPDATE, INSERT, SELECT, DELETE ON tokens.* TO 'tokenuser'@'%';
