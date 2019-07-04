import pytube
from pytube import YouTube
import sys
import os
from urllib.request import Request, urlopen

LIST_FILE = sys.argv[1]
OUT_PATH = sys.argv[2]
if not os.path.exists(OUT_PATH):
    os.makedirs(OUT_PATH)

LIST = open(LIST_FILE, "r")
ITEMS = LIST.readlines()

def yt_download(link, path_to_download):
    link = str(link)
    yt = YouTube(link)
    print ("title is: ", yt.title)
    print (yt.streams.filter().first() ) #res="480p"
    stream = yt.streams.filter().first()

    print (".....downloading........")
    stream.download(path_to_download)
    print ("download done")
    return None


# for i in ITEMS:
#     print (i)
#     yt_download(i, OUT_PATH)
#     print ("done")

yt_download("https://youtu.be/OEn45sjHDCc", OUT_PATH)
