from flask import jsonify
from flask_restful import Resource
from config.chatbot_config import Bot

# CHATBOT OBJECT INITIALIZATION
chatBot = Bot('Charlie')
# TRAIN CHATBOT
chatBot.trainBot()

# RESOURCES THAT WILL BE EXPORTED FOR ENDPOINT USAGE

# CONTROLLER FOR COLLECTING CUSTOM MESSAGE FROM USER
class BotController(Resource):
    def post(self,message):
        return {'response': str(chatBot.sayToBot(message))},200

# CONTROLLER FOR STARTING BOT SELF INTRODUCTION
class BotStarter(Resource):
    def get(self):
        return {'response':'Hellow, my name is charlie'},200

# CONTROLLER FOR USER INSTRUCTION BEFORE BOT STARTS
class BotDefault(Resource):
    def get(self):
        return {'response':'Tap help to start'},200

# CONTROLLER FOR HELP TEXT
class Help(Resource):
    def get(self):
        return {'response':'Here is a Help Text'},200