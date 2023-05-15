import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as alert
from app_classes_v2 import Candidate, Recruiter, Adviser_Bot, Job
import app_functions

def write_page(frame_name):
    """Write the graphic content of the formular"""
    frame_info = tk.Frame(frame_name)
    frame_info.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    entries = [] # a list to store the form objects dinamicaly created for later calling
    def update_info(event):
        """Call the form elements values when focus changes to save them.
        This way every changes in form fields update the dictionary."""
        widget = event.widget
        key_index = entries.index(widget)
        key = list(Candidate.data.keys())[key_index]
        if isinstance(widget, tk.Entry):
            value = widget.get() # this method take values from Entry tk.objects
        else:
            value = widget.get("1.0", tk.END) # this method take values from Text tk.objects
        Candidate.data[key] = value
        Candidate.save_infos()

    # First section of the form to colect basic candidate infos
    frame_1 = tk.Frame(frame_info)
    frame_1.pack(fill=tk.BOTH, expand=True)
    # This section splited in 2 columns
    frame_left = tk.Frame(frame_1)
    frame_left.pack(fill=tk.BOTH, expand=True, padx=(0,5),side="left")
    frame_right = tk.Frame(frame_1)
    frame_right.pack(fill=tk.BOTH, expand=True, padx=(5,0), side="right")
    # Generating dinamicaly the form fields for first 8 keys in dictionary
    for i, (key, value) in enumerate(Candidate.data.items()):
        if i < 4:
            frame = tk.Frame(frame_left)
        elif 3 < i < 8:
            frame = tk.Frame(frame_right)
        else:
            break
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        label = tk.Label(frame, text=key.capitalize())
        label.config(width=13, anchor="e")
        label.pack(padx=(0,10), side="left")
        entry = tk.Entry(frame)
        entry.insert(0, value)
        entry.bind("<FocusOut>", update_info)
        entry.pack(fill="x", expand=True, side="right")
        entries.append(entry)

    # Generating dinamicaly the form fields for 9.th key in dictionary
    frame_2 = tk.Frame(frame_info)
    frame_2.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    label = tk.Label(frame_2, text="Short description")
    label.config(width=14, anchor="e")
    label.pack(padx=(0,10), side="left")
    text = tk.Text(frame_2, height=5)
    text.insert("1.0", Candidate.data["short_description"])
    text.bind("<FocusOut>", update_info)
    text.pack(fill="x", expand=True, side="right")
    entries.append(text)

    # Generating the sub section Experience
    frame_experience = tk.LabelFrame(frame_info, text="Experience")
    frame_experience.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Generating each experience frame
    for exp in Candidate.data["experience"]:
        frame_exp_item = tk.LabelFrame(frame_experience)
        frame_exp_item.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        informations = f"{exp['title']}"
        text_exp_item = tk.Message(frame_exp_item, text = informations)
        text_exp_item.pack(side="left")
        for key, value in exp.items():
            entry = tk.Entry(frame_exp_item)
            entry.insert(0, value)
            if key == "date_start" or key == "date_end":
                entry.config(width=10)
                entry.pack(side="left")
            elif key == "description":
                entry.pack(fill="x", expand=True, side="left")
            entry.pack(side="left")
            entries.append(entry)
        button = tk.Button(frame_exp_item, text="-", command = 0)
        button.pack(side="left")
    
    frame_exp_new = tk.LabelFrame(frame_experience)
    frame_exp_new.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    entry_title = tk.Entry(frame_exp_new)
    entry_title.pack(side="left")
    entry_description = tk.Entry(frame_exp_new)
    entry_description.pack(fill="x", expand=True, side="left")
    entry_company = tk.Entry(frame_exp_new)
    entry_company.pack(side="left")
    entry_start = tk.Entry(frame_exp_new)
    entry_start.config(width=10)
    entry_start.pack(side="left")
    entry_end = tk.Entry(frame_exp_new)
    entry_end.config(width=10)
    entry_end.pack(side="left")
    button = tk.Button(frame_exp_new, text="+", command = 0)
    button.pack(side="left")
