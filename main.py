import tkinter as esige
from tkinter import *
from tkinter import filedialog
from tkinter import font
from types import LambdaType
from tkinter.filedialog import askopenfile
import os
import argparse
from fileinput import filename
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

                if filename.endswith('.mkv'):
                  # continue

                  Video_File = os.path.join(txt, filename)
                

               
                  new_filenames = re.sub("\.mkv|FHR|1080p|for skiza tune|FOR SKIZA TO 811|dial|send skiza|skiza|811|ixtendz|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
                  new_filename = re.sub("(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)
                  new_filename = re.sub("(\-)$","",new_filename, flags=re.IGNORECASE)
                  new_filenamer = re.sub("(\_)"," ",new_filename, flags=re.IGNORECASE)
                  new_filenamerz = re.sub("- -","-",new_filenamer, flags=re.IGNORECASE)
                  new_filenamer = re.sub("\--","\-",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamers = re.sub("(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)
                
                  testing = os.path.join(txt,new_filenamers+'.mkv')
                  if os.path.exists(testing):
                      swag = os.path.join(txt,new_filenamers+' v2 '+'.mkv')
                      drake = os.rename(os.path.join(txt,filename), testing)
                     #print('file already exist')
                  else:
                    drake = os.rename(os.path.join(txt,filename), testing)
                    print('mkv')
                
                elif filename.endswith('.mp4'):
                  # continue

                  Video_File = os.path.join(txt, filename)
                

               
                  new_filenames = re.sub("\.mp4|FHR|1080p|for skiza tune|FOR SKIZA TO 811|dial|send skiza|skiza|811|ixtendz|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
                  new_filename = re.sub("(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)
                  new_filename = re.sub("(\-)$","",new_filename, flags=re.IGNORECASE)
                  new_filenamer = re.sub("(\_)"," ",new_filename, flags=re.IGNORECASE)
                  new_filenamerz = re.sub("- -","-",new_filenamer, flags=re.IGNORECASE)
                  new_filenamer = re.sub("\--","\-",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamers = re.sub("(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)
                
                  testing = os.path.join(txt,new_filenamers+'.mp4')
                  if os.path.exists(testing):
                      swag = os.path.join(txt,new_filenamers+' v2 '+'.mp4')
                      drake = os.rename(os.path.join(txt,filename), testing)
                     #print('file already exist')
                  else:
                    drake = os.rename(os.path.join(txt,filename), testing)
                    print('mp4')



                elif filename.endswith('.mp3'):
                  # continue

                  Video_File = os.path.join(txt, filename)
                

               
                  new_filenames = re.sub("\.mp3|FHR|1080p|for skiza tune|FOR SKIZA TO 811|dial|send skiza|skiza|811|ixtendz|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
                  new_filename = re.sub("(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)
                  new_filename = re.sub("(\-)$","",new_filename, flags=re.IGNORECASE)
                  new_filenamer = re.sub("(\_)"," ",new_filename, flags=re.IGNORECASE)
                  new_filenamerz = re.sub("- -","-",new_filenamer, flags=re.IGNORECASE)
                  new_filenamer = re.sub("\--","\-",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamers = re.sub("(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)
                
                  testing = os.path.join(txt,new_filenamers+'.mp3')
                  if os.path.exists(testing):
                      swag = os.path.join(txt,new_filenamers+' v2 '+'.mp3')
                      drake = os.rename(os.path.join(txt,filename), testing)
                     #print('file already exist')
                  else:
                    drake = os.rename(os.path.join(txt,filename), testing)
                    print('mp3')

                else:
                    continue
     #esige.messagebox.showinfo("Hurray!","Renaming Completed.")

    
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
