from flask import Flask ,jsonify,request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])

app = Flask(__name__)

@app.route('/')
def index():
    # response = chatbot.get_response('I would like to book a flight.')
    return str(chatbot.get_response('I would like to book a flight.'))

if __name__ == '__main__':
    app.run(debug=True)