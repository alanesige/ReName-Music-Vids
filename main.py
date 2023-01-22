import tkinter as esige
from tkinter import *
from tkinter import filedialog
from tkinter import font
from types import LambdaType
from tkinter.filedialog import askopenfile
import os
from fileinput import filename
import os
from fileinput import filename
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from tqdm import tqdm

root = esige.Tk()
canvas = esige.Canvas(root, width = 300, height = 400)
canvas.grid(columnspan=3, rowspan=7)
random_text3 = esige.Label(root, text='No folder selected.', foreground=[('black')], font=('calibri',10,'bold'))
random_text3.grid(columnspan=3, column=0, row=5)

def get_sporty_nigga(new_filenamers):
            #print("Name Finder Launched...")
            try:

                        cid = ''
                        secret = ''
                        #Authentication - without user

                        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='',
                                                                    client_secret='',
                                                                    redirect_uri="http://localhost:8888/callback")) 

                        song = new_filenamers

                        results = sp.search(q=song, limit=1, type='track')
                        #Track Details
                        name = results['tracks']['items'][0]['name']
                        album = results['tracks']['items'][0]['album']['name']
                        artist_name = results['tracks']['items'][0]['artists'][0]['name']
                        feaured_artists = results['tracks']['items'][0]['artists'][0]['name']

                        the_feaures = []
                        #features = results['tracks']['items'][0]
                        count = 0
                        try:
                         while True:
                            next_guy = results['tracks']['items'][0]['artists'][count]['name']
                            the_feaures.append(next_guy)
                            count += 1
                            pass

                        except:
                            pass

                        all_artist = ','.join(the_feaures)
                        global new_name
                        new_name = name+" - "+all_artist
                        #confirm match percentage
                        listname = new_filenamers.split()
                        list_len = len(listname)
                        list_count = 0
                        truest = 0

                        try:
                            while True:            
                               list_value = listname[list_count]
                               list_match = re.search(list_value,new_name,flags=re.IGNORECASE)
                               list_count += 1
                               if list_match:
                                   truest+=1
                               else:
                                  print("Percentages Compromised!")
                                  pass
                               continue       
                        except:
                             pass

                        total_percentage = (truest/list_len)*100
                        print(total_percentage)
                        if total_percentage > 50:
                            new_name = re.sub(r"\/|\\|\?|\*|\<|\>|\||\:","",new_name, flags=re.IGNORECASE)
                            match = re.search(artist_name,new_filenamers,flags=re.IGNORECASE)
                            if match:
                               thee_name = new_name
                            else:
                               thee_name = new_filenamers
                        else:
                           thee_name = new_filenamers
                        #end of percent
                        print("the new name is "+thee_name)
                        return thee_name

            except:
                print("song not found")
                return new_filenamers
                pass

"""
end of spotify shenanigans
"""
def open_file():    
    file = filedialog.askdirectory()
    global txt
    global txtnoma    
    
    txt=  str(file)
    print("the string at the begining "+txt)
    txtnoma = txt.rsplit('/',1)[-1]
    #txtnomazaidi = txtnoma.rsplit('.',1)[-2]
    print(txtnoma)
    random_text3.config(text = txtnoma)
 
def open_files():    
        file = filedialog.askopenfile(title="Select Media file")
        global txt
        global txtnoma
        txt=  str(file.name)
        txtnoma = txt.rsplit('/',1)[-1]
        #txtnomazaidi = txtnoma.rsplit('.',1)[-2]
        print(txtnoma)
        random_text3.config(text = txtnoma)
        #esige.messagebox.showinfo("File Rename","Feature coming soon.")
def awesome():
    print(txt)
    if(os.path.isdir(txt)):
       print("Okay, is folder")
    #try:
       for foldername, dirs, filenames in os.walk(txt):
              
          for filename in filenames:
               #if os.path.isfile(filename):
             shrimp(filename)
             
          continue 
    #except:
    elif(os.path.isfile(txt)):
       txt1 = txt.rsplit('/',1)[-1]
       txt2 = "/"+txt1
       global txt3
       txt3 = txt.replace(txt2,"")
       print(f"the folder is {txt3} and the filename is {txt1}")
       for foldername, dirs, filenames in os.walk(txt3):
          for filename in filenames:
               if str(filename) == str(txt1):
                 print("working")
                 shrimps(filename)
                 #esige.messagebox.showinfo("File Rename","Rename Complete.")
                 break
          
    #except:
 
    else:
        print("Not file nor dir")
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
def shrimp(filename):
    if filename.endswith('.mkv'):
                  # continue
              Video_File = os.path.join(txt, filename)             
              new_filenames = re.sub("\.mkv|\[SPOTIFY\-DOWNLOADER\.COM\]|clip|ATL ViDz|ATL ViDz|\#|ItsNambaNanneTV|ItsNambaNnaneTV|prod. Dj Nephas|DIR_@TONY_DE_GIGZ|PROD by DJ NEPHAS|iXtendz|The Decimators|DIR-VIKTA DANIELS|Nakuru All Stars|Oolisikia Wapi|dj mistanewa|Dr@viktadaniel|BAETUESDAY|KENYAN VERSION|Dir. by @_Tony De Gigz_|dirby@qvsual|prod by Magix Enga|Xmix|Mad House Sounds|@elanimuziki    to|@elanimuziki|\@MR MIMS 254|Iphone x  Edit|greatlakesmix.com|Lovechild Records|Long Version|short Version|INTRODUCING VARIOUS NEW ARTISTES|CLUB VERSiON|RED ACAPELLA|Visuals|JACK JACK ON THE|ItsNambaNaneTV|or   to|Main Switch|send to|2018|dance crew|\{|\}|JustLife.com|(SongsLover.com)|SongsLover.com|YouTube|Directed by @QuadDub|REFORMAT|5B   5D|unofficial|V2|h264|FHR|full video|hq|1080p|for skiza tune|FOR SKIZA TO 811|0fficial|Song|dial|send skiza|skiza|811|ixtendz|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
              new_filename = re.sub(r"(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)

              new_filename = re.sub(r"(\-)$","",new_filename, flags=re.IGNORECASE)
              new_filenamer = re.sub(r"(\_)"," ",new_filename, flags=re.IGNORECASE)
              new_filenamerz = re.sub(r"- -","-",new_filenamer, flags=re.IGNORECASE)
              new_filenamer = re.sub(r"\--","\-",new_filenamerz, flags=re.IGNORECASE)
              new_filenamer = re.sub(r"\---","\***",new_filenamerz, flags=re.IGNORECASE)
              new_filenamers = re.sub(r"(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)  
              #print("before spoty shit "+ new_filenamers)
              new_filenamers = get_sporty_nigga(new_filenamers)
              
              print(txt)
              testing = os.path.join(txt,new_filenamers+'.mkv')
              if os.path.exists(testing):
                      swag = os.path.join(txt,new_filenamers+' '+'.mkv')
                      drake = os.rename(os.path.join(txt,filename), swag)
                      #print(testing)
              else:
                     drake = os.rename(os.path.join(txt,filename), testing)
                     #print(testing)
    elif filename.endswith('.MKV'):
                  # continue
                  Video_File = os.path.join(txt, filename)               
                  new_filenames = re.sub("\.MKV|\[SPOTIFY\-DOWNLOADER\.COM\]|clip|(SongsLover.com)|ATL ViDz|ItsNambaNanneTV|ItsNambaNnaneTV|prod. Dj Nephas|DIR_@TONY_DE_GIGZ|PROD by DJ NEPHAS|iXtendz|The Decimators|DIR-VIKTA DANIELS|Nakuru All Stars|Oolisikia Wapi|dj mistanewa|Dr@viktadaniel|BAETUESDAY|KENYAN VERSION|Dir. by @_Tony De Gigz_|dirby@qvsual|ATL ViDz|\#|prod by Magix Enga|Xmix|Mad House Sounds|@elanimuziki    to|@elanimuziki|\@MR MIMS 254|Iphone x  Edit|greatlakesmix.com|Lovechild Records|Long Version|short Version|INTRODUCING VARIOUS NEW ARTISTES|CLUB VERSiON|RED ACAPELLA|Visuals|JACK JACK ON THE|ItsNambaNaneTV|or   to|Main Switch|send to|2018|dance crew|\{|\}|JustLife.com|SongsLover.com|YouTube|Directed by @QuadDub|REFORMAT|5B   5D|unofficial|V2|h264|FHR|full video|hq|1080p|for skiza tune|FOR SKIZA TO 811|0fficial|Song|dial|send skiza|skiza|811|ixtendz|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
                  new_filename = re.sub(r"(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)

                  new_filename = re.sub(r"(\-)$","",new_filename, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"(\_)"," ",new_filename, flags=re.IGNORECASE)
                  new_filenamerz = re.sub(r"- -","-",new_filenamer, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\--","\-",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\---","\***",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamers = re.sub(r"(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)

                  #print("before spoty shit "+ new_filenamers)  

                  new_filenamers = get_sporty_nigga(new_filenamers)
                  print(txt)
                                
                  testing = os.path.join(txt,new_filenamers+'.MKV')
                  if os.path.exists(testing):
                      swag = os.path.join(txt,new_filenamers+' '+'.MKV')
                      drake = os.rename(os.path.join(txt,filename), swag)
                      #print(testing)
                  else:
                    drake = os.rename(os.path.join(txt,filename), testing)
                    #print(testing)
                
    elif filename.endswith('.mp4'):
                  # continue
                  Video_File = os.path.join(txt, filename)               
                  # continue
                  #print('Tis mp4')
                  Video_File = os.path.join(txt, filename)              
                  new_filenames = re.sub("\.mp4|YouTube|\[SPOTIFY\-DOWNLOADER\.COM\]|New Plus DOWNLOAD|download|clip|(SongsLover.com)|ATL ViDz|ATL ViDz|\#|prod by Magix Enga|Xmix|Mad House Sounds|@elanimuziki    to|@elanimuziki|\@MR MIMS 254|Iphone x  Edit|ItsNambaNanneTV|ItsNambaNnaneTV|prod. Dj Nephas|DIR_@TONY_DE_GIGZ|PROD by DJ NEPHAS|iXtendz|The Decimators|DIR-VIKTA DANIELS|Nakuru All Stars|Oolisikia Wapi|dj mistanewa|Dr@viktadaniel|BAETUESDAY|KENYAN VERSION|Dir. by @_Tony De Gigz_|dirby@qvsual|greatlakesmix.com|Lovechild Records|Long Version|short Version|INTRODUCING VARIOUS NEW ARTISTES|CLUB VERSiON|RED ACAPELLA|Visuals|JACK JACK ON THE|ItsNambaNaneTV|or   to|Main Switch|send to|2018|dance crew|\{|\}|JustLife.com|SongsLover.com|Directed by @QuadDub|REFORMAT|5B   5D|unofficial|V2|FHR|1080p|full video|hq|h264|for skiza tune|FOR SKIZA TO 811|dial|0fficial|Song|send skiza|skiza|811|ixtendz|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
                  new_filename = re.sub(r"(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)

                  new_filename = re.sub(r"(\-)$","",new_filename, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"(\_)"," ",new_filename, flags=re.IGNORECASE)
                  new_filenamerz = re.sub(r"- -","-",new_filenamer, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\--","\-",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\---","\***",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamers = re.sub(r"(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)

                  #print("before spoty shit "+ new_filenamers)

                  new_filenamers = get_sporty_nigga(new_filenamers)
                  
                  testing = os.path.join(txt,new_filenamers+'.mp4')
                 
                  if os.path.exists(testing):
                      swag = os.path.join(txt,new_filenamers+' '+'.mp4')
                      drake = os.rename(os.path.join(txt,filename), swag)
                      #print(testing)
                  else:
                    mana = os.path.join(txt,filename)
                    drake = os.rename(mana, testing)
                    #print(testing)
    elif filename.endswith('.MP4'):
                  # continue
                  Video_File = os.path.join(txt, filename)              
                  new_filenames = re.sub("\.MP4|YouTube|\[SPOTIFY\-DOWNLOADER\.COM\]|clip|New Plus DOWNLOAD|download|(SongsLover.com)|ATL ViDz|ATL ViDz|\#|prod by Magix Enga|Xmix|Mad House Sounds|@elanimuziki    to|@elanimuziki|\@MR MIMS 254|Iphone x  Edit|greatlakesmix.com|Lovechild Records|Long Version|short Version|INTRODUCING VARIOUS NEW ARTISTES|CLUB VERSiON|RED ACAPELLA|Visuals|ItsNambaNanneTV|ItsNambaNnaneTV|prod. Dj Nephas|DIR_@TONY_DE_GIGZ|PROD by DJ NEPHAS|iXtendz|The Decimators|DIR-VIKTA DANIELS|Nakuru All Stars|Oolisikia Wapi|dj mistanewa|Dr@viktadaniel|BAETUESDAY|KENYAN VERSION|Dir. by @_Tony De Gigz_|dirby@qvsual|JACK JACK ON THE|ItsNambaNaneTV|or   to|Main Switch|send to|2018|dance crew|\{|\}|JustLife.com|SongsLover.com|Directed by @QuadDub|REFORMAT|5B   5D|unofficial|V2|h264|FHR|full video|hq|1080p|for skiza tune|FOR SKIZA TO 811|0fficial|Song|dial|send skiza|skiza|811|ixtendz|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
                  new_filename = re.sub(r"(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)

                  new_filename = re.sub(r"(\-)$","",new_filename, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"(\_)"," ",new_filename, flags=re.IGNORECASE)
                  new_filenamerz = re.sub(r"- -","-",new_filenamer, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\--","\-",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\---","\***",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamers = re.sub(r"(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)

                  #print("before spoty shit "+ new_filenamers)

                  new_filenamers = get_sporty_nigga(new_filenamers)
                  print(txt)

                  testing = os.path.join(txt,new_filenamers+'.MP4')
                  if os.path.exists(testing):
                      swag = os.path.join(txt,new_filenamers+' '+'.MP4')
                      
                      drake = os.rename(os.path.join(txt,filename), swag)
                      #print(testing)             
                  else:
                    drake = os.rename(os.path.join(txt,filename), testing)
                    #print(testing)                
    elif filename.endswith('.3gp'):
                  #continue
                  Video_File = os.path.join(txt, filename)          
                  new_filenames = re.sub("\.3gp|YouTube|\[SPOTIFY\-DOWNLOADER\.COM\]|clip|New Plus DOWNLOAD|download|(SongsLover.com)|ATL ViDz|ATL ViDz|\#|prod by Magix Enga|Xmix|Mad House Sounds|@elanimuziki    to|@elanimuziki|\@MR MIMS 254|Iphone x  Edit|greatlakesmix.com|Lovechild Records|Long Version|short Version|INTRODUCING VARIOUS NEW ARTISTES|CLUB VERSiON|RED ACAPELLA|Visuals|JACK JACK ON THE|ItsNambaNaneTV|or   to|Main Switch|send to|2018|dance crew|\{|\}|JustLife.com|SongsLover.com|Directed by @QuadDub|REFORMAT|ItsNambaNanneTV|ItsNambaNnaneTV|prod. Dj Nephas|DIR_@TONY_DE_GIGZ|PROD by DJ NEPHAS|iXtendz|The Decimators|DIR-VIKTA DANIELS|Nakuru All Stars|Oolisikia Wapi|dj mistanewa|Dr@viktadaniel|BAETUESDAY|KENYAN VERSION|Dir. by @_Tony De Gigz_|dirby@qvsual|5B   5D|unofficial|V2|h264|FHR|full video|hq|1080p|for skiza tune|FOR SKIZA TO 811|0fficial|Song|dial|send skiza|skiza|811|ixtendz|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
                  new_filename = re.sub(r"(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)

                  new_filename = re.sub(r"(\-)$","",new_filename, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"(\_)"," ",new_filename, flags=re.IGNORECASE)
                  new_filenamerz = re.sub(r"- -","-",new_filenamer, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\--","\-",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\---","\***",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamers = re.sub(r"(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)

                  #print("before spoty shit "+ new_filenamers)

                  new_filenamers = get_sporty_nigga(new_filenamers)
                  print(txt)

                  testing = os.path.join(txt,new_filenamers+'.3gp')
                  if os.path.exists(testing):
                      swag = os.path.join(txt,new_filenamers+' '+'.3gp')
                      drake = os.rename(os.path.join(txt,filename), swag)
                      #print(testing)
                  else:
                    drake = os.rename(os.path.join(txt,filename), testing)
                    #print(testing)
    elif filename.endswith('.mp3'):
                  # continue
                  new_filenames = re.sub("\.mp3|YouTube|\[SPOTIFY\-DOWNLOADER\.COM\]|clip|New Plus DOWNLOAD|download||(SongsLover.com)|ATL ViDz|ATL ViDz|\#|prod by Magix Enga|Xmix|Mad House Sounds|@elanimuziki    to|@elanimuziki|\@MR MIMS 254|Iphone x  Edit|greatlakesmix.com|Lovechild Records|Long Version|short Version|INTRODUCING VARIOUS NEW ARTISTES|CLUB VERSiON|RED ACAPELLA|Visuals|JACK JACK ON THE|ItsNambaNaneTV|or   to|Main Switch|send to|2018|dance crew|\{|\}|JustLife.com|SongsLover.com|Directed by @QuadDub|REFORMAT|5B   5D|unofficial|FHR|V2|h264|full video|hq||1080p|for skiza tune|FOR SKIZA TO 811|dial|0fficial|Song|send skiza|skiza|811|ixtendz|ItsNambaNanneTV|ItsNambaNnaneTV|prod. Dj Nephas|DIR_@TONY_DE_GIGZ|PROD by DJ NEPHAS|iXtendz|The Decimators|DIR-VIKTA DANIELS|Nakuru All Stars|Oolisikia Wapi|dj mistanewa|Dr@viktadaniel|BAETUESDAY|KENYAN VERSION|Dir. by @_Tony De Gigz_|dirby@qvsual|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
                  Video_File = os.path.join(txt, filename)                
                  new_filename = re.sub(r"(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)

                  new_filename = re.sub(r"(\-)$","",new_filename, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"(\_)"," ",new_filename, flags=re.IGNORECASE)
                  new_filenamerz = re.sub(r"- -","-",new_filenamer, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\--","\-",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\---","\***",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamers = re.sub(r"(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)

                  #print("before spoty shit "+ new_filenamers)

                  new_filenamers = get_sporty_nigga(new_filenamers)
                  print(txt)

                  testing = os.path.join(txt,new_filenamers+'.mp3')
                  if os.path.exists(testing):
                      swag = os.path.join(txt,new_filenamers+' '+'.mp3')
                      drake = os.rename(os.path.join(txt,filename), swag)
                      #print(testing)
                  else:
                    drake = os.rename(os.path.join(txt,filename), testing)
                    #print(testing)
#shimpest

def shrimps(filename):
    if filename.endswith('.mkv'):
                  # continue
              Video_File = os.path.join(txt3, filename)             
              new_filenames = re.sub("\.mkv|\[SPOTIFY\-DOWNLOADER\.COM\]|clip|ATL ViDz|ATL ViDz|\#|ItsNambaNanneTV|ItsNambaNnaneTV|prod. Dj Nephas|DIR_@TONY_DE_GIGZ|PROD by DJ NEPHAS|iXtendz|The Decimators|DIR-VIKTA DANIELS|Nakuru All Stars|Oolisikia Wapi|dj mistanewa|Dr@viktadaniel|BAETUESDAY|KENYAN VERSION|Dir. by @_Tony De Gigz_|dirby@qvsual|prod by Magix Enga|Xmix|Mad House Sounds|@elanimuziki    to|@elanimuziki|\@MR MIMS 254|Iphone x  Edit|greatlakesmix.com|Lovechild Records|Long Version|short Version|INTRODUCING VARIOUS NEW ARTISTES|CLUB VERSiON|RED ACAPELLA|Visuals|JACK JACK ON THE|ItsNambaNaneTV|or   to|Main Switch|send to|2018|dance crew|\{|\}|JustLife.com|(SongsLover.com)|SongsLover.com|YouTube|Directed by @QuadDub|REFORMAT|5B   5D|unofficial|V2|h264|FHR|full video|hq|1080p|for skiza tune|FOR SKIZA TO 811|0fficial|Song|dial|send skiza|skiza|811|ixtendz|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
              new_filename = re.sub(r"(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)

              new_filename = re.sub(r"(\-)$","",new_filename, flags=re.IGNORECASE)
              new_filenamer = re.sub(r"(\_)"," ",new_filename, flags=re.IGNORECASE)
              new_filenamerz = re.sub(r"- -","-",new_filenamer, flags=re.IGNORECASE)
              new_filenamer = re.sub(r"\--","\-",new_filenamerz, flags=re.IGNORECASE)
              new_filenamer = re.sub(r"\---","\***",new_filenamerz, flags=re.IGNORECASE)
              new_filenamers = re.sub(r"(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)

              #print("before spoty shit "+ new_filenamers)

              new_filenamers = get_sporty_nigga(new_filenamers)
              print(txt)

              testing = os.path.join(txt3,new_filenamers+'.mkv')
              if os.path.exists(testing):
                      swag = os.path.join(txt3,new_filenamers+' '+'.mkv')
                      drake = os.rename(os.path.join(txt3,filename), swag)
                      #print(testing)
              else:
                     drake = os.rename(os.path.join(txt3,filename), testing)
                     #print(testing)
    elif filename.endswith('.MKV'):
                  # continue
                  Video_File = os.path.join(txt3, filename)               
                  new_filenames = re.sub("\.MKV|\[SPOTIFY\-DOWNLOADER\.COM\]|clip|(SongsLover.com)|ATL ViDz|ItsNambaNanneTV|ItsNambaNnaneTV|prod. Dj Nephas|DIR_@TONY_DE_GIGZ|PROD by DJ NEPHAS|iXtendz|The Decimators|DIR-VIKTA DANIELS|Nakuru All Stars|Oolisikia Wapi|dj mistanewa|Dr@viktadaniel|BAETUESDAY|KENYAN VERSION|Dir. by @_Tony De Gigz_|dirby@qvsual|ATL ViDz|\#|prod by Magix Enga|Xmix|Mad House Sounds|@elanimuziki    to|@elanimuziki|\@MR MIMS 254|Iphone x  Edit|greatlakesmix.com|Lovechild Records|Long Version|short Version|INTRODUCING VARIOUS NEW ARTISTES|CLUB VERSiON|RED ACAPELLA|Visuals|JACK JACK ON THE|ItsNambaNaneTV|or   to|Main Switch|send to|2018|dance crew|\{|\}|JustLife.com|SongsLover.com|YouTube|Directed by @QuadDub|REFORMAT|5B   5D|unofficial|V2|h264|FHR|full video|hq|1080p|for skiza tune|FOR SKIZA TO 811|0fficial|Song|dial|send skiza|skiza|811|ixtendz|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
                  new_filename = re.sub(r"(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)

                  new_filename = re.sub(r"(\-)$","",new_filename, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"(\_)"," ",new_filename, flags=re.IGNORECASE)
                  new_filenamerz = re.sub(r"- -","-",new_filenamer, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\--","\-",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\---","\***",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamers = re.sub(r"(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)

                  #print("before spoty shit "+ new_filenamers)

                  new_filenamers = get_sporty_nigga(new_filenamers)
                  print(txt)

                  testing = os.path.join(txt3,new_filenamers+'.MKV')
                  if os.path.exists(testing):
                      swag = os.path.join(txt3,new_filenamers+' '+'.MKV')
                      drake = os.rename(os.path.join(txt3,filename), swag)
                      #print(testing)
                  else:
                    drake = os.rename(os.path.join(txt3,filename), testing)
                    #print(testing)
                
    elif filename.endswith('.mp4'):
                  # continue
                  Video_File = os.path.join(txt3, filename)               
                  # continue
                  #print('Tis mp4')
                  Video_File = os.path.join(txt3, filename)              
                  new_filenames = re.sub("\.mp4|YouTube|\[SPOTIFY\-DOWNLOADER\.COM\]|New Plus DOWNLOAD|download|clip|(SongsLover.com)|ATL ViDz|ATL ViDz|\#|prod by Magix Enga|Xmix|Mad House Sounds|@elanimuziki    to|@elanimuziki|\@MR MIMS 254|Iphone x  Edit|ItsNambaNanneTV|ItsNambaNnaneTV|prod. Dj Nephas|DIR_@TONY_DE_GIGZ|PROD by DJ NEPHAS|iXtendz|The Decimators|DIR-VIKTA DANIELS|Nakuru All Stars|Oolisikia Wapi|dj mistanewa|Dr@viktadaniel|BAETUESDAY|KENYAN VERSION|Dir. by @_Tony De Gigz_|dirby@qvsual|greatlakesmix.com|Lovechild Records|Long Version|short Version|INTRODUCING VARIOUS NEW ARTISTES|CLUB VERSiON|RED ACAPELLA|Visuals|JACK JACK ON THE|ItsNambaNaneTV|or   to|Main Switch|send to|2018|dance crew|\{|\}|JustLife.com|SongsLover.com|Directed by @QuadDub|REFORMAT|5B   5D|unofficial|V2|FHR|1080p|full video|hq|h264|for skiza tune|FOR SKIZA TO 811|dial|0fficial|Song|send skiza|skiza|811|ixtendz|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
                  new_filename = re.sub(r"(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)

                  new_filename = re.sub(r"(\-)$","",new_filename, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"(\_)"," ",new_filename, flags=re.IGNORECASE)
                  new_filenamerz = re.sub(r"- -","-",new_filenamer, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\--","\-",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\---","\***",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamers = re.sub(r"(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)

                  #print("before spoty shit "+ new_filenamers)

                  new_filenamers = get_sporty_nigga(new_filenamers)
                  print(txt)

                  testing = os.path.join(txt3,new_filenamers+'.mp4')
                  if os.path.exists(testing):
                      swag = os.path.join(txt3,new_filenamers+' '+'.mp4')
                      drake = os.rename(os.path.join(txt3,filename), swag)
                      #print(testing)
                  else:
                    drake = os.rename(os.path.join(txt3,filename), testing)
                    #print(testing)
    elif filename.endswith('.MP4'):
                  # continue
                  Video_File = os.path.join(txt3, filename)              
                  new_filenames = re.sub("\.MP4|YouTube|\[SPOTIFY\-DOWNLOADER\.COM\]|clip|New Plus DOWNLOAD|download|(SongsLover.com)|ATL ViDz|ATL ViDz|\#|prod by Magix Enga|Xmix|Mad House Sounds|@elanimuziki    to|@elanimuziki|\@MR MIMS 254|Iphone x  Edit|greatlakesmix.com|Lovechild Records|Long Version|short Version|INTRODUCING VARIOUS NEW ARTISTES|CLUB VERSiON|RED ACAPELLA|Visuals|ItsNambaNanneTV|ItsNambaNnaneTV|prod. Dj Nephas|DIR_@TONY_DE_GIGZ|PROD by DJ NEPHAS|iXtendz|The Decimators|DIR-VIKTA DANIELS|Nakuru All Stars|Oolisikia Wapi|dj mistanewa|Dr@viktadaniel|BAETUESDAY|KENYAN VERSION|Dir. by @_Tony De Gigz_|dirby@qvsual|JACK JACK ON THE|ItsNambaNaneTV|or   to|Main Switch|send to|2018|dance crew|\{|\}|JustLife.com|SongsLover.com|Directed by @QuadDub|REFORMAT|5B   5D|unofficial|V2|h264|FHR|full video|hq|1080p|for skiza tune|FOR SKIZA TO 811|0fficial|Song|dial|send skiza|skiza|811|ixtendz|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
                  new_filename = re.sub(r"(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)

                  new_filename = re.sub(r"(\-)$","",new_filename, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"(\_)"," ",new_filename, flags=re.IGNORECASE)
                  new_filenamerz = re.sub(r"- -","-",new_filenamer, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\--","\-",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\---","\***",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamers = re.sub(r"(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)

                  #print("before spoty shit "+ new_filenamers)

                  new_filenamers = get_sporty_nigga(new_filenamers)
                  print(txt)

                  testing = os.path.join(txt3,new_filenamers+'.MP4')
                  if os.path.exists(testing):
                      swag = os.path.join(txt3,new_filenamers+' '+'.MP4')
                      drake = os.rename(os.path.join(txt3,filename), swag)
                      #print(testing)             
                  else:
                    drake = os.rename(os.path.join(txt3,filename), testing)
                    #print(testing)                
    elif filename.endswith('.3gp'):
                  #continue
                  Video_File = os.path.join(txt3, filename)          
                  new_filenames = re.sub("\.3gp|YouTube|\[SPOTIFY\-DOWNLOADER\.COM\]|clip|New Plus DOWNLOAD|download|(SongsLover.com)|ATL ViDz|ATL ViDz|\#|prod by Magix Enga|Xmix|Mad House Sounds|@elanimuziki    to|@elanimuziki|\@MR MIMS 254|Iphone x  Edit|greatlakesmix.com|Lovechild Records|Long Version|short Version|INTRODUCING VARIOUS NEW ARTISTES|CLUB VERSiON|RED ACAPELLA|Visuals|JACK JACK ON THE|ItsNambaNaneTV|or   to|Main Switch|send to|2018|dance crew|\{|\}|JustLife.com|SongsLover.com|Directed by @QuadDub|REFORMAT|ItsNambaNanneTV|ItsNambaNnaneTV|prod. Dj Nephas|DIR_@TONY_DE_GIGZ|PROD by DJ NEPHAS|iXtendz|The Decimators|DIR-VIKTA DANIELS|Nakuru All Stars|Oolisikia Wapi|dj mistanewa|Dr@viktadaniel|BAETUESDAY|KENYAN VERSION|Dir. by @_Tony De Gigz_|dirby@qvsual|5B   5D|unofficial|V2|h264|FHR|full video|hq|1080p|for skiza tune|FOR SKIZA TO 811|0fficial|Song|dial|send skiza|skiza|811|ixtendz|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
                  new_filename = re.sub(r"(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)

                  new_filename = re.sub(r"(\-)$","",new_filename, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"(\_)"," ",new_filename, flags=re.IGNORECASE)
                  new_filenamerz = re.sub(r"- -","-",new_filenamer, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\--","\-",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\---","\***",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamers = re.sub(r"(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)

                  #print("before spoty shit "+ new_filenamers)

                  new_filenamers = get_sporty_nigga(new_filenamers)
                  print(txt)

                  testing = os.path.join(txt3,new_filenamers+'.3gp')
                  if os.path.exists(testing):
                      swag = os.path.join(txt3,new_filenamers+' '+'.3gp')
                      drake = os.rename(os.path.join(txt3,filename), swag)
                      #print(testing)
                  else:
                    drake = os.rename(os.path.join(txt3,filename), testing)
                    #print(testing)
    elif filename.endswith('.mp3'):
                  # continue
                  new_filenames = re.sub("\.mp3|YouTube|\[SPOTIFY\-DOWNLOADER\.COM\]|clip|New Plus DOWNLOAD|download||(SongsLover.com)|ATL ViDz|ATL ViDz|\#|prod by Magix Enga|Xmix|Mad House Sounds|@elanimuziki    to|@elanimuziki|\@MR MIMS 254|Iphone x  Edit|greatlakesmix.com|Lovechild Records|Long Version|short Version|INTRODUCING VARIOUS NEW ARTISTES|CLUB VERSiON|RED ACAPELLA|Visuals|JACK JACK ON THE|ItsNambaNaneTV|or   to|Main Switch|send to|2018|dance crew|\{|\}|JustLife.com|SongsLover.com|Directed by @QuadDub|REFORMAT|5B   5D|unofficial|FHR|V2|h264|full video|hq||1080p|for skiza tune|FOR SKIZA TO 811|dial|0fficial|Song|send skiza|skiza|811|ixtendz|ItsNambaNanneTV|ItsNambaNnaneTV|prod. Dj Nephas|DIR_@TONY_DE_GIGZ|PROD by DJ NEPHAS|iXtendz|The Decimators|DIR-VIKTA DANIELS|Nakuru All Stars|Oolisikia Wapi|dj mistanewa|Dr@viktadaniel|BAETUESDAY|KENYAN VERSION|Dir. by @_Tony De Gigz_|dirby@qvsual|vxtendz|For Skiza  skiza  to 811|\'|\"|ogopa video|WSHH Exclusive|skiza to 811|hd|Tubidy.io|360p|480p||SabWap.CoM|Directed by WeL!iveTV|Prod. By JDONTHATRACK|Prod. by JDOnThaTrack|@prodbyyaygo|Fun Video|nrXtendz|Xtendz|Coke Studio Africa|(Intro Outro)|SNMiX|Dir.Ivan Odie|- _2|mpeg2|Ashawo|lucie|clean|via torchbrowser.com|Afrobeats|prod. by Team Salut - #FlavourzEP|Produced by Team Salut|GRM Daily|official mash up video|mpeg|Vibes Video|extended|beat|instrumental|ug remix|Baba nla|nr|xtends|YTMAs|Prod By- Tay Keith|y2mate\.com|audio|visualizer|Acoustic|QUARANTINE LOVE|Lyric|demo|Soundtrack|SpiderMan- Into The SpiderVerse Soundtrack|Produced by. StarboyUniverse|Prod. By Tony Fadd|Danielle Bregoli is|Prod. by Ulopa & Kus Ma|BEAT LINK|Mash Up|Ogede|emPawa Africa &|#emPawa100 Artist|Badder Than Bad|RH Exclusive|Gbadun You|Danielle Bregoli|Extended Version|2016|2017|Shot By- @Yoo Ali|Dir. Shooter-7-Seven|Dir Gerard Victor|Late Night with Seth Meyers|720p|London On Da Track|Prod. by JDOnThaTrack|Prod. by DJ Cause|I Know I'm Right Pt. 2|Directed by WeL!iveTV|- WSHH Exclusive -|from CREED- Original Motion Picture Soundtrack|The Album - Diamonds|720P HD|Spider-Man- Into the Spider-Verse|Freestyle|Quality Control|via torchbrowser.com|Prod. By Young Mercy DL|WSHH_Exclusive|hd720|By PDUB The Producer|Dir By JDFilms|Prod. by London on Tha Track|Into The SpiderVerse Soundtrack|THE SCOTTS FORTNITE ASTRONOMICAL EVENT|DN4|Oficial|Produced by. StarboyUniverse|WSHH Exclusive|youtube|Copy|official|music|Dir. by @_ColeBennett|video|\[|\]|\,|\/|\\|\_|lyric|remix|explicit|4k|SMS|wshh exclusve|Presented by @lakafilms|TO 811 FOR SKIZA|([0-9]{5,20})|directed by cole bennett", "", filename, flags=re.IGNORECASE)
                  Video_File = os.path.join(txt3, filename)                
                  new_filename = re.sub(r"(\(\d.*\))|(\()|(\))|^(\-)|(\-)$|(\_)$|^([ ]{0,})|([ ]{0,})$|((\_).([ ]{0,}))$|(\s\s*)$","",new_filenames, flags=re.IGNORECASE)

                  new_filename = re.sub(r"(\-)$","",new_filename, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"(\_)"," ",new_filename, flags=re.IGNORECASE)
                  new_filenamerz = re.sub(r"- -","-",new_filenamer, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\--","\-",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamer = re.sub(r"\---","\***",new_filenamerz, flags=re.IGNORECASE)
                  new_filenamers = re.sub(r"(\s\s*)$","",new_filenamer, flags=re.IGNORECASE)

                  #print("before spoty shit "+ new_filenamers)

                  new_filenamers = get_sporty_nigga(new_filenamers)
                  print(txt)

                  testing = os.path.join(txt3,new_filenamers+'.mp3')
                  if os.path.exists(testing):
                      swag = os.path.join(txt3,new_filenamers+' '+'.mp3')
                      drake = os.rename(os.path.join(txt3,filename), swag)
                      #print(testing)
                  else:
                    drake = os.rename(os.path.join(txt3,filename), testing)
                    #print(testing)
root.mainloop()
