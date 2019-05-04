from flask import request
from Config import Config

class Response:

    def __init__(self, message, pager=None, current_page=None, contents=None, twitter_card=None):
        if request.endpoint == 'router.get_all':
            if request.view_args.get('proc') == 'one':
                self.title = '{0} - {1}'.format(contents[0].title, Config.APP_NAME)
        else:
            self.title = Config.APP_NAME
        self.message = message
        if not(pager is None):
            self.pager = pager
        if not(current_page is None):
            self.current_page = current_page
        if not(contents is None):
            self.contents = contents
        if not(twitter_card is None):
            self.twitter_card = twitter_card
        
        