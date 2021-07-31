from __future__ import unicode_literals
import youtube_dl
import os
from sys import platform


if platform == "linux" or platform == "linux2":
    os.system("sudo apt install ffmpeg")
    os.system("clear")


ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }
    ],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    while True:
        print("[Type exit to close this application]")
        x = input("Enter Youtube link: ")

        if x == "exit":
            break

        try:
            ydl.download([x])
        except:
            os.system("clear")
            print("Please enter correct youtube URL or enter exit\n")
