#!/usr/bin/env python
import sys
import os
import subprocess

DryRunType = (raw_input('DryRunType: '))
cdsid = (raw_input ('Enter Your CDSID: '))
commitid = (raw_input ('Enter CommitID: '))

if DryRunType == "recheck":
    print ("Recheck on Commit: ", commitid)
    ssh -p 29421 cdsid@gotsvl1415.got.volvocars.net gerrit review -m '"!recheck"' commitid #This line has not been interpreted from shell to py
        result = $?
            if result != 0:
                print ("Commit check not executed")
elif DryRunType == "testgate":
    print ("TestGate on Commit: ", commitid)
    ssh -p 29421 cdsid@gotsvl1415.got.volvocars.net gerrit review -m '"!recheck"' commitid #This line has not been interpreted from shell to py
        resultgate = $?
            if result != 0:
                print ("Gate test not executed")
elif DryRunType == "testhourly":
    print ("TestHourly on Commit: ", commitid)
    ssh -p 29421 cdsid@gotsvl1415.got.volvocars.net gerrit review -m '"!recheck"' commitid #This line has not been interpreted from shell to py
        resulthourly = $?
            if result != 0:
                print ("Hourly dry run not executed")
else:
    print (commitid, "Not Executed")

