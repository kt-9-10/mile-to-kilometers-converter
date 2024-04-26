from tkinter import *


# Button function
def button_clicked():
    input_text = input_miles.get()
    try:
        input_num = float(input_text)
        result_num = round(input_num * 1.60934)
    except ValueError:
        result_num = "Error"

    result_label.config(text=f"{result_num}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

# Label
Question_label = Label(text="is equal to", font=("Segoe UI", 16))
Question_label.grid(column=0, row=1)

miles_label = Label(text="Miles", font=("Segoe UI", 16))
miles_label.grid(column=2, row=0)


km_label = Label(text="Km", font=("Segoe UI", 16))
km_label.grid(column=2, row=1)

result_label = Label(text="0", font=("Segoe UI", 16))
result_label.grid(column=1, row=1)

# Entry
input_miles = Entry(width=8, font=("Segoe UI", 16))
input_miles.grid(column=1, row=0)

# Button
button = Button(text="Calculate", font=("Segoe UI", 16), command=button_clicked)
button.grid(column=1, row=2)






window.mainloop()
