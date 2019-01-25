'''
Created on 2018/11/21

@author: Tanuki
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column, Sequence
from sqlalchemy.types import Integer, VARCHAR, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import ARRAY

Base = declarative_base()

class Contents(Base):
    
    __tablename__ = 'contents'
    
    id = Column(Integer, Sequence('contents_id_seq'), primary_key=True)
    title = Column(VARCHAR(128))
    tags = Column(ARRAY(VARCHAR(32)))
    content = Column(Text)
    users_id = Column(VARCHAR(32))
    upload_at = Column(TIMESTAMP)
    update_at = Column(TIMESTAMP)
    version = Column(Integer())
    
    def __repr__(self):
        return "<CONTENTS(id='%r', title='%r', users_id='%r', version='%r')>" % (self.id, self.title, self.users_id, self.version)