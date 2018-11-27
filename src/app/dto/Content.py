'''
Created on 2018/11/20

@author: Tanuki
'''

class Content:
        
    id = None
    title = None
    tags = None
    content = None
    users_id = None
    upload_at = None
    update_at = None
    version = None
    
    def __init__(self, content_id, title, tags, content, users_id, upload_at, update_at, version):
        self.id = content_id
        self.title = title
        self.tags = tags
        self.content = content
        self.users_id = users_id
        self.upload_at = upload_at
        self.update_at = update_at
        self.version = version