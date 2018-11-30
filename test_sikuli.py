# _*_ coding:utf-8 _*_
'''
Created on 2015/04/23
@author: Jack.Lin
Description: Open remote desktop console.
'''
from jpype import *
from pickle import NONE
import automan.tool.error as error

if __name__ == '__main__':
    '''
    Constructor
    '''
    
    jvmPath = getDefaultJVMPath()
    startJVM(jvmPath, '-ea', r'-Djava.class.path=./sikulixapi.jar')
    app = JClass('org.sikuli.script.App')
    Screen = JClass('org.sikuli.script.Screen')
    screen = Screen()
    jpgname="./img/HCI/ip.png"
    try:
        x =  screen.wait(jpgname,5)
        if x != "None":
            screen.click(jpgname)
        else:
            raise 
    except :
        raise 