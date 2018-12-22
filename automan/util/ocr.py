#coding=utf-8
'''
Created on 2018

@author: Tim.Huang
'''
import datetime
from PIL import Image
from pytesseract import image_to_string

class Ocr(object):
    def __init__(self):
        '''
        '''

    def image_text_get(self,dict):
        #file = "receipt.png"
        file = dict['file']
        img = Image.open(file);
        text = image_to_string(img,config='-psm 5')
        text = ''.join(text[::-1])
        text = text.replace('\n', '').replace('\r', '').upper()
        return text
    
    def image_text_test(self,dict):
        print dict["test"]

if __name__ == '__main__':
    print "dssd"
    print Ocr().image_text_get("")
    