'''
Created on 2018/11/18

@author: Tanuki
'''
import os
from app  import create_app

config_name = os.getenv('PROME_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run(debug=True)