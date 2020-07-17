import speech_recognition as sr

def recordVoice():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("******** Waiting for Input = ")
        audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
        try:
            command = r.recognize_google(audio);
            print("****  YOUR INPUT **** \n" + command)

            return command
        except sr.UnknownValueError:
            #print("Speech Recognition could not understand audio")
            #recordVoice()
            return "UnknownValueError"
        except sr.RequestError as e:
            #print("Could not request results from Speech Recognition service; {0}".format(e))
            #recordVoice()
            return "UnknownValueError"

