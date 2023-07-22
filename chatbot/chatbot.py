import random
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Chatbot:
    def __init__(self):
        self.responses = {
            "What is Python?": "Python is a high-level programming language known for its simplicity and readability.",
            "How do I define a function in Python?": "You can define a function in Python using the 'def' keyword.",
            "What is a variable?": "A variable is a storage location in a program where you can store a value.",
            # Add more responses as needed
        }

        self.chatbot = ChatBot('MyChatBot')
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)

        # Train the chatbot on English language corpus
        self.trainer.train('chatterbot.corpus.english')

    def get_response(self, question):
        # Check if the response is available in the pre-defined responses
        response = self.responses.get(question)
        if response is not None:
            return response

        # If not found, use the ChatterBot to get a response
        response = self.chatbot.get_response(question)
        return str(response)
