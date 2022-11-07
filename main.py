
import tkinter as tk
import random
import pyttsx3
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING
import webbrowser



def help():
    messagebox.askokcancel("Are You Sure Want to continue?", "Want to continue?")
    webbrowser.open('https://www.naturalreaders.com/online/support/help')
    
    




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


window = tk.Tk()
window.geometry("500x200")
window.title('random number generator')
randombutton=tk.Button(text='Generate',command=randomoutput)
randombutton.pack()
close = tk.Button(text='Close',command=close)
close.pack()
help = tk.Button(text='Help',command=help)
help.pack()
window.mainloop()
