import Speech as sp
import os
import subprocess
import RecordSuite as recordSuite
import time;

def run():
    while (1):
        try:
            print("\n****** YOUR IN MAIN ******\n")
            command = sp.recordVoice()
            command=command.lower()
            if "stop" in command.lower():
                print("\n****** RobotQ Framework Stopped ******\n")
                break
            elif "run" in command:
                print("\n****** Running Robot Framework Regression ******\n")
                ms = time.time() * 1000.0
                dirname="results{0}".format(ms);
                output=os.popen("mkdir ../results/"+dirname).read()
                print(output)
                subprocess.call("robot -d ../results/"+ dirname+" ../suites/*.robot ")
                #  results=os.popen("robot ./suite.robot").read();
                # print(results)
                print("\n******* Completed Robot Framework Execution ******\n")
            elif "record"  in command:
                print("\n****** Record New Suite ******\n")
                recordSuite.recordSuite()
            elif "analyse"  in command:
                print("\n****** Analyze the results *******\n")
                pass
            else:
                continue;
        except:
            continue;

run()