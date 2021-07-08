import pyttsx3
import datetime
import speech_recognition as sr
import tensorflow as tf
import numpy as np
from keras.preprocessing import image

#Importing model
cnn = tf.keras.models.load_model('Dog_Cat.model')

#setting up engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Speak Function
def speak(audio):
    '''

    Parameters
    ----------
    audio : String
        The string to be speek out .

    Returns
    -------
    None.

    '''
    engine.say(audio)
    engine.runAndWait()

#Wish funtion
def wishMe():
    '''
    An intial wish and info to user

    Returns
    -------
    None.

    '''
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening") 
        
    speak("I am your personal assistant How may i help You")    

#Take input 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 150
        audio = r.listen(source)
    
    try:
        print("Recognising...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said: {query}\n")  
    except Exception as e:
        speak("Say that again please")
        return "None"
    
    return query
        

def jarvis():
    wishMe()
    while True:
        query = takeCommand().lower()
        
        
        if 'predict' in query:
            speak("Predicting Results")
            path = query[len(query)-1]
            try:
                test_image = image.load_img('dataset/single_prediction/'+ path +'.jpg', target_size = (64, 64))
            except:
                test_image = image.load_img('dataset/single_prediction/'+ path +'.png', target_size = (64, 64))    
            test_image = image.img_to_array(test_image)
            test_image = np.expand_dims(test_image, axis = 0)
            result = cnn.predict(test_image)
            if result[0][0] == 1:
                prediction = 'dog'
            else:
                prediction = 'cat'
            print(prediction)    
            speak(f"According to results it is a {prediction}")    
        elif 'good' in query:
            speak('I am always there for you ...By the way thanks') 
            print('I am always there for you ...By the way thanks')
        elif 'bad' in query:
            speak('I am really sorry for wrong results   I will improve my self in future')
            print('I am really sorry for wrong results   I will improve my self in future')
        elif 'exit' in query:
            break

    
    
    
    
    
    
    
    
    
    
    
    