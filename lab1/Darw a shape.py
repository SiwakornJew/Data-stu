import tkinter as tk
def show_output():
    number=int(number_in.get())
    output = ''
    for i in range(1,13):
        output += str(number)+ ' x ' +str(i)
        output += ' = ' +str(number*i) +' \n'
        output_label.configure(text=output)


window =tk.Tk()
window.title('Python')
window.minsize(width=500,height=500)

title=tk.Label(master=window, text='Multiplication Table')

title.pack()

number_in =tk.Entry(master=window)
number_in.pack()

go_button =tk.Button(
    master=window, text='therefor',
    command=show_output
    )
go_button.pack()

output_label =tk.Label(master=window)
output_label.pack()




window.mainloop()