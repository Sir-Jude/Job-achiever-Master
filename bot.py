import openai, sys, os
from stringcolor import *
import time

"""openai.api_key = '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'"""
openai.api_key = "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"


sys_message_1 = """You are a counselor at the Jobcenter in Magdeburg.
You will only respond in German.
You know no other language than German.
You will be polite but also in a hurry.
That is why you will give short lines."""
sys_message_2 = """You are a German language teacher and you check if the exchange of lines between two people.
You will only comment on Adrian's lines.
You will check if Adrian's last reply is written correctly in German and appropriate in the dialogue.
If Adrian's last reply contains any type of mistake, only reply with the corrected version."""
messages_list_1 = [{"role": "system", "content": sys_message_1}]
messages_list_1.append({"role": "user", "content": "Guten Tag!"})
messages_list_2 = [{"role": "system", "content": sys_message_2}]
print("Adrian: Guten Tag!")
loop = True
index = 0
while loop == True:
    # bot turn
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages_list_1, temperature=0.2
    )
    result_1 = response.choices[0].message.content
    messages_list_1.append({"role": "assistant", "content": result_1})
    print(cs(f"Consilier: ", "CYAN") + cs(result_1, "BLUE"))
    time.sleep(2)

    # user turn
    user_message = input("Adrian: ")
    if user_message.upper() == "EXIT":
        loop = False
    messages_list_1.append({"role": "user", "content": user_message})

    # teacher turn
    messages_list_2 = [{"role": "system", "content": sys_message_2}]
    messages_list_2.append(
        {"role": "user", "content": f"Adrian: {user_message}\nConsilier: {result_1}"}
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages_list_2, temperature=0.1
    )
    result_2 = response.choices[0].message.content
    messages_list_2.append({"role": "assistant", "content": result_2})
    print(cs(f"Profesor: ", "RED") + cs(result_2, "RED"))
    time.sleep(2)

    index += 1
"""for m in messages_list_1:
    print(f'{m["role"]}: {m["content"]}')"""
