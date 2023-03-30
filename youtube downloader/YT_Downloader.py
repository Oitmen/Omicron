
from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor
import re

def herunterladens():
    link = input("Füge den Link ein:")
    yt = YouTube(link)
    print("Das zu herunterlatende Lied: ",yt.title)
    print("Wird herunter geladen...")
    yt.streams.filter(only_audio=True).first().download()
    print("Wurde Heruntergeladne")

def herunterladnep():
    link = input("Füge den Link ein:")
    pl = Playlist(link)
    print("download startet...")
    for url in pl:
        print("download")
        YouTube(url).streams.filter(only_audio=True).first().download()


def mp3():
    print("Wird zu mp3 umgewandelt...")
    for file in os.listdir():
        if re.search('mp4', file):
            mp4_path = os.path.join(file)
            mp3_path = os.path.join(os.path.splitext(file)[0]+'.mp3')
            new_file = moviepy.editor.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
    print("Fertig")




def Programm1():
    while True:
        herunterladens()
        mp3()

def Programm2():
    while True:
        herunterladnep()
        mp3()
        
        
def main():
    pom = input("Möchtest du einzelne Songs(s) oder ganze Plalisten(p) herunterladen:(s/p)")
    if pom == "s":
        Programm1()
    else:
        Programm2()

try:
    main()
except:
    print("error")
    