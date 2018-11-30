'''
Created on 2010/12/28

@author: panda.huang
'''
import automan.tool.error as error
from automan.tool.verify import Verify
from pathlib import Path

class Tool(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def file_verify(self):
        my_file = Path("test.txt")
        if my_file.is_file() == True:
            return
        else:
            raise error.notfind()
    
    def dir_list(self):
        return 100
    
    def test_get(self):
        #raise error.notfind()
        return "121132321321"

    def testerror_get(self):
        raise error.notfind()
        #return "121132321321"
    
    def dir_set(self,value_dict):
        pass
    
    def dir_verify(self,value_dict):
        local_dict = dict(value_dict)
        #get value from system
        try:
            system_value = local_dict['key']
            local_dict['system_value'] = system_value
            Verify().verify(local_dict)
        except error.equalerror:
            raise error.equalerror()
        except error.notequalerror:
            raise error.notequalerror()
        except:
            raise error.nonamevalue()
        
    def getsystem(self,test):
        return '100'