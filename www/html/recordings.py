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

tgids={
	600: "HHFD DISP",
	604: "HHFD TAC4",
	605: "HHFD Training",
	700: "OFD DISPATCH",
	800: "BFD DISPATCH",
}

rids={
	109: "AVD",
	108: "Dispatch",
	107: "Dispatch",
	114: "Dispatch",
	62005: "P311",
	62013: "P321",
	62014: "P331",
	62024: "R312",
	62015: "P341",
	62022: "R372",
	62010: "P361",
	62016: "L342",
	62021: "P371",
	62023: "Q381",
	62004: "C30",
	61008: "P311-A",
	61039: "P321-A",
	61044: "P331-A",
	61012: "R312-A",
	61049: "P341-A",
	61082: "R372-A",
	61073: "P361-A",
	61054: "L342-A",
	61078: "P371-A",
	61077: "Q381-A",
	61013: "C30-A",
	61009: "P311-B",
	61040: "P321-B",
	61045: "P331-B",
	61014: "R312-B",
	61050: "P341-B",
	61083: "R372-B",
	61074: "P361-B",
	61053: "L342-B",
	61079: "P371-B",
	61087: "Q381-B",
	61006: "C30-B",
	61010: "P311-C",
	61041: "P321-C",
	61046: "P331-C",
	61015: "R312-C",
	61051: "P341-C",
	61084: "R372-C",
	61075: "P361-C",
	61055: "L342-C",
	61005: "Q381-C",
	61007: "C30-C",

	61011: "P311-D",
	61047: "P331-D",
	61016: "R312-D",
	61052: "P341-D",
	61085: "R372-D",
	61076: "P361-D",
	61056: "L342-D",
	61000: "Q381-D",
	61013: "C30-D",
	62025: "317",
	62006: "R316-RESERVE",

}


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
			if int(today_file[32:35]) in tgids:
				tg_name=tgids[int(today_file[32:35])]
			else:
				tg_name=today_file[32:35]
			if int(today_file[36:int(len(today_file)-4)]) in rids:
				radio_name=rids[int(today_file[36:int(len(today_file)-4)])]
			else:
				radio_name=int(today_file[36:int(len(today_file)-4)])
			print "<a href=\"/VC-Record/"+today+"/"+today_file +"\" target=\"archive\"\">"+str(today_file[:2])+":"+str(today_file[2:4])+":"+str(today_file[4:6])+" - ("+str(today_file[7:10]).lstrip("0")+"s) - "+str(tg_name)+" - "+str(radio_name)+"</a><hr>"




