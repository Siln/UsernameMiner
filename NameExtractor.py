#!/usr/bin/env python

## Script: NameExtractor.py
## Author: FolieADeux
## Date: 11/12/2012
## This script is intended to take a list of names and see if 
## any two represent a first name and last name combination in
## the body of a target URL's webpage. The names are based on 
## input files to account for localization, but US name files
## are included with the program.
## Redistribute and edit as you wish.

from bs4 import BeautifulSoup
import os
import sys
import urllib
import urllib2

#Handle Arguments
if len(sys.argv) < 5:
  print "USAGE: " + sys.argv[0] + " TARGET_URL FIRSTNAME_FILE LASTNAME_FILE OUTPUT_FILE"
	sys.exit()

target = sys.argv[1]
firstNameLocation = sys.argv[2]
lastNameLocation = sys.argv[3]
outLocation = sys.argv[4]

#Grab URL Text
page = urllib2.urlopen(target)
soup = BeautifulSoup(page)
pageText = soup.body(text = True)

#Split URL Text into Words
pageTextString = ""
for each in pageText:
	pageTextString += each

pageTextString = pageTextString.split(" ")
trimmedPageText = []
for each in pageTextString:
	trimmedPageText.append(each.lower().replace("\n", " "))

#Load Name Lists
firstNameFile = open(firstNameLocation, 'r')
firstNameList = []
for each in firstNameFile:
	firstNameList.append(each)
firstNameFile.close()

lastNameFile = open(lastNameLocation, 'r')
lastNameList = []
for each in lastNameFile:
	lastNameList.append(each)
lastNameFile.close()

#Make all names lowercase
for i in range(0, len(firstNameList)):
	firstNameList[i] = firstNameList.lower()

for i in range(0, len(firstNameList)):
	lastNameList[i] = lastNameList.lower()

#Search text for names
foundList = []

for i in range(0, len(trimmedPageText)):
	if trimmedPageText[i] in firstNameList:
		if trimmedPageText[i + 1] in lastNameList:
			foundList.append(trimmedPageText[i] + " " + trimmedPageText[i + 1]

print "Search complete. " + len(foundList) + " names found."

#Exit if no names found
if len(foundList == 0):
	print "No names found. Program will now exit."
	sys.exit()

#Ready file for output
def outFileAbort(fileLocation):
	decision2 = raw_input('Do you want to write to the end of it or abort? (1/2) ')
	if str(decision2) == '1':
	try:
		outFile =  open(fileLocation, 'w')
	except IOError:
		print 'Unknown error occurred'
		sys.exit()
	elif str(decision2) == '2':
		sys.exit()
	else:
		print 'Please input 1 or 2. '
		outFileAbort(fileLocation)

def outFileExists(fileLocation):
	decision = raw_input('The output file already exists, do you want to delete it? (y/n) ')
	if str(decision) == 'y':
		os.remove(fileLocation)
	try:
		outFile = open(fileLocation, 'w')
	except IOError:
		print 'Unknown error occurred'
		sys.exit()
	elif str(decision) == 'n':
		outFileAbort(fileLocation)
	else:
		print 'Please input y or n '
		outFileExists(fileLocation)

def outFileNotExist(fileLocation):
	try:
		outFile = open(fileLocation, 'w')
	except IOError:
		print 'Unknown error occurred'
		sys.exit()

if os.path.isfile(outLocation) == True:
	outFileExists(outLocation)
elif os.path.isfile(outLocation) == False:
	outFileExists(outLocation)

#Write names
for each in foundList:
	outFile.write(each)

#Close outFile
outFile.close()

#Notify user of program completion
print "Output file has been written."
