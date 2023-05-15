import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as alert
from app_classes_v2 import Candidate, Recruiter, Adviser_Bot, Job
import app_functions

def write_page(frame_name):
    # definig the content frame
    info_frame = tk.Frame(frame_name)
    info_frame.pack(fill=tk.BOTH, expand=True, side="left")
    details_frame = tk.Frame(frame_name)
    details_frame.pack(fill=tk.BOTH, expand=True, side="right")

    label1 = tk.Label(info_frame, text="aaaa 1")
    label1.pack()

    label2 = tk.Label(details_frame, text="eeee 2")
    label2.pack()

    label3 = tk.Label(details_frame, text="uuuu 3")
    label3.pack()
