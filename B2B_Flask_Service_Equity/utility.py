from encryption import NewEnryption
import time
import datetime
import os

def readPropertyFile(fileName):
    propertDict={}
    try:
        with open (fileName) as m_file:
            contents=m_file.readlines()
            for prop in contents:
                propertDict[prop[0:prop.find('=')]]=prop[prop.find('=')+1:].replace("\n","")
    except Exception as er:
        print('Unable to read property File ',er)
        propertDict=None
    return propertDict



def writeLog(functionname,logstr):
    conDict=readPropertyFile('b2b.properties')
    NE= NewEnryption()
    today=str(getYYYYMMDD())
    newpath = str(NE.decryptData(conDict['LOGPATH']))
    if not os.path.isdir(newpath):
        os.makedirs(newpath)
    logfile=newpath+"/B2BLog_"+today+".log"
    datetimestr=today+"_"+str(getHHMISS())
    with open(logfile,mode="a") as myFile:
        myFile.write(datetimestr+"`"+functionname+"`"+logstr+"\n")

def getYYYYMMDD():
    now = str(datetime.datetime.now()).split(" ")
    date = now[0]
    return date.replace("-","")

def getHHMISS():
    now = str(datetime.datetime.now()).split(" ")
    time = str(now[1]).split(":")
    return time[0]+time[1]+time[2].split(".")[0]