'''
Created on 2018/11/21

@author: Tanuki
'''


class Config(object):
    APP_NAME = 'Prome'
    DEBUG = True
    SQLALCHEMY_ECHO = True
    DATABASE_URI =  'postgresql://postgres:docker_postgre_task320@localhost:5432/test_db'
    DISPLAY_NUMBER_OF_CONTENTS = 5

    TWITTER_ACCOUNT = 'task320'
    TWITTER_CARD_IMAGE = 'https://storage.googleapis.com/prome-238513.appspot.com/twitter_card_image.png'

        
        