import tkinter as tk
from app_classes_v2 import Candidate, Recruiter, Adviser_Bot, Job
import pages.candidate_infos as p_candidate
import pages.job_details as p_job
import time

# setting the app window
window = tk.Tk()
window.title("Job Achiever Master")
window.resizable(False, True)

# defining the main frame for the window
frame = tk.Frame(window)
frame.pack(fill="both", expand=True)

# defining the functions to call the page content constructors
def page_candidate():
    """Place the desire frame and hide the rest."""
    frame_candidate.pack(fill="both", expand=True, padx=10, pady=(5,10))
    frame_job.pack_forget()
    frame_interview.pack_forget()
    frame_analyse.pack_forget()

def page_job():
    """Place the desire frame and hide the rest."""
    frame_candidate.pack_forget()
    frame_job.pack(fill="both", expand=True, padx=10, pady=(5,10))
    frame_interview.pack_forget()
    frame_analyse.pack_forget()

def page_interview():
    """Place the desire frame and hide the rest."""
    frame_candidate.pack_forget()
    frame_job.pack_forget()
    frame_interview.pack(fill="both", expand=True, padx=10, pady=(5,10))
    frame_analyse.pack_forget()

def page_analyse():
    """Place the desire frame and hide the rest."""
    frame_candidate.pack_forget()
    frame_job.pack_forget()
    frame_interview.pack_forget()
    frame_analyse.pack(fill="both", expand=True, padx=10, pady=(5,10))

def download_cv():
    """Call the CV generator and open the PDF file"""
    pass

def download_letter():
    """Call the Cover Letter generator and open the PDF file"""
    pass

def send_email():
    """Call the e-mail sender"""
    pass

# MENU BUTTONS
frame_menu =tk.LabelFrame(frame, text="Main menu")
frame_menu.pack(fill="both", expand=True, padx=10, pady=(10,5))
icon_1 = tk.PhotoImage(file="images/icons8-document-writer-50.png")
button_1 = tk.Button(frame_menu, text="Candidate infos", command = page_candidate, image=icon_1, compound=tk.TOP)
button_1.pack(side="left", padx=(10,5), pady=10)
button_1.config(state="active")
icon_2 = tk.PhotoImage(file="images/icons8-cv-50.png")
button_2 = tk.Button(frame_menu, text="CV", command = download_cv, image=icon_2, compound=tk.TOP)
button_2.pack(side="left", padx=(5,5), pady=10)
button_2.config(state="disabled")
icon_3 = tk.PhotoImage(file="images/icons8-stock-share-50.png")
button_3 = tk.Button(frame_menu, text="Job details", command = page_job, image=icon_3, compound=tk.TOP)
button_3.pack(side="left", padx=(5,5), pady=10)
button_3.config(state="active")
icon_4 = tk.PhotoImage(file="images/icons8-agreement-50.png")
button_4 = tk.Button(frame_menu, text="Cover letter", command = download_letter, image=icon_4, compound=tk.TOP)
button_4.pack(side="left", padx=(5,5), pady=10)
button_4.config(state="disabled")
icon_5 = tk.PhotoImage(file="images/icons8-send-email-50.png")
button_5 = tk.Button(frame_menu, text="Email sender", command = send_email, image=icon_5, compound=tk.TOP)
button_5.pack(side="left", padx=(5,5), pady=10)
button_5.config(state="disabled")
icon_6 = tk.PhotoImage(file="images/icons8-apologise-50.png")
button_6 = tk.Button(frame_menu, text="Interview", command = page_interview, image=icon_6, compound=tk.TOP)
button_6.pack(side="left", padx=(5,5), pady=10)
button_6.config(state="disabled")
icon_7 = tk.PhotoImage(file="images/icons8-combo-chart-50.png")
button_7 = tk.Button(frame_menu, text="Interview analyse", command = page_analyse, image=icon_7, compound=tk.TOP)
button_7.pack(side="left", padx=(5,10), pady=10)
button_7.config(state="disabled")

# CONTENT FRAMES DFINITIONS
# defining frame for page content
frame_page = tk.Frame(frame)
frame_page.pack(fill="both", expand=True)
# defining candidate frame
frame_candidate = tk.LabelFrame(frame_page, text="Candidate info")
frame_candidate.pack(fill="both", expand=True, padx=10, pady=(5,10))
p_candidate.write_page(frame_candidate)
# defining candidate frame
frame_job = tk.LabelFrame(frame_page, text="Job description")
frame_job.pack(fill="both", expand=True, padx=10, pady=(5,10))
p_job.write_page(frame_job)
# defining candidate frame
frame_interview = tk.LabelFrame(frame_page, text="Interview simulation")
frame_interview.pack(fill="both", expand=True, padx=10, pady=(5,10))
# defining candidate frame
frame_analyse = tk.LabelFrame(frame_page, text="Interview analyse")
frame_analyse.pack(fill="both", expand=True, padx=10, pady=(5,10))

# default the app starts with candidate page
page_candidate()
# starting the graphic interface
window.mainloop()