#!/bin/python
#coding:utf-8

def analysis(string):
    global ii, jj
    lists = []
    src = lyric = title = ' '
    type = 0
    if "_id" in string:
        lists = string.split(',')
        for i in lists:
            if "_id" in i:
                #print i
                _, _, thisID = i.split(":")
                if int(thisID[2:-3]) in chinese:
                    ii += 1
                    type = 9
                    fwrite.write("chinese" + '\n')
                elif int(thisID[2:-3]) in english:
                    jj += 1
                    type = 1
                    fwrite.write("english" + '\n')
                else:
                    type = 0
                    break
            if "src" in i:
                _, src = i.split(":")
            if "lyric_url" in i:
                _, lyric = i.split(":")
            if "title" in i:
                _, title = i.split(":")

        if len(src) > 10 and type != 0:
            #print lyric, src
            lyric = lyric[2:-1]
            src = src[2:-1]
            if len(lyric) < 10:
                lyric = "none"
            else:
                lyric = qiniu + lyric
            src = qiniu + src
            if "Walk" in title:
                title = "《Walking, Walking》西西教唱歌"
            else:
                title = title[1:]
            fwrite.write(title + '\n')
            fwrite.write(src + '\n')
            fwrite.write(lyric + '\n')
            print title
            print src
            print lyric

qiniu = "http://7xls3g.com1.z0.glb.clouddn.com/"



f = file("./musictype")

chinese = []
english = []

while True:
    line = f.readline()
    if len(line) == 0:
        break
    _, type, _, id, _ = line.split("\"")
    if int(type) == 9:
        chinese.append(int(id))
    elif int(type) == 1:
        english.append(int(id))

f.close()


f = file("./audios")
fwrite = file("./afteranalysis.txt", 'w')

ii = 0
jj = 0
while True:
    line = f.readline()
    if len(line) == 0:
        break
    analysis(line)

print chinese, len(chinese)
print english, len(english)
print ii, jj

f.close()
