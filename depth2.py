#!/usr/bin/env python

import re

InFileName = 'ctd.txt'
InFile = open(InFileName, 'r')

LineNumber = 0

OutFileName = 'MaxDepthFile'
OutFile = open(OutFileName, 'w')

#Create empty lists to store depth & time
DepthList = [] 		#List of depths
DepthTimeList = []	#List of depth & time
DepthTimeList800 = []	#List of depth & time for depth>800m

for Line in InFile:
	if LineNumber > 0:
		Line=Line.strip('\n')
		ElementList=Line.split(',')
		Depth = float(ElementList[4])	#Isolate the depth as a float
		DepthList.append(Depth)		#Make a list of all depths

		Time = ElementList[1].split()[1]	#Isolate time

		#Separate hours, minutes, seconds & convert to float
		Time = Time.split(':')	
		HourCol = float(Time[0])
		MinCol = float(Time[1])
		SecCol = float(Time[2])
		#Calculate time in seconds
		Seconds = (3600*HourCol)+(60*MinCol)+SecCol

		#Make a list containing all depth & time
		DepthTimeList.append([float(Depth),float(Seconds)])

		#Make a list of depth & times below 800m
		if Depth >= 800:
			DepthTimeList800.append\
			([float(Depth),float(Seconds)])

	LineNumber = LineNumber + 1

#Caclulate maximum depth
DepthListSorted=sorted(DepthList)
MaxDepth = DepthListSorted[-1]	#Find maximum depth
MinDepth = DepthListSorted[0]	#Find minimum depth

MaxDepthStatement = "The maximum depth reached was %.2f meters." % (MaxDepth)
OutFile.write(MaxDepthStatement + '\n')

#Calculate time to 800m & time below 800m
Init = DepthTimeList[0]		#Isolate the initial time point
Init800 = DepthTimeList800[0]	#Identify the first time point below 800m
Final = DepthTimeList800[-1]	#Identifiy the final time point below 800m

#Calculate time to reach 800 m by subtracting time initial time
TimeTo800 = (float(Init800[1])-float(Init[1]))/60

#Calculate time belwo 800m
TimeBelow = (float(Final[1])-float(Init800[1]))/60

print "From the initial recording, it took %.0f minutes to reach 800 meters." \
	% (TimeTo800)
print "The submersible remained below 800 meters for %.0f minutes." \
	% (TimeBelow)


InFile.close()
OutFile.close()
