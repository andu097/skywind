from tkinter import *
from tkinter import messagebox
import sys
import re

BACKGROUND_COLOR = "#B1DDC6"


# create the tkinter window with labels and buttons
w = Tk()
w.title("Calculator")
w.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


string_label = Label(text="Insert string:")
string_label.grid(row=1, column=0)

string_entry = Entry(width=25)
string_entry.grid(row=1, column=1)
string_entry.focus()

string = str(string_entry.get())




def Add():
    my_string = str(string_entry.get())
    suma = 0
    if my_string != None:
        #split text into delimiter part and part to be searched for numbers
        lines = my_string.split('\\n')
        if len(lines) > 1 :
            text = str(lines[1])
            if '[' in lines[0]:
                #format delimiter to extract only useful part in the split section popping the brackets and the //
                delimiter = re.findall(r'\[.*?\]' , lines[0])[0][1:-1]
            else :
                delimiter = lines[0][2:]
        else :
            delimiter = ','
            text = str(lines[0])
        #cast second part of the array to string
        
        #extract list of numbers
        numbers = text.split(delimiter)
        #add all numbers lower than 1000 and higher than 0
        for x in numbers:
            if int(x) < 1000 and int(x) > 0:
                suma = suma + int(x)
    messagebox.showinfo(title="Sum", message=f"Sum is: {suma}")


add_button = Button(width=36, text="Add", command=Add)
add_button.grid(row=4, column=1, columnspan=2)



w.mainloop()