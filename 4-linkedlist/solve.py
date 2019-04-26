#!/usr/bin/env python3
import urllib.request
import re

url_source = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

chain = "400" # 66831
chain_count = 0
querystring = "nothing="
url = url_source + "?" + querystring + chain
prev_chain = ""

while True:
	try:
		response = urllib.request.urlopen(url)
		resp = response.read().decode()
		
		number = re.findall(r"[0-9]+", resp)
		chain = number[0]
		prev_chain = chain
		chain_count += 1

		print("[*] Chain Found: {}, chained {} times".format(chain,chain_count))
		print("[*] Response: ")
		print(resp)
		url = url_source + "?" + querystring + chain
	except IndexError:
		print("[*] Chain Finished!")
		print("[*] Chain Found: {}, chained {} times".format(prev_chain,chain_count-1))
		print("[*] Next Level : {}".format(resp))
		break

