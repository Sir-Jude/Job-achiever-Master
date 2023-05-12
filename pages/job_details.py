import tkinter
from tkinter import ttk
from tkinter import messagebox as alert
from app_classes_v2 import Candidate, Recruiter, Adviser_Bot, Job

def write_page(frame):
    content_frame = tkinter.LabelFrame(frame, text="Job details")
    content_frame.grid(row= 1, column=0, padx=10, pady=10, sticky="nsew")

    first_name_label = tkinter.Label(content_frame, text="First Name")
    first_name_label.grid(row=0, column=0, padx=(10,10), pady=10)
    last_name_label = tkinter.Label(content_frame, text="Last Name")
    last_name_label.grid(row=0, column=1, padx=(10,10), pady=10)
    name_entry = tkinter.Entry(content_frame)
    name_entry.grid(row=1, column=0, padx=(10,10), pady=10)
    surname_entry = tkinter.Entry(content_frame)
    surname_entry.grid(row=1, column=1, padx=(10,10), pady=10)


    button = tkinter.Button(content_frame, text="Save job", command = 0)
    button.grid(row=1, column=2, sticky="news", padx=10, pady=10)
