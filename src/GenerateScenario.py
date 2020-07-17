import os
import json

def generateScenario(suiteName):
    suite = {"settings": {}, "variables": {},"testcases": {}}
    settingsList=["SeleniumLibrary"];
    variableList={}
    print("\n****** Scenario Generation Started ******\n")
    with open('../config/config.json') as confFile:
        confObj = json.load(confFile)
    variableList["Browser"]=confObj['Browser']
    variableList["Url"]=confObj['Url'];
    print("\n****** Variable List ******\n",variableList)
    
    with open('../test/'+suiteName+'.json') as suiteFile:
        suiteObj = json.load(suiteFile)
    testcaseList=suiteObj['testcaseList']
    print("\n****** Testcases List ******\n",testcaseList)
    
    for variable in suiteObj['variableList']:
        variableList.append(variable)
    print("\n****** Variable List ******\n",variableList)
   
    for library in suiteObj['settingsList']:
        settingsList.append(library)
       
    print("\n****** Settings List ******\n",settingsList)
    suite['settings']=settingsList
    suite['variables']=variableList
    suite['testcases']=testcaseList
    return suite
    
    