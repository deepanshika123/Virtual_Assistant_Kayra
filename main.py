import requests
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI


recognizer=sr.Recognizer
engine= pyttsx3.init()
newsapi="ceab44eec7704961809ec89428176b1b"

def speak(text):
    engine.say(text)
    engine.runAndWait()


def aiProcess(command):
   client = OpenAI(
    api_key="=============",
)

   completion = client.chat.completions.create(
    model = "gpt - 3.5-turbo",
    messages=[
        {
            "role": "system" , "content":"You are a virtual assistant named kayra skilled in general tasks like alexa and google cloud"},
        { "role" : "user" , "content": command   }     
        
    ]
    )

   return completion.choices[0].message.content



def processcommand(c):
   if "open google " in c.lower():
      webbrowser.open("https://google.com")
   elif "open facebook" in c.lower():
      webbrowser.open("https://facebook.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
   elif "open linkedin" in c.lower():
      webbrowser.open("https://linkedin.com")
   elif c.lower().startswith("play"):
      song = c.lower(). split(" ")[1]
      link=musiclibrary.music[song]
      webbrowser.open(link)

   elif "news" in c.lower():
      r= requests.get(f"https://newsapi.org/v2/top-headlines/sources?apiKey={newsapi}")
      if r.status_code == 200:
         data= r.json()

      articles = data.get('articles ' ,[])

      for article in articles:
         speak(article['title'])


   else:
      output = aiProcess(c)
      speak(output)


   

if __name__== "__main__":
    speak("Initializing Kayra.....")
while True:
      #lishen for the wake word "Kayra"
       # obtain audio from the microphone
    r = sr.Recognizer() 
    print("recognizing...")
    try:
       with sr.Microphone() as source:
        print("Lishening....")
        audio = r.listen(source , timeout=2 , phrase_time_limit=1)
        word = r.recognize_google(audio)
        if(word.lower() == "Kayra"):
           speak("Ya")
           #listen for command
           with sr.Microphone() as source:
             print("Kayra Active...")
             audio = r.listen(source )
             command = r.recognize_google(audio)

             processcommand(command)

    except Exception as e:
     print("Error; {0}".format(e))

