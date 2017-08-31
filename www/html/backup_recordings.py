#!/usr/bin/python 

import datetime
import os
from subprocess import call
import sys

if sys.argv[1]=="today":
    today= datetime.date.today().strftime("%Y%m%d")
else:
    today= sys.argv[1]

duration=0


tgid=sys.argv[2]


if len(sys.argv)<4:
    rid=""
    duration_filter=0
else:
    rid=sys.argv[3]
    duration_filter=sys.argv[4]

root_folder = "/var/www/html/VC-Record/"
today_folder = root_folder + today

tgid_rid="_"+tgid+"_"+rid


today_files = os.listdir(today_folder)
for today_file in reversed(today_files):
	if tgid_rid in today_file:
		duration=int(today_file[7:10])
		if duration>int(duration_filter):
			file = today_folder +"/"+ today_file
			print "<a href=\"/VC-Record/"+today+"/"+today_file +"\" target=\"archive\"\">"+today_file+"</a><hr>"


