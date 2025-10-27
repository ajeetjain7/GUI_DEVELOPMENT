
import paralleldots
# Setting your API key

class API:

    def __init__(self): #IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk
        paralleldots.set_api_key('a89c02e67a2b8bc9ddd0c112db7e87cd1a7b6522')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner(self,text):
        paralleldots.ner(text)

    def emotion_prediction(self,text):
        paralleldots.emotion(text)