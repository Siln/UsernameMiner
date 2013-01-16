#!/usr/bin/env python

## Script: WebCrawler.py
## Author: FolieADeux
## Date: 1/13/2013
## This script is intended to crawl all 
## pages on a website to a specified depth,
## internal or external.
## Redistribute and edit as you wish.

import sys
import os
import urllib
import lxml.html
import time

#Handle arguments
if len(sys.argv) < 5:
    print 'USAGE: ' + sys.argv[0] + " TARGET_URL OUT_FILE SCOPE DEPTH"
    sys.exit()

if not 'http://' in sys.argv[1].lower():
    print "TARGET operator must be a full URL in the form of \'http://www.example.com\'"
    sys.exit()
else:
    target = sys.argv[1]
domain = target.split('.')[1]
outLocation = sys.argv[2]
if (sys.argv[3].lower() == 'internal'):
    scope = 'internal'
elif (sys.argv[3].lower() == 'external'):
    scope = 'external'
else:
    print "SCOPE operator must be \'internal\' or \'external\'"
    sys.exit()
depth = int(sys.argv[4])
filesFound = []

def anomalousLink(url):
    decision3 = raw_input(url + ' is an anomalous link. Would you like to delete it? (y/n) ')
    if (str(decision3) == 'y'):
  return 1
    elif (str(decision3) == 'n'):
	return 0
    else:
	print 'Please input y or n.'
	anomalousLink(url)

#Define function
def findLinks(url, scope, layer):
    linksFound = []
   
    connection = urllib.urlopen(url)
    dom = lxml.html.fromstring(connection.read())

    for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
        linksFound.append(link)

    #Add files to filesFound
    global filesFound
    for link in linksFound:
	if not 'http://' in link and not link in filesFound:
	    filesFound.append(link)

    #Filter files already found
    try:
	for link in linksFound:
	    if link in filesFound:
	        linksFound.remove(linksFound.index(link))
    except ValueError:
	time.sleep(0.00000001)

    #Ensure proper link structure
    for link in linksFound:
	if not 'http://' in link:
 	        linksFound[linksFound.index(link)] = 'http://' + domain + '.com' + '/' + link
	#Filter links if internal
	elif scope == 'internal':
	    linksFound.remove(link)
	else:
	    if anomalousLink(link) == 1:
	        linksFound.remove(link)

    #Implement recursion
    if layer > 1:
	for link in linksFound:
	    if not link.split('/')[-1] in filesFound:
	    	recLinks = findLinks(link, scope, layer - 1)
	    	for each in recLinks:
		    if not each in linksFound:
		        linksFound.append(each)

    #Let program know depth == 1
    if layer == 1:
	global depth
	depth = 1
    
    #Return results
    return linksFound    

#Find links
finalLinksFound = findLinks(target, scope, depth)
print finalLinksFound

#Ready file for output
def outFileAbort(fileLocation):
    decision2 = raw_input('Do you want to write to the end of it or abort? (1/2) ')
    if str(decision2) == '1':
        try:
            outFile =  open(fileLocation, 'w')
        except IOError:
            print 'Unknown error occurred'
            sys.exit()
        #Write output to file
        for each in finalLinksFound:
            outFile.write(each)

        #Close outFile
        outFile.close()

        #Notify user of completion
        print "Output file has been written."

        #Kill Program
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

    #Write output to file
    for each in finalLinksFound:
        outFile.write(each)

    #Close outFile
    outFile.close()

    #Notify user of completion
    print "Output file has been written."

    #Kill program
    sys.exit()

def outFileNotExist(fileLocation):
    try:
        outFile = open(fileLocation, 'w')
    except IOError:
        print 'Unknown error occurred'
        sys.exit()
    #Write output to file
    for each in finalLinksFound:
        outFile.write(each)

    #Close outFile
    outFile.close()

    #Notify user of completion
    print "Output file has been written."
    
    #Kill program
    sys.exit()

if depth == 1:
	if os.path.isfile(outLocation) == True:
	    outFileExists(outLocation)
	elif os.path.isfile(outLocation) == False:
	    outFileNotExist(outLocation)
