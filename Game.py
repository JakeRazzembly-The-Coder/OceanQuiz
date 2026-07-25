import tkinter as tk

Saved_Name = ""

def _input_get(input, output):
    input = tk.Text.get(output)
    return(output)
    print(Saved_Name)

root = tk.Tk()

root.title("Ocean Quiz")

Name_Input = tk.Text()
Name_Input.grid(column=0, row=0, padx=20, pady=30,)

Save_Name = tk.Button(text="Enter Name", function=lambda: _input_get(Name_Input, Saved_Name))

root.mainloop()