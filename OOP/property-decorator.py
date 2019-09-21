############
# this part take us to the property decorator, setter, getter and deleter of class
# now, let's start
import json


class Phone:
    def __init__(self,name, osname,price):
        self.name=name
        self.osname=osname
        self.price=price
    
    def get_info(self):
        return json.dumps({
            'Name': self.name,
            'OS': self.osname,
            'Price': self.price
        })
    #now we start explore the property decorator -> this is getter
    @property
    def get_phone_name(self):
        return 'The phone has name: {}'.format(self.name)
    #now is setter
    @get_phone_name.setter
    def set_phone_name(self,name):
        self.name=name
    #and deleter
    @get_phone_name.deleter
    def delete_phone(self):
        self.name=None
        self.osname=None
        self.price=None
        print("Deleted phone's information!")

if __name__=='__main__':
    phone1=Phone('iPhone','iOS',1000)
    phone2=Phone('Sony','Android',500)
    phone1.name='Samsung' # set the name attribute of phone1 to Samsung directly
    phone2.name='HTC' # call setter to set phone2'name to HTC
    ## here is deleter
    del phone1.delete_phone # call deleter
    print("Phone1: ", phone1.get_info()) #print the info of phone1 to check
    

    # print(phone1.get_info())
    # print(phone2.get_info())        
    # print(phone1.get_phone_name) #Here, although get_phone_name is a method, we call it as an attribute
    print(phone2.get_phone_name)
    print("Phone2: ",phone2.get_info())