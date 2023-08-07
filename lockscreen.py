from tkinter import *

root = Tk()
root.attributes('-fullscreen',True)
root.attributes('-topmost',True)
root.attributes('-disabled', True)
Label(root,text='Your screen limit has reached',font=('Segoe UI', '72')).pack()
