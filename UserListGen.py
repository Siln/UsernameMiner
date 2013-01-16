#!/usr/bin/env python

## Script: UserListGen.py
## Author: FolieADeux
## Date: 11/5/2012
## This script is intended to take a list of names and mutate
## them into a list of usernames to be used in a bruteforce test.
## Redistribute and edit as you wish.

import sys
import os

#Handle Arguments
if len(sys.argv) < 3:
  print 'Usage: ' + sys.argv[0] + ' INPUTFILE OUTPUTFILE'
	sys.exit()

#Ready file for reading
inLocation = sys.argv[1]
try:
	inFile = open(inLocation, 'r')
except IOError:
	print 'File does not exist'
	sys.exit()

#Create name list
inList = []
for each in inFile:
	inList.append(each)

#Close inFile
inFile.close()

#Create list for usernames
outList = []

#Mutate names
for each in inList:

	#Divide into first and last names
	whole = each.split()
	fname = whole[0]
	lname = whole[-1]
    
	#Mutation 1
	outList.append(fname + lname)
	outList.append(fname.lower() + lname.lower())

	#Mutation 2
	outList.append(lname + fname)
	outList.append(lname.lower() + fname.lower())

	#Mutation 3
	outList.append(fname + '.' + lname)
	outList.append(fname.lower() + '.' + lname.lower())

	#Mutation 4
	outList.append(lname + '.' + fname)
	outList.append(lname.lower() + '.' + fname.lower())

	#Mutation 5
	outList.append(fname[0] + lname)
	outList.append(fname[0].lower() + lname.lower())

	#Mutation 6
	outList.append(lname[0] + fname)
	outList.append(lname[0].lower() + fname.lower())

	#Mutation 7
	outList.append(fname[0] + '.' + lname)
	outList.append(fname[0].lower() + '.' + lname.lower())

	#Mutation 8
	outList.append(lname[0] + '.' + fname)
	outList.append(lname[0].lower() + '.' + fname.lower())

#Ready file for output
outLocation = sys.argv[2]
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

#Write mutations to file
for each in outList:
    outFile.write(each + '\n')

#Close outFile
outFile.close()

#Notify user of completion
print "File generation complete."
