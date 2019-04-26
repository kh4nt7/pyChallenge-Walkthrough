#!/usr/bin/env python
import re
import zipfile

archieve = zipfile.ZipFile('channel.zip', 'r')
comments = []

filename = "90052"
ext = ".txt"

prev = ""
count = 0

while True:
	with open(filename+ext) as file:
		try:
			data = file.read()
			number = re.findall(r'[0-9]+',data)[0]
			count += 1
			comments.append(archieve.getinfo(number+ext).comment.decode('utf-8'))
			prev = number
			print("[*] Next File: {}, count {}".format(number,count))
			filename = number
		except IndexError:
			print("[*] Found File: {}, count {}".format(prev, count-1))
			print()
			break

print("[*] Starting to expand comments ...")
print()
print("".join([c for c in comments]))
