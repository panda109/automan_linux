'''
Created on Oct 18, 2018

@author: panda109
'''
import datetime
from fbchat import Client
from fbchat.models import *

if __name__ == '__main__':
    client = Client('yr6703@gmail.com', 'Panda109!!')
    #print('Own id: {}'.format(client.uid))
    now = datetime.datetime.now()
    text="jdsdsjkdsdjsldsldskldslds"
    text = text + " at " + now.strftime("%Y-%m-%d %H:%M:%S")
    client.send(Message(text), thread_id=client.uid, thread_type=ThreadType.USER)
    client.logout()
