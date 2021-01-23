from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logic_adapter.logic_adapter as logic

class Bot:
    
    botName = None
    chatbot = None

    # Bot Initialization
    def __init__(self,name):
        # INITIALIZING BOT NAME
        Bot.botName = name

        # INITIALIZING CHATBOT WITH NAME AND LOGICAL ADAPTER
        Bot.chatbot = ChatBot(Bot.botName,logic_adapters=logic.adapters)
    

    def trainBot(self):
        trainer = ChatterBotCorpusTrainer(Bot.chatbot)
        # TRAINING STARTS NOW
        # trainer.train('chatterbot.corpus.english')
        trainer.train("./conversation/custom.yml")

    def sayToBot(self,say):
        return Bot.chatbot.get_response(say)

    