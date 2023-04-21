import openai, sys, os
from stringcolor import *
import time

"""openai.api_key = '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'"""
openai.api_key = "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"


sys_message_1 = """Tu esti un consilier de la Jobcenter din Magdeburg.
Vei raspnde doar in limba germana.
Nu cunosti alta limba decat germana.
Vei fi politicos dar si grabit.
De aceea vei da replici scurte."""
sys_message_2 = """Tu esti un profesor de limba germana si verifici daca schimbul de replici dintre doua persoane.
Vei comenta doar replicile a lui Adrian.
Vei verifica daca utima replica a lui Adrian este scrisa corect in limba germana si potrivita in dialog.
Daca ultima replica a lui Adrian contine orice tip de gresala raspunzi doar cu varianta corectata."""
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
