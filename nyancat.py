from threading import Thread
from tkinter import *

from playsound import *


def play():
    while True:
        playsound("rsrc/cat.mp3")

soundthread = Thread(target=play)
soundthread.start()
# from PIL import Image, ImageTk
root = Tk()
# canvas = Canvas(root, width=500, height=500)
root["bg"] = "gray0"
c=Canvas(root,width=250,height=250, bd=0, highlightthickness=0)
c.pack()
yourcomputerhasbeeentrashed=Label(root,font='Times 30')
yourcomputerhasbeeentrashed.pack()
yourcomputerhasbeeentrashed.configure(text='your computer has been trashed by the memz trojan. Now enjoy the nyan cat.')
c['bg']='gray0'
trashed=Label(root)
labelcat = Label(root)
label=Label(root)
label.pack()
class Nyan:
    def __init__(self, nyanimg):
        root.attributes('-fullscreen', True)
        # canvas.pack()

        frameCnt = 12
        frames = [PhotoImage(file=nyanimg, format='gif -index %i' % (i)) for i in range(frameCnt)]

        def update(ind):
            frame = frames[ind]
            ind += 1
            if ind == frameCnt:
                ind = 0
            labelcat.configure(image=frame)
            root.after(100, update, ind)

        labelcat['bg'] = "gray0"
        labelcat.pack()
        root.after(0, update, 0)
        root.mainloop()
        label.configure(image='rainbow_up.gif')
        self.rainbow(True)
        # winsound.PlaySound('rsrc/nyan.mp3', winsound.SND_ALIAS | winsound.SND_ASYNC)
    def rainbow(self,up):
        #if up:
        label.configure(image='rainbow_up.gif')

class Nyan1:
    def __init__(self, nyanimg):
        label1 = Label(root)
        root.attributes('-fullscreen', True)
        # canvas.pack()

        frameCnt = 12
        frames = [PhotoImage(file=nyanimg, format='gif -index %i' % (i)) for i in range(frameCnt)]

        def update(ind):
            frame = frames[ind]
            ind += 1
            if ind == frameCnt:
                ind = 0
            label1.configure(image=frame)
            root.after(100, update, ind)

        label1['bg'] = "gray0"
        label1.pack()
        root.after(0, update, 0)
        root.mainloop()
        self.rainbow(True)
    def rainbow(self,up):
        if up:
            label.configure(image='rainbow_up.gif')

def orig():
    Nyan('rsrc/original.gif')


def cust():
    Nyan1('rsrc/original.gif')


root.title('Google Chrome')
while True:
    root.protocol('WM_DELETE_WINDOW', cust)
    Nyan1('rsrc/original.gif')
