
# advance function
# allowing any number of agrument /args
# unlimited positional number of input
def add(b,*args):
    number = sum([n for n in args])
    print(number)
    print(b)


add(3, 2, 3)
# optional  unlmited kwargs/ keywords argument
# it turns it to dictionary
# recall getting values from a dictionary e.g dic['name']
# if the name key does not exist it would return an error but if you use dic.get('name')
# it would return None which is better !!!
def calculate(**kwargs):
    print(kwargs['add'])
    print(kwargs.get('multiply'))
calculate(add = 2 )
from tkinter import *

window = Tk()
window.title('My first GUI')
window.minsize(500, 500)
# label
my_first_label = Label(text='Nothing Happened Yet', font=('Arial', 20), fg='blue', )
my_first_label.pack()
# you can access the properties like bg,fg,text using
# my_first_label['text'] = 'yoo
# my_first_label.config(bg = 'white') this is tuple so you can pass in as many variable as it contains
my_first_label['bg'] = 'pink'
# Entry Component
my_entry = Entry(width=10, bg='white', fg='black', )
# to get the value from my_entry we use the get method
# adding a placeholder to entry we use my_entry.insert(END,'then what ever')
my_entry.insert(END, 'then what ever')


# adding spinBOx

def spin():
    print(spinBox.get())


spinBox = Spinbox(from_=0, to=30, command=spin)


# adding scale
def scale():
    print(scale.get())


spinBox.pack()

scaler = Scale(from_=0, to=10, width=5, command=scale)
scaler.pack()
my_entry.pack()


# button
def button_clicked():
    my_first_label.configure(text=my_entry.get())


button = Button(text='click me oo', command=button_clicked)
button.pack()
# Text Entry Box
my_first_text = Text(height=5, width=30)
my_first_text.insert(END, 'Multiple Line Text Box')
# put the cursor in text box
my_first_text.focus()
# to get the value
# 1.0 means get the first line of the text starting from index 0
# which you can play with

my_first_text.pack()


# add check box
def check_box():
    print(check_state.get())


check_state = IntVar()
checkbox = Checkbutton(text='I agree', variable=check_state, command=check_box)
checkbox.pack()


# adding radio button
def radio_button_clicked():
    print(radio_state.get())


radio_state = IntVar()
radio_button = Radiobutton(variable=radio_state, value=1, text='option 1', command=radio_button_clicked)
radio_button2 = Radiobutton(variable=radio_state, value=2, text='option 2', command=radio_button_clicked)
radio_button.pack()
radio_button2.pack()
# adding list button
def list_used(event):
    print(list_button.get(list_button.curselection()))
list_button = Listbox(height=4)
box = [2, 3, 1, 4]
for i in box:
    list_button.insert(box.index(i), i)
list_button.bind('<<ListboxSelect>>',list_used)
list_button.pack()
window.mainloop()
from tkinter import *

screen = Tk()
screen.title('Unit Converter')
screen.minsize(width=200, height=200)
# adding padding
screen.config(padx=50, pady=50)
# pack,place,grid (Layout manager)
# label = Label(text = 'label')
# label.place(x=50,y=0)

label2 = Label(text='yoouu')
label2.grid(column=1, row=1)
label2.config(pady=10, padx=10)
button = Button(text='Click me !')
button.config(pady=20)
button.grid(row=2, column=2)

button_2 = Button(text='newbie')
button_2.grid(row=1, column=3)
input1 = Entry()
input1.insert(END, 'Type somthing')
input1.grid(row=5, column=5)


def from_used(event):
    print(from_button.get(from_button.curselection()))


# def to_used(event):
#     print(to_button.get(to_button.curselection()))


from_button = Listbox(height=5)

from_unit = ['Kilometer', 'Mile', 'Meter', 'Foot', 'Yard']
for i in from_unit:
    from_button.insert(from_unit.index(i), i)
from_button.bind('<<ListboxSelect>>', from_used)
from_button.grid(row=6, column=1)
to_unit = ['Meter', 'Feet', 'Yard', 'Kilometer', 'Mile']

# to_button = Listbox(height=5)
# for i in to_unit:
#     to_button.insert(to_unit.index(i), i)
# to_button.bind('<<ListboxSelect>>', to_used)
# to_button.grid(row=6, column=4)
# dont use grid and pack


screen.mainloop()

