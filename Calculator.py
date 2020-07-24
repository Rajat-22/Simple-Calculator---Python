
# First import all from tkinter

from tkinter import*


# Here I define the working of button click

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


# Here I define the working of button Display

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")


# Here I define the working of button Equals

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""


# Here I define the title and where the value store

cal = Tk()
cal.title("Calculator -By Rajat")
operator =""
text_Input = StringVar()


# What the screen of the calculator shows is defined here

txtDisplay = Entry(cal , font=('arial' , 20 , 'bold'),
                   textvariable = text_Input , bd=30 , insertwidth=4 , bg="sky blue", justify='right').grid(columnspan=4)


# Here is the code for First row of the calculator.

btn1=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="1", bg="sky blue" , command=lambda:btnClick(1)).grid(row=1, column=0)
btn2=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="2", bg="sky blue" , command=lambda:btnClick(2)).grid(row=1, column=1)
btn3=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="3", bg="sky blue" , command=lambda:btnClick(3)).grid(row=1, column=2)
Add=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="+", bg="sky blue" , command=lambda:btnClick("+")).grid(row=1, column=3)


# Code for second row of the calculator.

btn4=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="4", bg="sky blue" , command=lambda:btnClick(4)).grid(row=2, column=0)
btn5=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="5", bg="sky blue" , command=lambda:btnClick(5)).grid(row=2, column=1)
btn6=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="6", bg="sky blue" , command=lambda:btnClick(6)).grid(row=2, column=2)
Sub=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="-", bg="sky blue" , command=lambda:btnClick("-")).grid(row=2, column=3)


# Code for third row of the calculator.

btn7=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="7", bg="sky blue" , command=lambda:btnClick(7)).grid(row=3, column=0)
btn8=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="8", bg="sky blue" , command=lambda:btnClick(8) ).grid(row=3, column=1)
btn9=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="9", bg="sky blue" , command=lambda:btnClick(9)).grid(row=3, column=2)
Mul=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="*", bg="sky blue" , command=lambda:btnClick("*")).grid(row=3, column=3)


# Code for Fourth row of the calculator.

clear=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="C", bg="sky blue" , command=btnClearDisplay ).grid(row=4, column=0)
btn0=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="0", bg="sky blue" , command=lambda:btnClick(0)).grid(row=4, column=1)
Result=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="=", bg="sky blue" , command=btnEqualsInput ).grid(row=4, column=2)
Div=Button(cal , padx=16 , bd=8 , fg="black" ,font=('arial', 20 , 'bold'), text="/", bg="sky blue" , command=lambda:btnClick("/")).grid(row=4, column=3)


# The last line and main line where the hole code runs.

cal.mainloop()







