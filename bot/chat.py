from bot import chatbot
from my_functions import *

while True:
    user = input("Voce: ")
    response = chatbot.get_response(user)
    
    if is_function(response):
        response = call_function(response)
    
    print("Bot: " + str(response))
    print("Confidence: " + str(response.confidence))
