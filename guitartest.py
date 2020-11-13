# Version: 0.1.0.0 alpha

import random as r
import sys
import os
import urllib.request as ul

# Init Sys
args = sys.argv
flag_insideSet = 0

# Init functions


def update():
    if checkUpdate("./program.py") == 1:
        doUpdate()


def transVerListToInt(given_ver_list):
    for x in range(4):
        given_ver_list[x] = int(given_ver_list[x].rstrip())
    return given_ver_list


def checkProgramVersion(program_py):
    if os.path.exists(program_py) == False:
        return [0, 0, 0, 0]
    file = open(program_py)
    readingfile = file.readline()
    while readingfile:
        if readingfile[0:11] == "# Version: ":
            version = transVerListToInt(readingfile[11:].split("."))
            print("Find version " + str(version))
            break
        readingfile = file.readline()
    return version


def checkUpdate(program_py):
    # Check
    print("Checking update, please wait.")
    url = "https://raw.githubusercontent.com/OzelotVanilla/GuitarTool/main/upd"
    upd = ul.urlopen(url).readlines()[1].decode("utf-8")
    upd = transVerListToInt(upd.rstrip().split("."))
    # for i in range(4):
    #     upd[i] = int(upd[i])
    # print(upd)
    # Read the version of current program.py
    version = checkProgramVersion(program_py)
    # Check exist
    if version == [0, 0, 0, 0]:
        print("File not exist. Downloading new version.")
        return 1
    # Check whether the current version is out of date
    flag_needUpd = 0
    for x in range(len(upd)):
        if upd[x] != "rls" and upd[x] != "alpha" and upd[x] != "beta" and upd[x] != "base":
            if upd[x] > version[x]:
                flag_needUpd = 1
    print(upd)
    if flag_needUpd == 1:
        flag_doUpd = input("Need update. Input \"y\" to update.")
        if flag_doUpd == "y":
            return 1

# Need to be modified


def doUpdate():
    # Go to update
    print("Will download file.")
    url = "https://raw.githubusercontent.com/OzelotVanilla/GuitarTool/main/upd"
    ver = ul.urlopen(url).readlines()[1].decode("utf-8").rstrip()
    url = "https://raw.githubusercontent.com/OzelotVanilla/GuitarTool/main/program.py"
    print(ver)
    newVerFileName = ".temp." + str(ver) + ".py"
    ul.urlretrieve(url, newVerFileName)
    if os.path.exists("program.py") == True:
        os.remove("program.py")
    os.rename(newVerFileName, "program.py")


# Init Vars
scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
string = 0
fret = 0
opens = scale[0]
move = 0

# Define Functions


def clr():
    os.system("cls")


def FretRememberTest():
    # M

    # Music Var
    global scale, string, fret, opens, move
    while True:
        string = r.randint(1, 6)
        fret = r.randint(0, 5)
        if string == 1:
            opens = 4
        if string == 2:
            opens = 11
        if string == 3:
            opens = 7
        if string == 4:
            opens = 2
        if string == 5:
            opens = 9
        if string == 6:
            opens = 4
        move += fret + opens
        if move >= 12:
            move -= 12
        if len(scale[move]) != 1:
            print("Pass, because you ask me not to test the thing with \"#\"")
            continue
        print("String " + str(string) + " at " + str(fret))
        answer = input("Input your answer: ")
        if answer == scale[move]:
            print("OK!")
            clr()
            continue
        elif answer == "exit":
            print("Not available exit function. Type \"exit()\" instead.")
            clr()
            continue
        elif answer == "exit()":
            clr()
            print()
            break
        else:
            print("The answer is: "+scale[move])
            clr()
            continue


FretRememberTest()
