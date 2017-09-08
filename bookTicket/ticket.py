import aiml
import os
k=aiml.Kernel()
if os.path.isfile("standards.brn"):
    k.bootstrap(brainFile="standards.brn")
else:
    k.bootstrap(learnFiles="std-startup.xml",commands="LOAD AIML B")
while True:
    cmd=input(">>")
    if cmd=="quit":
        exit()
    else:
        print(k.respond(cmd))
        if ((cmd) == "thank you"):
            exit()