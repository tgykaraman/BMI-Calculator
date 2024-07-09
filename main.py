from tkinter import *

window = Tk()
window.title("BMI App")
window.minsize(width=250, height=250)
window.config(padx=50, pady=50)

weightLabel = Label(text="Enter Your Weight (kg)", font=("Arial", 14, "normal"))
weightLabel.pack()
weightEntry = Entry(width=10)
weightEntry.pack()

heightLabel = Label(text="Enter Your Height (cm)", font=("Arial", 14, "normal"))
heightLabel.pack()
heightEntry = Entry(width=10)
heightEntry.pack()


def calculateBMI():
    try:
        h = float(heightEntry.get())
        w = int(weightEntry.get())
        bmi = round(w / (h * h), 2)
        if bmi < 18.5:
            result = "Your BMI is {}. You are Underweight!".format(bmi)
        elif 18.5 < bmi <= 24.9:
            result = f"Your BMI is {bmi}. You are Normal!"
        elif 25.0 < bmi <= 29.9:
            result = f"Your BMI is {bmi}. You are Overweight!"
        elif 30.0 < bmi <= 34.9:
            result = f"Your BMI is {bmi}. You are Class I obesity!"
        elif 35.0 < bmi <= 39.9:
            result = f"Your BMI is {bmi}. You are Class II obesity!"
        else:
            result = f"Your BMI is {bmi}. Your are Class III obesity!"
        resultLabel.config(text=result)
    except:
        resultLabel.config(text="Please enter valid numbers for height and weight!")


calculateButton = Button(text="Calculate", command=calculateBMI)
calculateButton.pack()

resultLabel = Label(text="",font=("Arial", 14, "normal"))
resultLabel.pack()

window.mainloop()
