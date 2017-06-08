#!/usr/bin/python3
import re
import requests
import argpar
import sys
import copy

def links_get(baselink):
	ret = []
	for  i in range(1, int(re.findall("page=([0-9]+)", requests.get(baselink).headers["Link"].split(",")[1])[0]) + 1):
		ret.append(baselink + "?page=" + str(i))
	return ret

def pages_get(links):
	ret = []
	for link in links:
		ret.extend(requests.get(link).json())
	return ret

if __name__ == '__main__':
	args = argpar.parse({"u": "https://api.github.com/users/{}/repos"}, copy.copy(sys.argv), posarg={"user": None})
	for repo in pages_get(links_get(args["u"].format(args["user"]))):
		print(repo["html_url"])