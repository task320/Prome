'''
Created on 2018/11/21

@author: Tanuki
'''
import os

class Config:
    APP_NAME = 'Prome'
    DEBUG = False
    SQLALCHEMY_ECHO = False
    DATABASE_URI =  os.getenv('DATABASE_URI')
    DISPLAY_NUMBER_OF_CONTENTS = 5

    TWITTER_ACCOUNT = 'task320'
    TWITTER_CARD_IMAGE = 'https://storage.googleapis.com/prome-238513.appspot.com/twitter_card_image.png'
