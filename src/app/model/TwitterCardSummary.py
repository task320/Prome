from Config import Config 

class TwitterCardSummary:
    def __init__(self, content ):
        self.card = 'summary'
        self.site = Config.TWITTER_ACCOUNT
        self.title = content.title
        self.image = Config.TWITTER_CARD_IMAGE