from setuptools import setup, find_packages

setup(
    name='chatbot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'spacy',
        'chatterbot',
        # Add any other dependencies here
    ],
)
