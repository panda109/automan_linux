'''
Created on Oct 13, 2018

@author: panda109
'''

import ConfigParser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
config = ConfigParser.ConfigParser()
config.read("./ini/Eonone.conf")


if __name__ == '__main__':
    print config.get("login", "id_signin_username")