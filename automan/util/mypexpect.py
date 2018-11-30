# _*_ coding:utf-8 _*_
'''
Created on 2015/04/23
@author: Jack.Lin
Description: Open remote desktop console.

Requirement: pip install -U pyautoit
'''
import pexpect
import requests
#import automan.tool.error as error
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("./ini/Pexpect.conf")

class Mypexpect(object):
    
    def __init__(self):
        logfile = config.get("gs", "logfile")
        self.fout = file( logfile ,'w') 
        cmd = config.get("gs", "cmd")
        self.child = pexpect.spawn(cmd)
        self.child.logfile = self.fout
    
    def pexpect_init(self):
        pass

    def cmd_send(self,para):
        self.child.sendline(para["text"])
    
    def text_expect(self,para):
        self.child.expect(para["text"])
        
    def key_get(self):
        key =""
        logfile = config.get("gs", "logfile")
        f = open(logfile,'r') 
        for line in f.readlines():
            if line[0] == "$":
                key = line[2:] 
        f.close()
        return key
    
    def password_get(self,para):
        keyword = ""
        payload = {'original_string': para["key"]}
        r = requests.post("http://swd.infortrend/linux_login_util.py", data=payload)
        print r
        for line in r.text.splitlines():
            if "Result" in line :
                password =   line[34:42]
        return password

    def __del__(self):
        self.fout.close()
        self.child.close(force=True)