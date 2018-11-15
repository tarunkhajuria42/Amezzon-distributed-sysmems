import Client as c
def userHandler():
    con = c.connect()
    if(con):
        user = c.makejson(['username','operation'],['tekraj','read'])
        #print user
        resp = c.makerequest(con,user)        
        print resp
        
userHandler()
