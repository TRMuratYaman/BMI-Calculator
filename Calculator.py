from tkinter import *


window = Tk()
window.minsize(width=250, height=250)
window.title("IBM Calculator")
window.config(padx=30, pady=30)

weight = Label(text="Enter Your Weight (kg)", fg="black")
weight.config(padx=10, pady=10)
weight.pack()

weight_entry = Entry(width=20)
weight_entry.pack()

height = Label(text="Enter Your Height (cm)", fg="black")
height.config(padx=10, pady=10)
height.pack()

height_entry = Entry(width=20)
height_entry.pack()

def calculatebmi():
    x, y = weight_entry.get(), height_entry.get()
    if (x == "") | (y == ""):
        result.config(text="Enter Both Weight and Height values")

    else:
        try:
            x, y = float(weight_entry.get()), float(height_entry.get()) / 100
            bmi = x / (y * y)
            result_message = show_result(bmi)
            result.config(text=result_message)
        except:
            result.config(text="Please enter valid inputs ! ")


def show_result(bmi):
    result_string = f"Your BMI is {bmi:.1f}.You are"
    if bmi > 16.0:
        result_string += "severely underweight."
    elif (bmi > 16.0) & (bmi <= 18.4):
        result_string += "underweight."
    elif (bmi > 18.5) & (bmi <= 24.9):
        result_string += "Normal."
    elif (bmi > 25.0) & (bmi <= 29.9):
        result_string += "overweight."
    elif (bmi > 30) & (bmi <= 34.9):
        result_string += "moderately obese."
    elif (bmi > 35) & (bmi <= 39.9):
        result_string += "severely obese ."
    elif (bmi >= 40):
        result_string += "morbidly obese."

    return result_string


calculate_button = Button(text="Calculate", bg="white", fg="black", command=calculatebmi)
calculate_button.pack()

result = Label(text="")
result.config(padx=20, pady=10)
result.pack()



window.mainloop()