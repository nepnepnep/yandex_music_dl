from __future__ import unicode_literals
import urllib.request, json
import youtube_dl

def download_my_music(music_directory,list_music):
    ydl_opts = {
        'outtmpl': music_directory+'%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(list_music)
def getListMymusic(url_music):
    with urllib.request.urlopen(url_music) as url:
        data = json.loads(url.read().decode())
        return data['playlist']['trackIds']
def parseListSongs(listSong):
    listUrl = []
    for song in listSong:
        songname    = song.split(":")[0]
        album       = song.split(":")[1]
        listUrl.append( "https://music.yandex.ru/album/"+album+"/track/"+songname)
    return listUrl


download_my_music('/home/sivannikov/Music/ya_music/',parseListSongs(getListMymusic("https://music.yandex.ru/handlers/playlist.jsx?owner=nepneppen&kinds=3&light=true")))
