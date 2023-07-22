import spacy
import json
import os
import random

# Specify the file path to the JSON file
data_file_path = r"C:\chatbotproject\training_data.json"

# Read the data from the JSON file
with open(data_file_path, "r") as f:
    TRAIN_DATA = json.load(f)

# Load the spaCy NER model
nlp = spacy.blank("en")
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner, last=True)

# Add your entity labels to the NER model
for text, annotations in TRAIN_DATA:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# Start training
nlp.begin_training()
for epoch in range(10):
    random.shuffle(TRAIN_DATA)
    losses = {}
    for text, annotations in TRAIN_DATA:
        nlp.update([text], [annotations], drop=0.5, losses=losses)
    print("Epoch:", epoch, "Losses:", losses)

# Save the trained model to disk
output_dir = "trained_ner_model"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
nlp.to_disk(output_dir)

# Load the trained NER model
ner_model = spacy.load("trained_ner_model")
# Function to extract programming-related entities from user input
def extract_programming_entities(user_input):
    doc = ner_model(user_input)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def create_chatbot():
    responses = {
        "What is Python?": "Python is a high-level programming language known for its simplicity and readability.",
        "How do I define a function in Python?": "You can define a function in Python using the 'def' keyword.",
        "What is a variable?": "A variable is a storage location in a program where you can store a value.",
        "How do I create a loop in Python?": "You can create a loop in Python using 'for' and 'while' statements.",
        "What is the difference between '==' and 'is' in Python?": "'==' checks for equality, while 'is' checks for object identity.",
        "What is the purpose of 'if' statements in Python?": "'if' statements are used for conditional execution in Python.",
        "How do I read input from the user in Python?": "You can use the 'input()' function to read input from the user.",
        "What is a list in Python?": "A list is a collection of items in a specific order.",
        "How do I install packages in Python?": "You can use 'pip' to install packages in Python.",
        "What is a dictionary in Python?": "A dictionary is a collection of key-value pairs.",
        "How do I handle exceptions in Python?": "You can use 'try', 'except', and 'finally' blocks to handle exceptions.",
        "Arsalan Keya?": "kora, Arsalan bazmi has, fra qsa xosha, yo yo, wadab wadab, tanya aybeki haya qomarchi ya.",
    }

    def get_response(question):
        response = responses.get(question, "I'm sorry, I don't have an answer for that question.")
        return response

    return get_response

def interact_with_chatbot(chatbot):
    print("Hello! I am your programming chatbot. How can I assist you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Extract programming-related entities from user input
        entities = extract_programming_entities(user_input)
        print("Extracted entities:", entities)

        response = chatbot(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    programming_chatbot = create_chatbot()
    interact_with_chatbot(programming_chatbot)
