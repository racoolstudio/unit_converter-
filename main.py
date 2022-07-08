from tkinter import *

my_screen = Tk()
my_screen.minsize(100, 100)
my_screen.title('Unit Converter')
my_screen.config(bg='black', pady=20, padx=20)
user_input = Entry()
user_input.insert(END, 'Enter Any Number')
user_input.config(width=13)
user_input.grid(column=1, row=1)
equal_label = Label(text='is equal to')
equal_label.config(bg='black', fg='white', width=10)
equal_label.config(pady=10)
equal_label.grid(column=0, row=2)

meter_label = Label(text='Meter')
meter_label.config(bg='black', fg='white', width=10)
meter_label.grid(column=3, row=1)
result_label = Label(text='0')
result_label.config(bg='white', fg='black', width=13)
result_label.grid(column=1, row=2)
foot_label = Label(text='foot/feet')
foot_label.config(bg='black', fg='white', width=10, pady=10)
foot_label.grid(row=2, column=3)


def from_meter_to_feet():
    num = float(user_input.get())
    result = round(num * 3.28084,2)

    return result_label.config(text=f'{result }')


button = Button(text='Calculate', command= from_meter_to_feet,)
button.grid(column=1, row=5)
my_screen.mainloop()
