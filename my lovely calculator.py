from tkinter import *
from functools import partial

root = Tk()

root.geometry("200x235")
root.title("Calculator")

standby = True
edited = False
Continue = False

lastResult = ""
lastEquation = ""

lbl = Label(root, text="0", bg="white", width=50, height=2)
lbl.pack()

signs = ["÷", "×", "-", "+"]
replace_signs = {"÷": "/", "×": "*"}


def calculate(equation):
    for key, val in replace_signs.items():
        equation = equation.replace(key, val)

    return eval(equation)


def getLast(equation):
    for sign in signs:
        equation = equation.replace(sign, "," + sign)

    sepEquaList = equation.split(",")

    return sepEquaList[len(sepEquaList) - 1]


def onClick(text):
    global standby
    global lastResult
    global lastEquation
    global Continue

    if standby:
        if str(text) == "=" and lbl.cget("text") == "0":
            return

        if str(text) in signs:
            Continue = True
        else:
            if not Continue:
                lbl.config(text="")
                standby = False
        # edited = True

    if str(text) == "=":
        Continue = False
        standby = True

        try:
            equation = lbl.cget("text")
            result = calculate(equation)

            lbl.config(text=result)

            lastEquation = equation
            lastResult = result
        except:
            try:
                print(lastResult)
                print(lastEquation)

                result = calculate(str(lastResult) + str(getLast(lastEquation)))

                lbl.config(text=result)

                lastResult = result
            except Exception as err:
                print(str(err))
                lbl.config(text="Error")
    elif str(text) == "🗑":
        Continue = False
        standby = True

        lastResult = ""
        lastEquation = ""

        lbl.config(text="0")
    else:
        lbl.config(text=str(lbl.cget("text")) + str(text))


def newButton(text, x, y, w=0):
    return Button(root, text=text, width=w, command=partial(onClick, text)).place(
        x=x, y=y
    )


def newButtonRow(texts, row):
    if len(texts) > 2:
        for index, text in enumerate(texts):
            newButton(
                text,
                ((10 + ((index + 1) * 40)) - 40)
                + (0 if index + 1 != len(texts) else 10),
                (45 + (row * 30)) - 30,
            )
    else:
        for index, text in enumerate(texts):
            newButton(
                text,
                (10 + ((index + 1) * 130)) - 130,
                (45 + (row * 30)) - 30,
                10 if index == 0 else 0,
            )


newButtonRow([7, 8, 9, "÷"], 1)
newButtonRow([4, 5, 6, "×"], 2)
newButtonRow([1, 2, 3, "-"], 3)
newButtonRow([0, "+"], 4)
newButtonRow(["=", "🗑"], 5)

root.mainloop()
