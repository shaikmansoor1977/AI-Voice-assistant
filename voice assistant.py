#below all the import section part is given
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
from openai import OpenAI


# Function to change voice (Male/Female)
def set_voice(voice_type="male"):
    voices = engine.getProperty("voices")
    if voice_type == "female":
        engine.setProperty("voice", voices[1].id)  # Female Voice
    else:
        engine.setProperty("voice", voices[0].id)  # Male Voice

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
     engine.say(text)
     engine.runAndWait()

#from the below code you can switch between male and female voices
set_voice("female")

#intigrated with openai
def aiprocess(command):
     client = OpenAI( 
    api_key="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",)


     completion = client.chat.completions.create(
     model="gpt-4o-mini",
     messages=[
          {"role": "system", "content": "You are a helpful virtual assistant named jarvis skilled in genral task like alexa and google. give short answers"},
          {
               "role": "user",
               "content": command
          }
     ]
     )

     return completion.choices[0].message.content


# this below code related to opening links & librarys and my personal qustions
def processcommand(c):
    if "open google" in c.lower():
         webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
         webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
         webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "what is my name" in c.lower():
         speak("your name is mansoor")

    elif "what is my father name" in c.lower():
         speak("your father name is khaadhar basha")

    elif "my degree completion year" in c.lower():
         speak("you completed your degree in 2025")

    elif "do i have any friends" in c.lower():
         speak(" yes sir you have a couple of friends and there names are santhosh,rohan,sai")

    elif "what is my favourite colour" in c.lower():
         speak(" you have four favourite colors sir and they are blue,green,pink and finally yellow ")


#let openai handle request
    else: 
        output=aiprocess(c)
        speak(output)
    

 
        

    
speak("allow me to introduce my self..... my name is jarvis...... i am a virtual assistent.......welcome back sir")
while True:
                    #listen for the wake word
                # obtain audio from the microphone
            
    r = sr.Recognizer()
            
                # recognize speech using google
    print("recognizing")    
    try:
        with sr.Microphone() as source:
            print("Listening........")
            audio = r.listen(source,timeout=8,phrase_time_limit=5)
        word=r.recognize_google(audio)
        if (word.lower()== "jarvis"):
            speak("yes")

            with sr.Microphone() as source:
                print("listening command...")
                audio = r.listen(source)
                command=r.recognize_google(audio)
                processcommand(command)
              

                                    
    except Exception as e:
         print("Error; {0}".format(e))

