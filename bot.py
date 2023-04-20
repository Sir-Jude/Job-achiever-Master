import openai, sys, os
from stringcolor import *


openai.api_key = "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"

role = """You are a (insert what bot should be)"""

loop = True
while loop == True:
    user = input("YOU: ")
    if user.upper() == "EXIT":
        loop = False 
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": user},])
    result = ''
    for choice in response.choices:
        result += choice.message.content
    print(cs(f"GPT: ","CYAN")+cs(result,"BLUE"))
