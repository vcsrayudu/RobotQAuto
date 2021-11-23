import Speech as sp
import os
import subprocess
import RecordSuite as recordSuite
import GenerateScenario as generateScenario
import TrainingComand as training
import time

def run():
    while (1):
        try:
            print("\n****** YOUR IN MAIN ******\n")
            command = sp.recordVoice()
            command=command.lower()
            if "stop" in command:
                print("\n****** RobotQ Framework Stopped ******\n")
                break
            elif "run" in command:
                print("\n****** Running Robot Framework Regression ******\n")
                ms = time.time() * 1000.0
                dirname="results{0}".format(ms)
                output=os.popen("mkdir ../results/"+dirname).read()
                print(output)
                suite=command.split(" ")
                if len(suite) == 1 :
                    subprocess.call("robot -d ../results/"+ dirname+" ../suites/*.robot ")
                else:
                    subprocess.call("robot -d ../results/"+ dirname+" ../suites/"+suite[1]+".robot ")
                #  results=os.popen("robot ./suite.robot").read();
                # print(results)
                print("\n******* Completed Robot Framework Execution ******\n")
            elif "record"  in command:
                print("\n****** Record New Suite ******\n")
                recordSuite.recordSuite()
            elif "analyse"  in command:
                print("\n****** Analyze the results *******\n")
                
            elif "generate"  in command:
                print("\n****** Say Scenario Name *******\n")
                scenario = sp.recordVoice()
                print("\n****** Generate LoginScenario *******\n"+scenario)

                suite=generateScenario.generateScenario(scenario)
                recordSuite.writeToFile("LoginScenario",suite)
                print("\n****** Generate Scenario *******\n")
               
            elif "generate testdata"  in command:
                print("\n****** Generate Test Data *******\n")
                
            elif "generate test steps"  in command:
                print("\n****** Generate Test Steps *******\n")
              
            elif "training"  in command:
                print("\n****** Training the system *******\n")
                training.trainigCommands()

            elif "deploy"  in command:
                print("\n****** Deplying the Application *******\n")
            elif "download"  in command:
                print("\n****** Downloading the Application *******\n")
            elif "uninstall"  in command:
                print("\n****** Uninstalling the system *******\n")
            elif "install"  in command:
                print("\n****** Installing the system *******\n")
            
            elif "send"  in command:
                print("\n****** Sending the Mail *******\n")
            elif "compile"  in command:
                print("\n****** Compile the Program/App *******\n")
            elif "upgrade"  in command:
                print("\n****** Upgrading the system *******\n")
            elif "update"  in command:
                print("\n****** Update the system *******\n")
            elif "rollback"  in command:
                print("\n****** Training the system *******\n")
            else:
                continue
        except Exception as e:
            print(e)
            continue

run()