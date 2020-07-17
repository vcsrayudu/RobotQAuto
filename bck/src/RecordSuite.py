import Speech as sp
#Record the test cases by suite
def recordSuite():
    suite = {"settings": {}, "variables": {},"test cases": {}}
    settingsList=[];
    variableList=[];
    testcaseList={};
    test=""
    remove=""
    command="command"
    print("****** New Suite Record Started ******")
    while (1):
        inputVoice = sp.recordVoice()
        inputVoice=inputVoice.lower().strip()
        remove = inputVoice      
        
        if inputVoice in "stop":
            print("\n****** New Suite Record Completed *******\n")
            break
        elif inputVoice  in "settings" or inputVoice in "variables" or inputVoice in "test cases":
            command = inputVoice
            print("\n*** Current Command ***\n "+command)
        elif inputVoice in  "unknownvalueerror":
            continue
        elif "variable" in  command:
            if "remove" in remove:
                print("\n****** Removing Last Command ******\n" +variableList.pop())
            elif " " in inputVoice:
                variableList.add(inputVoice.title())
                #suite["variables"]=variableList
            print("\n****** Variables List *******\n " ,variableList)
        elif "setting" in command:
            #settingsList=suite["settings"]
            if "remove" in remove:
                print("\n****** Removing Last Command ******\n" +settingsList.pop())
                #settingsList.remove(lastCommand)
            elif "selenium" in inputVoice:
                inputVoice="SeleniumLibrary"
                settingsList.append(inputVoice)
            else:
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
    suite["test cases"]=testcaseList
    del variableList
    del settingsList
    del testcaseList
    writeToFile(suite)
    
def writeToFile(suite):
    #New suite is writing to the file
    f = open("../suites/suite1.robot", "w+")
    print("\n******* Writing to Suite file *******\n")
    for library in suite:
        if library in "settings":
            f.write("*** Settings ***" )
            for libEntry in suite[library]:
                 f.write("\nLibrary  " + libEntry)
        if library in "variables":
            f.write("\n*** Variables ***")
            for variable in suite[library]:
                variables = variable.split(" ")
                f.write("\n${" + variables[0].title()+"}  "+variables[1].title())
        if library in "test cases":
            f.write("\n*** Test Cases ***")
            for testcase in suite[library]:
                f.write("\n" + testcase.title())
                for steps in suite[library][testcase]:
                    f.write("\n\t"+steps.title())
    print("\n******* New Suite Created Succesfully *******\n")
    del suite
    
    f.close()

recordSuite()
