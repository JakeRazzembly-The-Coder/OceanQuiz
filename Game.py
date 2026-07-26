import tkinter as tk

Saved_Name = ""

def _input_get(input, output, error):
    output = input.get().strip()
    if output == "":
        error.set("Enter a Text")
    else:
        return(output)

root = tk.Tk()

Name_Error_TextVar = tk.StringVar(root, value="")

root.title("Ocean Quiz")

Name_Input = tk.Entry(root,)

Save_Name = tk.Button(text="Enter Name", command=lambda: _input_get(Name_Input, Saved_Name, Name_Error_TextVar,))

Name_Error = tk.Label(root, textvariable=Name_Error_TextVar,)

Name_Input.grid(column=0, row=0, padx=20, pady=(30, 5))
Save_Name.grid(column=1, row=0, padx=20, pady=(30, 5))
Name_Error.grid(column=0, row=1, padx=20, pady=(0, 30))

root.mainloop()