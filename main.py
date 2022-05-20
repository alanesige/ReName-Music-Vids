import tkinter as esige
from tkinter import *
from tkinter import filedialog
from tkinter import font
from types import LambdaType
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import os
import argparse
import  tkinter.messagebox
from fileinput import filename
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from PyPDF2.pdf import ContentStream
from PyPDF4.generic import TextStringObject, NameObject
from PyPDF4.utils import b_
from pip import main

import os
import argparse
from fileinput import filename
import re

#novelty

root = esige.Tk()

canvas = esige.Canvas(root, width = 300, height = 400)
canvas.grid(columnspan=3, rowspan=7)

random_text3 = esige.Label(root, text='No folder selected.', foreground=[('black')], font=('calibri',10,'bold'))
random_text3.grid(columnspan=3, column=0, row=5)

def open_file():    
    file = filedialog.askdirectory()
    global txt
    global txtnoma
    
    txt=  str(file)
    txtnoma = txt.rsplit('/',1)[-1]
    #txtnomazaidi = txtnoma.rsplit('.',1)[-2]
    print(txtnoma)
    random_text3.config(text = txtnoma)

 
def open_files():    
        esige.messagebox.showinfo("File Rename","Feature coming soon.")


def awesome():
     print(txt)
     for foldername, dirs, filenames in os.walk(txt):
            for filename in filenames:

                Video_File = os.path.join(txt, filename)
                print(Video_File)
                new_filename = newfilename = re.sub("FHR|1080p|y2mate\.com - |audio|youtube|official|music|video|\(|\)|\[|\]|\,|\/|\\|_|lyric|SMS|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
                print(new_filename)
                os.rename(os.path.join(txt,filename), os.path.join(txt,new_filename))
     esige.messagebox.showinfo("Renaming Completed.")           



    
browse_text = esige.StringVar()

browse_btn = esige.Button(
             
             root,
             textvariable=browse_text,
             command=lambda:open_files(),
             height=2,
             width=15,background=[('grey')],font=('calibri',10,'bold'),foreground=[('brown')],
             
             )
browse_text.set("File Select")
browse_btn.grid(column=1, row=1)

browse_texty = esige.StringVar()
browse_btny = esige.Button(
             
             root,
             textvariable=browse_texty,
             command=lambda:open_file(),
             height=2,
             width=15,background=[('grey')],font=('calibri',10,'bold'),foreground=[('brown')],
             
             
             )
browse_texty.set("Folder Select")
browse_btny.grid(column=1, row=2)


random_text2 = esige.Label(root, text="Proceed",foreground=[('navyblue')])
random_text2.grid(columnspan=3, column=0, row=3)



watermark_text = esige.StringVar()
watermark_text.set("Rename")
watermark_btn = esige.Button(root, textvariable=watermark_text,bg='darkgrey',
                          
   command=lambda:  awesome()                                  
                                 , height=2, width=15,font=('calibri',13,'bold'),foreground=[('white')],background=[('green')],
                                    activebackground=[('white')], activeforeground=[('green')],
                                    
   
   )

watermark_btn.grid(column=1, row=4)

#clear button


clear_text = esige.StringVar()
clear_text.set("Clear")
clear_btn = esige.Button(root, textvariable=clear_text,bg='darkgrey',
     height=1, width=6,font=('calibri',10,'bold'),foreground=[('black')],background=[('grey')],
                                    activebackground=[('white')], activeforeground=[('green')],
                                    command=lambda:clear()
   
   )

clear_btn.grid(column=1,row=6)
#clear function

def clear():
    random_text3.config(text = '')
   

root.mainloop()
