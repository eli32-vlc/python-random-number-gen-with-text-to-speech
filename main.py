
import tkinter as tk
import random
import pyttsx3
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING
import webbrowser



def help():
    messagebox.askokcancel("Are You Sure Want to continue?", "Want to continue?")
    #No Help There
    webbrowser.open('https://https://www.naturalreaders.com/online/')


def buy():
    #It a joke
    messagebox.askokcancel("Are You Sure Want To Buy?", "Are You Sure Want To Buy?")
    messagebox.showerror('Error','Error code 0x100029')
    messagebox.askretrycancel("Error", "Try again?")



def close():
    window.destroy()

def randomoutput():
    messagebox.askokcancel("Are You Sure Want to continue?", "Want to continue?,you have 3 credit left?")
    output = random.randint(0,1000000000)
    messagebox.showinfo('Output',"Your Random Number is %d" % output)
    engine = pyttsx3.init()
    engine.say("Your Random Number is %d" % output)
    engine.runAndWait()
    randomtext = tk.Label(text=output)
    randomtext.pack()
    print("Your Random Number is %d" % output)
    #prank
    window.destroy()
    messagebox.showerror('Error','Error code 0x10000964')
    messagebox.askretrycancel("Error", "Try again?")
    messagebox.askretrycancel("Python Crash", "Python Crash,Try again?")
    messagebox.showerror('Error','Error code 0x08400964')



window = tk.Tk()
window.geometry("500x200")
window.title('random generator')
randombutton=tk.Button(text='Generate',command=randomoutput)
randombutton.pack()
close = tk.Button(text='Close',command=close)
close.pack()
buy = tk.Button(text='Buy This software',command=buy)
buy.pack()
help = tk.Button(text='Help',command=help)
help.pack()
window.mainloop()
