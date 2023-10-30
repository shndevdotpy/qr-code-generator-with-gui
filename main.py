import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import ImageTk, Image  
from typing import MappingView
import qrcode,os,uuid
from qrcode import constants

gui = tk.Tk()

gui.title('QR Generator')
gui.geometry("300x210")


label1=tk.Label(text='Content:')
label2=tk.Label(text='Inner color:')
label3=tk.Label(text='Outer color:')
empty=tk.Label(text='')


textBox = tk.Text(gui, height = 3, width = 300)

def getLink(): 
    link = textBox.get(1.0, "end-1c") 
    print(link)
    innercolor = comboBox.get()
    outercolor = comboBox2.get()
    if (innercolor == outercolor or outercolor == innercolor):
        tk.messagebox.showinfo(title="Error", message="Inner and outer color cannot be the same!")
    elif (innercolor == "" or outercolor == ""):
        tk.messagebox.showinfo(title="Error", message="Please select inner and outer colors.")
    elif (link == ""):
        tk.messagebox.showinfo(title="Error", message="The content can't be empty.")
    else:
        filenamegenerator = str(uuid.uuid4())

        code = qrcode.QRCode(version=1, error_correction=constants.ERROR_CORRECT_L, box_size=40, border=1)

        code.add_data(link)

        code.make(fit=True)

        image = code.make_image(fill_color=innercolor,back_color=outercolor)

        image.save (os.path.join('C:\\Users\\',os.getlogin(),'Desktop','qr_' + filenamegenerator +'.png'))
        tk.messagebox.showinfo(title="Success!", message="The QR code is saved on your desktop.")

printButton = tk.Button(gui, text = "Save to Desktop", command = getLink)


comboBox = ttk.Combobox(gui, values=["Red", "Yellow", "Blue", "Purple", "Pink", "Orange", "Green", "Black", "White"])
#red/yellow/blue/purple/pink/orange/green/black/white
def inner_selected(event):
   selected_option = comboBox.get()
   print("Inner color selected:", selected_option)
comboBox.bind("<<ComboboxSelected>>", inner_selected)

comboBox2 = ttk.Combobox(gui, values=["Red", "Yellow", "Blue", "Purple", "Pink", "Orange", "Green", "Black", "White"])
def outer_selected(event):
   selected_option = comboBox2.get()
   print("Outer color selected:", selected_option)
comboBox2.bind("<<ComboboxSelected>>", outer_selected)


label1.pack()
textBox.pack()
label2.pack()
comboBox.pack()
label3.pack()
comboBox2.pack()
empty.pack()
printButton.pack() 
gui.mainloop()
