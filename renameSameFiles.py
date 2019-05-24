#!/usr/bin/python
import os

file = "esempio.txt" #nome del file da cercare
path = "../esempio/" #percorso di destinazione
final_path = path + file

founded = True
count = 1

while founded == True:
	try:
		fh = open(final_path, 'r')
		founded = True
		oldext = file.split(".")[-1]
		oldtext = file.split(".")[0]
		os.rename(final_path, path + oldtext + str(count) + "." + oldext)

		count += 1

	except FileNotFoundError:
		founded = False
		print("Not found")
