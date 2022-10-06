from tkinter import *

expression = ''
equation = StringVar()

def press(num):
    global expression

    expression = expression + str(num)
    
    #update the expression
    equation.get(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)

        expression = ''

    except:
        print('alo')