import openai
from stringcolor import * # for color, importing stringcolor library

openai.api_key = "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" # api key
model 	       = "gpt-3.5-turbo" # choosing gpt model

role = """You are a summarizer. Every input you get, you directly summarize to a short and
           concise form. You do not give any other output than the Summary. You do not ask
           questions or say anything else than the summary of the given input."""

def custom_input(prompt=""): # aint working, gotta get fixed (or read a file and let content be file content)
    print(prompt, end="")
    lines = []
    consecutive_newlines = 0

    while consecutive_newlines < 3:
        try:
            character = input()[0]  # Read one character
            consecutive_newlines = 0
        except IndexError:  # User pressed Enter
            character = "\n"
            consecutive_newlines += 1

        if consecutive_newlines < 3:
            lines.append(character)
            if character == "\n":
                print(end="")
            else:
                print(character, end="")
    return "".join(lines)

class Summarizer: # AI summarizing articles 
    def __init__(self):
        self.role = role

    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
            {"role": "system", "content": self.role},
            {"role": "user", "content": user_input},]
        )
        result = response.choices[0].message.content
        return result

bot = Summarizer()

with open("to_be_summarized.txt","r") as file:
    content = file

content = custom_input("Give me something to summarize: ")

print(bot.get_response(content))

print("CONTENT: ",content)