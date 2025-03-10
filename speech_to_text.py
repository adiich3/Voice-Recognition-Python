import speech_recognition as sr
import pyttsx3
print("Listening...")
r = sr.Recognizer()

def record_text():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                return MyText.lower()  # Transformă textul în litere mici pentru verificări simple
        except sr.UnknownValueError:
            print("Unknown error, please try again.")

def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")

while True:
    text = record_text()
    if text == "stop":  # Dacă utilizatorul spune "stop", programul se oprește
        print("Exiting program.")
        break
    output_text(text)
    print("Spoken text:", text)
