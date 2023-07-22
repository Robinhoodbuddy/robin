from chatbot import chatbot
from nlp import nlp_api

def get_chatbot_response(user_input):
    entities = nlp_api.extract_entities(user_input)
    response = chatbot.get_response(user_input, entities)
    return response
