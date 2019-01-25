'''
Created on 2018/11/21

@author: Tanuki
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import VARCHAR, TIMESTAMP

Base = declarative_base()

class Users(Base):
  
    __tablename__ = 'users'
    
    id = Column(VARCHAR(32), primary_key=True)
    password = Column(VARCHAR(32))
    create_at = Column(TIMESTAMP)
    update_at = Column(TIMESTAMP)
    
    def __repr__(self):
        return "<Users(id='%r', create_at='%r', update_at='%r')>" % (self.id, self.create_at, self.update_at)