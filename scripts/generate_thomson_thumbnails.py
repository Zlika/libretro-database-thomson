#!/usr/bin/python3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# This script downloads thumbnails for Thomson games
# from the ScreenScraper site.
# To optimize the size of the Snap and Title images, use imagemagick
# to reduce the number of colors to 256 with the following command:
# mogrify -colors 256 -depth 8 *.png

from collections import namedtuple, OrderedDict
import datetime
import os
import re
import urllib.request


THOMSON_PLATFORMID = 141
SCREENSCRAPER_URL = "https://www.screenscraper.fr/"
SCREENSCRAPER_GAMESLIST_URL = SCREENSCRAPER_URL + "medias/" + str(THOMSON_PLATFORMID) + "/gameslist.csv"
SCREENSCAPER_MEDIA_BASEURL=SCREENSCRAPER_URL + "image.php?gameid="


def checkPng(imgFile):
	with open(imgFile, "rb") as f:
		bytes = f.read(4)
		if bytes != b'\x89PNG':
			os.remove(imgFile)


def download_thumbnails(gameid, gamename):
	print("Downloading media for " + gamename)
	# Download Boxart
	boxart = "../thumbnails/Named_Boxarts/" + gamename + ".png"
	try:
		urllib.request.urlretrieve(SCREENSCAPER_MEDIA_BASEURL + str(gameid) + "&media=box-2D&region=wor&maxwidth=512", boxart)
		checkPng(boxart)
	except:
		print("Cannot find Boxart image for game " + gamename)
	# Download Snap
	snap = "../thumbnails/Named_Snaps/" + gamename + ".png"
	try:
		urllib.request.urlretrieve(SCREENSCAPER_MEDIA_BASEURL + str(gameid) + "&media=ss&region=wor&maxwidth=320", snap)
		checkPng(snap)
	except:
		print("Cannot find Snap image for game " + gamename)
	# Download Title
	title = "../thumbnails/Named_Titles/" + gamename + ".png"
	try:
		urllib.request.urlretrieve(SCREENSCAPER_MEDIA_BASEURL + str(gameid) + "&media=sstitle&region=wor&maxwidth=320", title)
		checkPng(title)
	except:
		print("Cannot find Title image for game " + gamename)


def get_gameslist():
	with urllib.request.urlopen(SCREENSCRAPER_GAMESLIST_URL) as response:
		csvfile = response.read().decode('cp1252').replace('"', '')
	lines = csvfile.splitlines()
	gameslist = []
	for i in range(1, len(lines)):
		columns = lines[i].split(';')
		gameslist.append([columns[0], columns[1]])
	return gameslist


if __name__ == "__main__":
	gameslist = get_gameslist()
	for game in gameslist:
		download_thumbnails(game[0], game[1])

