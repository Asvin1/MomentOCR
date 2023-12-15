import tkinter as tk
from PIL import Image,ImageTk
import pyscreenshot as ImageGrab
import pyautogui
import pytesseract
import pyperclip
import io
import sys

if("win" in sys.platform):
    pytesseract.pytesseract.tesseract_cmd =r'D:\tess\tesseract' #Make sure to chnage the path to your tesseract executable
window = tk.Tk()

state=0
sx,sy=0,0

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    pop = tk.Label(popup, text=msg)
    pop.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = sys.exit)
    B1.pack()
    popup.mainloop()

def motion(event):
    global state
    x, y = event.x, event.y
    global label,sx,sy
    if(state==1):
        label.coords(rec,sx,sy,x,y)

def draw(e):
    global state
    if(state!=2):
        print(pyautogui.position().x,pyautogui.position().y)
        global label
        global sx,sy
        sx,sy=e.x,e.y
        label.delete("all")
        global rec
        rec=label.create_rectangle(e.x,e.y,e.x,e.y,fill='black')
        state=1


def fin(e):
    global state
    if(state!=2):
        state=2
        bbox = (sx, sy, e.x, e.y)
        pic=ImageGrab.grab(bbox=bbox)
        #pic.save('read.png')
        buffer = io.BytesIO()
        pic.save(buffer,format='png')
        try:
            pyperclip.copy(pytesseract.image_to_string(pic,config='--psm 6 --oem 1'))
        except:
            window.destroy()
            popupmsg("tesseract might not be installed on your system")
            
        window.destroy()


window.attributes('-fullscreen', True)
window.title("On Screen OCR")
window.configure(bg='grey')
window.wait_visibility(window)
window.attributes("-alpha", 0.5)
window.config(cursor="crosshair")
if("win" in sys.platform):
    window.attributes("-transparentcolor", "black")

label = tk.Canvas(window,background='grey',borderwidth=0,highlightthickness=0)
label.pack()


pic=ImageGrab.grab()
img=ImageTk.PhotoImage(pic)
print(img.width(),img.height())
window.geometry(str(img.width())+'x'+str(img.height())+"+0+0")
window.resizable(0, 0)

label.place(x=0,y=0,width=img.width(),height=img.height())

label.bind('<Motion>', motion)
label.bind('<Button-1>',draw)
label.bind('<ButtonRelease>',fin)

window.mainloop()

