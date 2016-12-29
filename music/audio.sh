#!/bin/bash

#for LINE in `cat ./afteranalysis.txt`
#do
#	echo $LINE
#done

i=0
a=4
en=0
filepath="./afteranalysis.txt"
dir="/home/szy/audios"
src="song.mp3"
lyric="lyric.txt"
chinese="/home/szy/audios/chinese"
english="/home/szy/audios/english"

rm -rf "$dir"
mkdir $dir
mkdir "$dir/chinese"
mkdir "$dir/english"
while read LINE
do
	if [ $((i%a)) -eq 0 ];then
		if [ $LINE == "chinese" ];then
			dir1=$chinese
		elif [ $LINE == "english" ];then
			let en=$en+1
			dir1=$english
		fi
		echo $dir1, ----------------------------------------------$LINE
	elif [ $((i%a)) -eq 1 ];then
		mkdir "$dir1/$LINE"
		route="$dir1/$LINE"
		echo $route
	elif [ $((i%a)) -eq 2 ];then
		curl -o "$route/$src" $LINE
		echo src $route/$src
	elif [ $((i%a)) -eq 3 ];then
		if [ $LINE == "none" ]; then
			echo "no lyric"
		else
			curl -o "$route/$lyric" $LINE
			echo lyric  $route/$lyric
		fi
	fi
	
	let i=$i+1
done <$filepath
echo  $en
