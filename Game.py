import tkinter as tk

Saved_Name = ""

def _input_get(input, output):
    output = input.get()
    return(output)

root = tk.Tk()

root.title("Ocean Quiz")

Name_Input = tk.Entry()
Name_Input.grid(column=0, row=0, padx=20, pady=30,)

Save_Name = tk.Button(text="Enter Name", command=lambda: _input_get(Name_Input, Saved_Name))
Save_Name.grid(column=1, row=0, padx=20, pady=30,)

root.mainloop()