import tkinter as tk

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    print("Name colected:", name)
    print("Age colected:", age)

# Create the window
window = tk.Tk()
window.geometry("300x200")  # Setting the window size (width x height)

# Creating input field for name
name_label = tk.Label(window, text="Name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

# Creating the input field for age
age_label = tk.Label(window, text="Age:")
age_label.pack()

age_entry = tk.Entry(window)
age_entry.pack()

# Creating the form submit button
submit_button = tk.Button(window, text="Send", command=submit_form)
submit_button.pack()

# Setting the position of elements in the form
name_label.place(x=20, y=20) 
name_entry.place(x=100, y=20)  
age_label.place(x=20, y=50)  
age_entry.place(x=100, y=50)  
submit_button.place(x=150, y=100)  

# Starting the main event loop
window.mainloop()