'''

Steps:
1. Set up spaCy for natural language processing.
2. Implement the chatbot logic to handle user inputs.
3. Define a set of conversational responses.




install spaCy and download the English language model using : 
pip install spacy
python -m spacy download en_core_web_sm




'''

import spacy
import random

# Load spaCy's small English model
nlp = spacy.load('en_core_web_sm')

# Predefined responses based on intents
RESPONSES = {
    'greet': ["Hello! How can I help you today?", "Hi there! How are you doing?", "Hello! What can I do for you?"],
    'goodbye': ["Goodbye! Have a nice day!", "See you later!", "Bye! Take care!"],
    'thanks': ["You're welcome!", "No problem!", "Glad I could help!"],
    'weather': ["It's sunny outside.", "It might rain later today.", "Looks like it's a good day to go outside!"],
    'unknown': ["I'm not sure I understand.", "Can you clarify that?", "I'm still learning! Can you rephrase?"]
}

# Sample keywords associated with different intents
KEYWORDS = {
    'greet': ['hello', 'hi', 'hey', 'morning'],
    'goodbye': ['bye', 'goodbye', 'see you', 'later'],
    'thanks': ['thanks', 'thank', 'appreciate'],
    'weather': ['weather', 'sunny', 'rain', 'cloudy']
}

def get_intent(user_input):
    """Process the user input and return the intent based on keywords"""
    doc = nlp(user_input.lower())

    for token in doc:
        for intent, keywords in KEYWORDS.items():
            if token.lemma_ in keywords:
                return intent
    return 'unknown'

def chatbot_response(intent):
    """Return a random response based on the detected intent"""
    return random.choice(RESPONSES[intent])

def chatbot():
    print("Chatbot: Hi! I'm here to chat with you. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Get the intent from user input
        intent = get_intent(user_input)

        # Generate and print the chatbot response
        response = chatbot_response(intent)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == '__main__':
    chatbot()







'''



How It Works:
1. Natural Language Processing (NLP):
The chatbot uses spaCy to process user input. It tokenizes and lemmatizes the input to find keywords associated with specific intents.
For example, if the input contains the word "hello", the chatbot identifies it as a greeting.


2. Intents and Responses:
We define basic intents like "greet", "goodbye", "thanks", and "weather".
Based on the recognized intent, the chatbot selects a response from a set of predefined options.

3. Running the Chatbot:
When the program starts, it will wait for user input, process it using spaCy, and respond accordingly.
The user can end the conversation by typing "exit".





EXAMPLE WORKING : 

Chatbot: Hi! I'm here to chat with you. Type 'exit' to end the conversation.
You: Hello
Chatbot: Hi there! How are you doing?
You: Can you tell me about the weather?
Chatbot: It's sunny outside.
You: Thanks
Chatbot: You're welcome!
You: Bye
Chatbot: See you later!

'''
