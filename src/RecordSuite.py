import Speech as sp
import json
import XpathRepo as xpathRepo
#Record the test cases by suite
def recordSuite():
    suite = {"settings": {}, "variables": {},"test cases": {}}
    settingsList=["SeleniumLibrary"];
    with open('../config/config.json') as confFile:
        confObj = json.load(confFile)
    with open('./training/TrainingSuite.json') as trainingFile:
        trainingRepo = json.load(trainingFile)
    variableList={"Browser":confObj["Browser"],"Url":confObj["Url"]};
    testcaseList={};
    test=""
    remove=""
    command="command"
    
    suiteName=""
    print("\n****** New Suite Record Started ******\n")
   
    while (1):
        inputVoice = sp.recordVoice()
        inputVoice=inputVoice.lower().strip()
        remove = inputVoice      
        
        if inputVoice in "stop":
            print("\n****** New Suite Record Completed *******\n")
            break
        elif inputVoice  in "settings" or inputVoice in "variables" or inputVoice in "test cases" or inputVoice in "suite name":
            command = inputVoice
            print("\n*** Current Command ***\n "+command)
        
        elif inputVoice in  "unknownvalueerror":
            continue
        elif "name" in command:
            suiteName=""
            temp=inputVoice.split(" ");
            for tp in temp: 
                suiteName+=tp.title();
            print("\n****** New Suite Name ******\n"+suiteName)
        elif "variable" in  command:
            if "remove" in remove:
                print("\n****** Removing Last Command ******\n" +str(variableList.popitem()))
            else:
                temp=inputVoice.split(" ");
                varValue=""
                try:
                    variableName=""
                    
                    for st in temp: 
                        variableName+=st
                    print("\n****** Say Variable value for name "+variableName+" ****** \n"); 
                    varValue=sp.recordVoice()
                    variableList[variableName.title()]=trainingRepo['variables'][varValue]
                except:
                    variableList[variableName.title()]=varValue
                #variableList.add(inputVoice.title())
                #suite["variables"]=variableList
            print("\n****** Variables List *******\n " ,variableList)
        elif "setting" in command:
            #settingsList=suite["settings"]
            if "remove" in remove:
                print("\n****** Removing Last Command ******\n" +settingsList.pop())
                #settingsList.remove(lastCommand)
            else:
                try:
                    settingsList.append(trainingRepo['settings'][inputVoice])
                except:
                    settingsList.append(inputVoice.title())
                
            #suite["settings"]=settingsList
            print("\n****** Library List ******\n" ,settingsList)
        elif "test case" in command:
            lastCommand=inputVoice.title()
            if inputVoice in "steps":
                test=inputVoice
            elif "steps" in test:
                steps=testcaseList[testcase]
                if "remove" in remove:
                     print("\n****** Removing Last Command ******\n" +steps.pop())
                elif "done" in inputVoice:
                    test=""
                else:
                    steps.append(inputVoice.title());
                testcaseList[testcase]=steps
                print("\n******* Test Case Steps  ****** \n " ,testcaseList)
            else:
                if "remove" in remove:
                    print("\n****** Removing Last Testcase ******\n" +str(testcaseList.popitem()))
                    try:
                        testcase=list(testcaseList.keys())[-1];
                    except:
                        pass
                elif " " in inputVoice:
                    testcase=inputVoice.title()
                    #testcaseList=suite["test cases"]
                    steps=[]
                    if testcaseList:
                        try:
                            #print("steps: " ,testcases)
                            steps=testcaseList[testcase]
                        except:
                            steps=[]
                    testcaseList[testcase]=steps;
                    #suite["test cases"]=testcaseList
                print("\n****** Test Case List ******\n" ,testcaseList)
        else:
            continue;
    suite["variables"]=variableList
    suite["settings"]=settingsList
    suite["testcases"]=testcaseList
    del variableList
    del settingsList
    del testcaseList
    if suiteName not in "":
        writeToFile(suiteName,suite)
    else:
         print("\n****** Suite Name is empty, Default Suite file is default.robot ******\n")
         writeToFile("default",suite)
    
def writeToFile(suiteName,suite):
    #New suite is writing to the file
    f = open("../suites/"+suiteName+".robot", "w+")
    print("\n******* Writing to Suite file at location *******\n"+"../suites/"+suiteName+".robot")
    with open('./training/TrainingSuite.json') as trainingFile:
        trainingRepo = json.load(trainingFile)
    try:
        with open('../page/'+suiteName+'.json') as xpathFile:
            xpathRepo = json.load(xpathFile)
    except:
        with open('../page/xpath.json') as xpathFile:
            xpathRepo = json.load(xpathFile)
    for library in suite:
        if library in "settings":
            f.write("*** Settings ***" )
            for libEntry in suite[library]:
                 f.write("\nLibrary  " + libEntry)
        if library in "variables":
            f.write("\n*** Variables ***")
            for variable in suite[library]:
                f.write("\n${" + variable.title()+"}  "+suite[library][variable].title())
        if library in "testcases":
            f.write("\n*** Test Cases ***")
            for testcase in suite[library]:
                f.write("\n" + testcase.title())
                f.write("\n\t"+trainingRepo['steps']["Open Browser"])
                for steps in suite[library][testcase]:
                    try:
                        step=steps.split(" ")
                        if "Input" in step[0]:
                            try:
                                f.write("\n\tInput Text  xpath="+xpathRepo[step[1]]+"  "+step[2].title())
                            except:
                                f.write("\n\tInput Text  xpath="+step[1]+"  "+step[2].title())
                        elif "Click" in step[0]:
                            try:
                                f.write("\n\tClick Element  xpath="+xpathRepo[step[1]])
                            except:
                                f.write("\n\tClick Element  xpath="+step[1])
                        else:
                            f.write("\n\t"+trainingRepo['steps'][steps.title()])
                    except:
                        f.write("\n\t"+steps.title())
                f.write("\n\t"+trainingRepo['steps']["Close Browser"])   
    print("\n******* New Suite Created Succesfully *******\n")
    del suite
    
    f.close()

#recordSuite()
