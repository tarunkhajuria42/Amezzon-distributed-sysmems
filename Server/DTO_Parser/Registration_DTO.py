import json

class Registration_DTO(object):
  def __init__(self,action=None,login=None,username=None,password=None,first_name=None,last_name=None,mail=None,id_code=None):
    self.action=action
    self.login=login
    self.username=username
    self.password=password
    self.firstname=first_name
    self.lastname=last_name
    self.mail=mail
    self.idcode=id_code
    self.response={}

  def set_response(self,token=None,message=None,message_connection=None):
    self.token=token
    response={}
    data={}
    error_messages={}
    error_messages['message']=message
    error_messages['message_connection']=message_connection
    data['error_messages']=error_messages
    data['token']=token
    response['data']=data
    self.response=response
    return

  def get_response(self):
    return json.dumps(self.response)


