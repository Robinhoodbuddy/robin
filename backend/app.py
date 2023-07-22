from flask import Flask, request, jsonify
from chatbot import Chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import configparser
from github import Github  # Import PyGithub library
from github_api import get_github_repository, get_github_issues  # Import functions from github_api module

# Import the new libraries
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymongo

# Initialize Flask app
app = Flask(__name__)

# Load configurations from config.ini
config = configparser.ConfigParser()
config.read('config/config.ini')

# Create a Chatbot instance
chatbot = Chatbot()

# Optionally, you can use ChatterBot as well
chatterbot = ChatBot('MyChatBot')
chatterbot_trainer = ChatterBotCorpusTrainer(chatterbot)

# Train the ChatterBot on the English language corpus
chatterbot_trainer.train(config.get('chatterbot', 'chatterbot_corpus'))

# API endpoint for handling user queries
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data['question']

    # Get response from the chatbot
    response = chatbot.get_response(question)

    return jsonify({'response': response})

# API endpoint for handling ChatterBot responses
@app.route('/api/chatterbot', methods=['POST'])
def chatterbot_response():
    data = request.get_json()
    question = data['question']

    # Get response from ChatterBot
    response = str(chatterbot.get_response(question))

    return jsonify({'response': response})

# API endpoint for retrieving GitHub repository information
@app.route('/api/github_repository', methods=['GET'])
def github_repository():
    owner = request.args.get('owner')
    repo_name = request.args.get('repo_name')
    token = "your_github_token"  # Replace with your actual GitHub personal access token

    repository_info = get_github_repository(owner, repo_name, token)
    return jsonify(repository_info)

# API endpoint for retrieving GitHub issues
@app.route('/api/github_issues', methods=['GET'])
def github_issues():
    owner = request.args.get('owner')
    repo_name = request.args.get('repo_name')
    token = "your_github_token"  # Replace with your actual GitHub personal access token

    issues_list = get_github_issues(owner, repo_name, token)
    return jsonify(issues_list)

if __name__ == '__main__':
    app.run(debug=config.getboolean('general', 'debug'), port=config.getint('general', 'port'))
