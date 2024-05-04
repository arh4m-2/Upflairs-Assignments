import speech_recognition as sr

r=sr.Recognizer()
print(sr.Microphone.list_microphone_names())

with sr.Microphone() as Source:
    r.adjust_for_ambient_noise(Source)
    print('say>>Kuch Bolo')
    audio=r.listen(Source)
    text=r.recognize_google(audio)
    print('ye bola aapne', text)