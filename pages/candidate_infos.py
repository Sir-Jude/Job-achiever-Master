import tkinter
from tkinter import ttk
from tkinter import messagebox as alert
from app_classes_v2 import Candidate, Recruiter, Adviser_Bot, Job

def write_page(frame):
    # definig the content frame
    content_frame = tkinter.LabelFrame(frame, text="Candidate infos")
    content_frame.grid(row= 1, column=0, padx=10, pady=10, sticky="nsew")

    # defining form elements
    # row 0
    name_label = tkinter.Label(content_frame, text="Name")
    name_label.grid(row=0, column=0, padx=(10,10), pady=10)
    surname_label = tkinter.Label(content_frame, text="Surame")
    surname_label.grid(row=0, column=1, padx=(10,10), pady=10)
    birthday_label = tkinter.Label(content_frame, text="Birthday")
    birthday_label.grid(row=0, column=2, padx=(10,10), pady=10)
    birthday_label = tkinter.Label(content_frame, text="Sex")
    birthday_label.grid(row=0, column=3, padx=(10,10), pady=10)
    # row 1
    name_entry = tkinter.Entry(content_frame)
    name_entry.grid(row=1, column=0, padx=(10,10), pady=10)
    surname_entry = tkinter.Entry(content_frame)
    surname_entry.grid(row=1, column=1, padx=(10,10), pady=10)
    birthday_entry = tkinter.Entry(content_frame)
    birthday_entry.grid(row=1, column=2, padx=(10,10), pady=10)
    sex_combobox = ttk.Combobox(content_frame, values=["male", "female"])
    sex_combobox.grid(row=1, column=3, padx=(10,10), pady=10)
    # row 2
    button = tkinter.Button(content_frame, text="Save candidate", command = 0)
    button.grid(row=2, column=0, sticky="news", padx=10, pady=10)
