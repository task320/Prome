'''
Created on 2018/11/20

@author: Tanuki
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Config import Config

session = None

class DbConection:

    def __init__(self):
        engine = create_engine(Config.DATABASE_URI, echo=Config.SQLALCHEMY_ECHO)
        self.session = sessionmaker(bind=engine)
        