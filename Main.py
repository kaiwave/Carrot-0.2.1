dbfper = 0
unlock = 0
pswdatmtnum = 0
passfile1 = open("passfile.txt","r")
passfile = passfile1.read()
username1 = open("username.txt","r")
username = username1.read()
import os
from time import sleep
while dbfper <= 100:
    print("Loading Database Files:", dbfper, "%")
    lineloadout = 0
    while lineloadout <= 2:
        print("") ; sleep(0.125)
        lineloadout = lineloadout + 1
    dbfper = dbfper + 6.25
intper = 0
while intper <= 100:
    print("Loading Initialisation Data", intper, "%")
    lineloadout = 0
    while lineloadout <= 2:
        print("") ; sleep(0.05)
        lineloadout = lineloadout + 1
    intper = intper + 6.25
print("")
print(" __  ____  _") ; sleep(0.2)
print("/     |    |") ; sleep(0.2)
print("\     |    |") ; sleep(0.2)
print(" --   |    -") ; sleep(0.2)
print("") ; sleep(0.2)
print("© Carrot Tech Industries") ; sleep(0.2)
print("A sub division of Yetroll®") ; sleep(0.2)
print("Loading cOS 0.2.1...") ; sleep(2)
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("User:", username)
while unlock == 0:
    if passfile == "null":
        input("Press Enter")
        unlock = 1
    else:
        if pswdatmtnum <=5:
            pswdatmt = input("Enter Password")
            if pswdatmt == passfile:
                unlock = 1
            else:
                unlock = 0
                pswdatmtnum = pswdatmtnum + 1
                print(pswdatmtnum, "Atterpts")
        else:
            countdn = 60
            while countdn >= 0:
                print("Login is disabled, try again in", countdn, "seconds.")
                countdn = countdn - 1
                sleep(1)
            countdn = 60
print("Welcome to cOS 0.2.1")
while not 0 == 1:
    commandinput = input("Enter Commands:")
    if commandinput == "/help":
        print("For entertainment, use /entertainment")
    if commandinput == "/entertainment":
        os.startfile("Entertainment.py")