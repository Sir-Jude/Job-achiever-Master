import tkinter
from tkinter import ttk
from tkinter import messagebox as alert
from app_classes_v2 import Candidate
from app_classes_v2 import Recruiter
from app_classes_v2 import Adviser_Bot
from app_classes_v2 import Job

def content_candidate():
    content_frame.destroy()
    write_content()

def write_content():
    content_frame =tkinter.LabelFrame(frame, text="Yeeees", width=frame.winfo_width())
    content_frame.grid(row= 1, column=0, padx=10, pady=10, sticky="nsew")
    button = tkinter.Button(content_frame, text="Surprise!", command = 1)
    button.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# setting the app window
window = tkinter.Tk()
window.title("Job Achiever Master")
window.resizable(False, False)

# setting the frame for the window
frame = tkinter.Frame(window)
frame.pack(fill="both", expand=True)

menu_frame =tkinter.LabelFrame(frame, text="Main menu")
menu_frame.grid(row= 0, column=0, padx=10, pady=10, sticky="nsew")

icon_1 = tkinter.PhotoImage(file="images/icons8-document-writer-50.png")
button_1 = tkinter.Button(menu_frame, text="Candidate info", command = content_candidate, image=icon_1, compound=tkinter.TOP)
button_1.grid(row=0, column=0, padx=(10,5), pady=10)
icon_2 = tkinter.PhotoImage(file="images/icons8-cv-50.png")
button_2 = tkinter.Button(menu_frame, text="CV", command = content_candidate, image=icon_2, compound=tkinter.TOP)
button_2.grid(row=0, column=1, padx=(5,5), pady=10)
button_2.config(state="disabled")
icon_3 = tkinter.PhotoImage(file="images/icons8-stock-share-50.png")
button = tkinter.Button(menu_frame, text="Job details", command = content_candidate, image=icon_3, compound=tkinter.TOP)
button.grid(row=0, column=2, padx=(5,5), pady=10)
icon_4 = tkinter.PhotoImage(file="images/icons8-agreement-50.png")
button = tkinter.Button(menu_frame, text="Cover letter", command = content_candidate, image=icon_4, compound=tkinter.TOP)
button.grid(row=0, column=3, padx=(5,5), pady=10)
icon_5 = tkinter.PhotoImage(file="images/icons8-send-email-50.png")
button = tkinter.Button(menu_frame, text="Email sender", command = content_candidate, image=icon_5, compound=tkinter.TOP)
button.grid(row=0, column=4, padx=(5,5), pady=10)
icon_6 = tkinter.PhotoImage(file="images/icons8-apologise-50.png")
button = tkinter.Button(menu_frame, text="Interview", command = content_candidate, image=icon_6, compound=tkinter.TOP)
button.grid(row=0, column=5, padx=(5,5), pady=10)
icon_7 = tkinter.PhotoImage(file="images/icons8-combo-chart-50.png")
button = tkinter.Button(menu_frame, text="Interview analyse", command = content_candidate, image=icon_7, compound=tkinter.TOP)
button.grid(row=0, column=6, padx=(5,10), pady=10)
window.update()

content_frame = tkinter.LabelFrame(frame, text="Candidate info")
content_frame.grid(row= 1, column=0, padx=10, pady=10, sticky="nsew")

first_name_label = tkinter.Label(content_frame, text="First Name")
first_name_label.grid(row=0, column=0, padx=(10,10), pady=10)
last_name_label = tkinter.Label(content_frame, text="Last Name")
last_name_label.grid(row=0, column=1, padx=(10,10), pady=10)
name_entry = tkinter.Entry(content_frame)
name_entry.grid(row=1, column=0, padx=(10,10), pady=10)
surname_entry = tkinter.Entry(content_frame)
surname_entry.grid(row=1, column=1, padx=(10,10), pady=10)


button = tkinter.Button(content_frame, text="Save", command = 0)
button.grid(row=1, column=2, sticky="news", padx=10, pady=10)









window.mainloop()