#!/bin/python
#coding:utf-8

def analysis(string):
    lists = []
    music = lyric = title = ' '
    if "lyric_url" in string:
        lists = string.split(',')
        for i in lists:
            if "music_url" in i:
                _, music = i.split(" : ")
            if "lyric_url" in i:
                _, lyric = i.split(" : ")
            if "title" in i:
                _, title = i.split(":")
        print music
        if len(music) > 10:
            #print lyric, src
            lyric = lyric[:-2]
            #music = music[2:-1]
            if len(lyric) < 10:
                lyric = "none"
            if "Walk" in title:
                title = "《Walking, Walking》西西教唱歌"
            else:
                title = title[1:]
            fwrite.write(title + '\n')
            fwrite.write(music + '\n')
            fwrite.write(lyric + '\n')
            #print title
            #print music
            #print lyric

f = file("./musics")
fwrite = file("./afteranalysis.txt", 'w')

while True:
    line = f.readline()
    if len(line) == 0:
        break
    analysis(line)

f.close()
