#!/bin/sh

if [ ! -f  "americanIdolWinners.csv" ]
then
	mv americanIdolWinners.xlsx americanIdolWinners.csv
fi

python3 data.py
