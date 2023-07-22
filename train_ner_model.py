import os
import spacy
from spacy.training.example import Example
import random
import json

# Specify the file path to the JSON file containing training data
data_file_path = r"C:\chatbotproject\training_data.json"

# Load the blank English model
nlp = spacy.blank("en")

# Load the spaCy NER model
ner = nlp.create_pipe("ner")
nlp.add_pipe(ner, last=True)

# Read the training data from the JSON file
with open(data_file_path, "r") as f:
    TRAIN_DATA = json.load(f)

# Define your custom entity labels based on your training data
for text, annotations in TRAIN_DATA:
    for ent in annotations.get("entities"):
        nlp.vocab.strings.add(ent[2])

# Get the ner component
ner = nlp.get_pipe("ner")

# Add the custom labels to the NER component
for text, annotations in TRAIN_DATA:
    example = Example.from_dict(nlp.make_doc(text), annotations)
    nlp.update([example], drop=0.5)  # You can adjust the drop value based on your data size

# Save the trained NER model to a specified directory
output_dir = "C:/chatbotproject/trained_ner_model"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
nlp.to_disk(output_dir)
print("NER Model trained and saved to:", output_dir)

# Split data into training and evaluation sets
random.shuffle(TRAIN_DATA)
train_data = TRAIN_DATA[:int(len(TRAIN_DATA) * 0.8)]
eval_data = TRAIN_DATA[int(len(TRAIN_DATA) * 0.8):]

# Start training the full model
for epoch in range(10):
    random.shuffle(train_data)
    losses = {}
    for text, annotations in train_data:
        nlp.update([text], [annotations], drop=0.5, losses=losses)
    print("Epoch:", epoch, "Losses:", losses)

# Save the trained model to disk
output_dir = "trained_ner_model"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
nlp.to_disk(output_dir)
print("Full model trained and saved to:", output_dir)
