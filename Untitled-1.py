from tkinter import *
value = 1
def change_value():
       global value
       value -= 1
       if value == 0:
                 print("button pressed")
                 value = 1
       else:
                pass    
tk = Tk()
btn = Button(tk, text="your_text", command=change_value)
btn.pack()
