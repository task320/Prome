'''
Created on 2018/11/21

@author: Tanuki
'''


class Config(object):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    DATABASE_URI =  'postgresql://postgres:docker_postgre_task320@localhost:5432/test_db'
    DISPLAY_NUMBER_OF_CONTENTS = 5

        
        