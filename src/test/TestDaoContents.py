'''
Created on 2018/11/22

@author: Tanuki
'''

import unittest
from app.dao import Contents
from app.dto import Content
from test import DbConnect

db_connect = DbConnect()

class TestDaoContent(unittest.TestCase):
    def test_insert(self):
        content = Content()
        content.title = "ユニットテスト"
        content.
        contents = Contents()
        contents.db = db_connect.db
        
        contents.insertContent()

if __name__ == '__main__':
    unittest.main()