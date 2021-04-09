import parser
from tkinter import *

root = Tk()
root.title("calculadora vulkano")

display=Entry(root)
display.grid(row=1, columnspan=6,sticky=W+E)

ind = 0

def obten_num(n):
    global ind
    display.insert(ind, n)
    ind+=1


def obten_op(operator):
    global ind
    opera_len = len(operator)
    display.insert(ind, operator)
    ind+=opera_len

def limpiar():
    display.delete(0, END)

def limp():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        limpiar()
        display.insert(0, display_new_state)
    else:
        limpiar()
        display.insert(0, "error")

def calcula():
    display_state = display.get()
    try:
        exmat = parser.expr(display_state).compile()
        resul= eval(exmat)
        limpiar()
        display.insert(0, resul)
    except Exception:
        limpiar()
        display.insert(0, "error")
    

#botones de numeros
Button(root, text="1", command=lambda:obten_num(1)).grid(row=2, column=0,sticky=W+E)
Button(root, text="2", command=lambda:obten_num(2)).grid(row=2, column=1,sticky=W+E)
Button(root, text="3", command=lambda:obten_num(3)).grid(row=2, column=2,sticky=W+E)

Button(root, text="4", command=lambda:obten_num(4)).grid(row=3, column=0,sticky=W+E)
Button(root, text="5", command=lambda:obten_num(5)).grid(row=3, column=1,sticky=W+E)
Button(root, text="6", command=lambda:obten_num(6)).grid(row=3, column=2,sticky=W+E)

Button(root, text="7", command=lambda:obten_num(7)).grid(row=4, column=0,sticky=W+E)
Button(root, text="8", command=lambda:obten_num(8)).grid(row=4, column=1,sticky=W+E)
Button(root, text="9", command=lambda:obten_num(9)).grid(row=4, column=2,sticky=W+E)



#botones de ayuda y operaciones

Button(root, text="AC", command=lambda:limpiar()).grid(row=5, column=0,sticky=W+E)
Button(root, text="0", command=lambda:obten_num(0)).grid(row=5, column=1,sticky=W+E)
Button(root, text="%", command=lambda: obten_op("%")).grid(row=5, column=2,sticky=W+E)

Button(root, text="+", command=lambda: obten_op("+")).grid(row=2, column=3,sticky=W+E)
Button(root, text="-", command=lambda: obten_op("-")).grid(row=3, column=3,sticky=W+E)
Button(root, text="*", command=lambda: obten_op("*")).grid(row=4, column=3,sticky=W+E)
Button(root, text="/", command=lambda: obten_op("/")).grid(row=5, column=3,sticky=W+E)

#botones de ayuda
Button(root, text="⤎", command=lambda:limp()).grid(row=2, column=4,sticky=W+E, columnspan = 2)
Button(root, text="exp", command=lambda: obten_op("**")).grid(row=3, column=4,sticky=W+E)
Button(root, text="^2", command=lambda: obten_op("**2")).grid(row=3, column=5,sticky=W+E)
Button(root, text="(", command=lambda: obten_op("(")).grid(row=4, column=4,sticky=W+E)
Button(root, text=")", command=lambda: obten_op(")")).grid(row=4, column=5,sticky=W+E)
Button(root, text="=", command=lambda:calcula()).grid(row=5, column=4,sticky=W+E, columnspan = 2)



root.mainloop()