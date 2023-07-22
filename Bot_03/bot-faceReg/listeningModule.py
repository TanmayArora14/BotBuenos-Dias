import multiprocessing
import speech_recognition as sr
import faceRecognitionModule
import cv2
import audioModule


def takeCommand1():
    r = sr.Recognizer()
    with sr.Microphone(0) as source:
        # r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        print(e)
        return "None"
    return query



def takeCommand():

    ct=0
    query=""

    while not("greet bot" in query or "my name is" in query or 'register me' in query or 'thank you' in query):
        print("zccvb")
        r = sr.Recognizer()

        with sr.Microphone(1) as source:
             
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source, 0, 7)
            print("Audio")

        try:
            query = r.recognize_google(audio, language='en-in')
            if query!="":
                print("NOT NULL query")
                return query
                
        except Exception as e:
            print(e)
            return "None"
    return query


def listen(frame):
    isRegistering = False
    cv2.waitKey(1)
    count = 0
    audioModule.speak("Please tell me your name")

    query = takeCommand().lower()
    if 'greet bot' in query:
        print("Give command")
        count = 0
    elif 'register me' in query:
        print("Please tell me your name")
        count = 0
    elif 'my name is ' in query:
        name = query.replace("my name is ", '')
        isRegistering = True
        count = 0
    elif '' in query:
        if count == 1:
            count = count+1
    elif 'thank you' in query:
        pass
    else:
        count = 0
    if(isRegistering == True):
            faceRecognitionModule.register_person(frame, name)
            print(name + " is registered")
            



# def listen1(frame):
#     isRegistering = False
#     cv2.waitKey(1)
#     count = 0
#     audioModule.speak("Please tell me your name")
# while True:
#     query = takeCommand().lower()
#     if 'greet bot' in query:
#         print("Give command")
#         count = 0
#     elif 'register me' in query:
#         print("Please tell me your name")
#         count = 0
#     elif 'my name is ' in query:
#         name = query.replace("my name is ", '')
#         isRegistering = True
#         count = 0
#     elif '' in query:
#         if count == 1:
#             break
#         count = count+1
#     elif 'thank you' in query:
#         break
#     else:
#         count = 0
#     if(isRegistering == True):
#             faceRecognitionModule.register_person(frame, name)
#             print(name + " is registered")
#             break


def play_videoFile(location, mirror=False):
    filePath = 'assets/' + location + '.mp4'
    cap = cv2.VideoCapture(filePath)
    cv2.namedWindow(location,cv2.WINDOW_AUTOSIZE)
    while True:
        ret_val, frame = cap.read()
        if mirror:
            frame = cv2.flip(frame, 1)
        cv2.imshow(location, frame)
        if (cv2.waitKey(5) == ord('q')):
            break
    cv2.release()
    cv2.destroyAllWindows()