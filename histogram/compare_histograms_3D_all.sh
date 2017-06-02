#!/bin/bash

path=`pwd`
path="${path}/../spectrogram/images"

echo "Searching for files in path $path..."

for entry in "${path}"/*
do
    for entry2 in "${path}"/*
    do
	   if [ "$entry" != "$entry2" ]
	   then
		  echo "filename1 is $entry"
		  echo "filename2 is $entry2"
		  python compare_histograms_1D.py -i "$entry" -i2 "$entry2"
		  echo " "
	   fi
    done
done
