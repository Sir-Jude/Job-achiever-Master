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

    def update_candidate(key):
        """Update candidate field and save it in json"""
        widget = event.widget
        value = widget.get() # this method take values from Entry tk.objects
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
    #Creating the field names
    frame_exp_fields = tk.LabelFrame(frame_experience)
    frame_exp_fields.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    item_title = tk.Label(frame_exp_fields, text = "Title")
    item_title.config(width=16)
    item_title.pack(side="left")
    item_description = tk.Label(frame_exp_fields, text = "Description")
    item_description.config(width=20)
    item_description.pack(fill="x", expand=True, side="left")
    item_company = tk.Label(frame_exp_fields, text = "Company")
    item_company.pack(side="left")
    item_company.config(width=16)
    item_start = tk.Label(frame_exp_fields, text = "Start date")
    item_start.config(width=10)
    item_start.pack(side="left")
    item_end = tk.Label(frame_exp_fields, text = "End date")
    item_end.config(width=10)
    item_end.pack(side="left")
    button_add = tk.Button(frame_exp_fields, text=" ", command = 0)
    button_add.pack(side="left")

    # Generating each experience item
    for exp in Candidate.data["experience"]:
        frame_exp_item = tk.LabelFrame(frame_experience)
        frame_exp_item.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        entry_title = tk.Entry(frame_exp_item)
        entry_title.insert(0, exp['title'])
        entry_title.config(width=16)
        entry_title.pack(side="left")
        entry_description = tk.Entry(frame_exp_item)
        entry_description.insert(0, exp['description'])
        entry_description.config(width=20)
        entry_description.pack(fill="x", expand=True, side="left")
        entry_company = tk.Entry(frame_exp_item)
        entry_company.insert(0, exp['company'])
        entry_company.config(width=16)
        entry_company.pack(side="left")
        entry_start = tk.Entry(frame_exp_item)
        entry_start.insert(0, exp['date_start'])
        entry_start.config(width=10)
        entry_start.pack(side="left")
        entry_end = tk.Entry(frame_exp_item)
        entry_end.insert(0, exp['date_end'])
        entry_end.config(width=10)
        entry_end.pack(side="left")
        button_delete = tk.Button(frame_exp_item, text="-", command = 0)
        button_delete.pack(side="left")
    #Creating the form for a new experience item
    frame_exp_new = tk.LabelFrame(frame_experience)
    frame_exp_new.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    entry_title = tk.Entry(frame_exp_new)
    entry_title.config(width=16)
    entry_title.pack(side="left")
    entry_description = tk.Entry(frame_exp_new)
    entry_description.config(width=20)
    entry_description.pack(fill="x", expand=True, side="left")
    entry_company = tk.Entry(frame_exp_new)
    entry_company.config(width=16)
    entry_company.pack(side="left")
    entry_start = tk.Entry(frame_exp_new)
    entry_start.config(width=10)
    entry_start.pack(side="left")
    entry_end = tk.Entry(frame_exp_new)
    entry_end.config(width=10)
    entry_end.pack(side="left")
    button_add = tk.Button(frame_exp_new, text="+", command = 0)
    button_add.pack(side="left")
