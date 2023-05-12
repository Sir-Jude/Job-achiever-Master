import tkinter
from tkinter import ttk
from tkinter import messagebox as alert
from app_classes_v2 import Candidate, Recruiter, Adviser_Bot, Job
import pages.candidate_infos as c_infos
import pages.job_details as j_infos


# setting the app window
window = tkinter.Tk()
window.title("Job Achiever Master")
window.resizable(False, False)

# defining the main frame for the window
frame = tkinter.Frame(window)
frame.pack(fill="both", expand=True)

# defining a labeled frame for the menu
menu_frame =tkinter.LabelFrame(frame, text="Main menu")
menu_frame.grid(row= 0, column=0, padx=10, pady=10, sticky="nsew") # sticky = how is aligned (north, south...)
# defining a labeled frame for the content
content_frame = tkinter.LabelFrame(frame, text="Candidate info")
content_frame.grid(row= 1, column=0, padx=(10,10), pady=10, sticky="nsew") # padx or pady can have 1 or 2 parameters

# defining the functions to call the content constructors from menu
def update_candidate():
    content_frame.destroy()
    c_infos.write_page(frame)

def download_cv():
    content_frame.destroy()
    pass

def update_job():
    content_frame.destroy()
    j_infos.write_page(frame)

def download_letter():
    content_frame.destroy()
    pass

def send_email():
    content_frame.destroy()
    pass

def run_interview():
    content_frame.destroy()
    pass

def analyse_interview():
    content_frame.destroy()
    pass

# MENU BUTTONS
icon_1 = tkinter.PhotoImage(file="images/icons8-document-writer-50.png")
button_1 = tkinter.Button(menu_frame, text="Candidate infos", command = update_candidate, image=icon_1, compound=tkinter.TOP)
button_1.grid(row=0, column=0, padx=(10,5), pady=10)
icon_2 = tkinter.PhotoImage(file="images/icons8-cv-50.png")
button_2 = tkinter.Button(menu_frame, text="CV", command = download_cv, image=icon_2, compound=tkinter.TOP)
button_2.grid(row=0, column=1, padx=(5,5), pady=10)
button_2.config(state="disabled")
icon_3 = tkinter.PhotoImage(file="images/icons8-stock-share-50.png")
button = tkinter.Button(menu_frame, text="Job details", command = update_job, image=icon_3, compound=tkinter.TOP)
button.grid(row=0, column=2, padx=(5,5), pady=10)
icon_4 = tkinter.PhotoImage(file="images/icons8-agreement-50.png")
button = tkinter.Button(menu_frame, text="Cover letter", command = download_letter, image=icon_4, compound=tkinter.TOP)
button.grid(row=0, column=3, padx=(5,5), pady=10)
icon_5 = tkinter.PhotoImage(file="images/icons8-send-email-50.png")
button = tkinter.Button(menu_frame, text="Email sender", command = send_email, image=icon_5, compound=tkinter.TOP)
button.grid(row=0, column=4, padx=(5,5), pady=10)
icon_6 = tkinter.PhotoImage(file="images/icons8-apologise-50.png")
button = tkinter.Button(menu_frame, text="Interview", command = run_interview, image=icon_6, compound=tkinter.TOP)
button.grid(row=0, column=5, padx=(5,5), pady=10)
icon_7 = tkinter.PhotoImage(file="images/icons8-combo-chart-50.png")
button = tkinter.Button(menu_frame, text="Interview analyse", command = analyse_interview, image=icon_7, compound=tkinter.TOP)
button.grid(row=0, column=6, padx=(5,10), pady=10)

# default the app starts with candidate page
update_candidate()
# starting the graphic interface
window.mainloop()