from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    while True:
        x = input('Enter Youtube link: ')

        if x == -1:
            break

        ydl.download([x])
        