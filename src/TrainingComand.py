import Speech as sp
import json
#import XpathRepo as xpathRepo
#Record the test cases by suite
def trainigCommands():
    print("\n****** Loading existing commands ******\n")
    with open('./training/TrainingSuite.json') as trainingFile:
        trainingRepo = json.load(trainingFile)
    steps=trainingRepo["steps"]
    print("\n****** Training the system Started ******\n")
    while (1):
        
        inputVoice = sp.recordVoice()
        inputVoice=inputVoice.lower().strip()
        print("\n*** Input Command ***\n "+inputVoice)
        if inputVoice in "stop":
            trainingRepo["steps"]=steps
            with open("./training/TrainingSuite.json", "w") as outfile: 
                json.dump(trainingRepo, outfile) 
            print("\n****** Training Completed *******\n")
            break
        elif inputVoice in  "unknownvalueerror":
            continue
        elif " " not in inputVoice:
            command = inputVoice.title()
            value=""   
            while (1):
                print("\n*** Say value for Command ***\n "+command)
                speach = sp.recordVoice()
                print("\n*** Current Value ***\n "+value)
                if speach in "done":
                    print("\n****** Proper value Completed *******\n"+value)
                    break
                elif speach in  "unknownvalueerror":
                    continue
                elif " " in speach :
                    value=speach.title() 

            steps[command]=value
            print("\n****** List *******\n",trainingRepo)