import Client as c

#make request to single product
def requests(what):
    con = c.connect()
    if(con):
        resp = c.makerequest(con,what)
        return resp
def requestProduct(name):
    keys  = ['product']
    
    values = [name]
    #print(len(key))
    #print(keys, values)
    product = c.makejson(keys,values,"product")
    #print(product)
    req = requests(product)
    return req


#make request by condition like electronics and laptop / 
def requestByCondition(condition):
    key = list(condition.keys())
    values = list(condition.values())
    product = c.makejson(key,values,"product")
    #print(product)
    req = requests(product)
    #print(req)
    return req
    
    

#make call to requestProduct
#which returns response from the server in the json format
#parse it and send it to the UI

def getProduct():
    #response = requestProduct("laptop")
    condition = {"product":"laptop","brand":"apple"}
    response  = requestByCondition(condition)
    print response
    
getProduct()
