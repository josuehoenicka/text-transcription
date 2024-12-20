import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Di una palabra:")

    while True:
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language='es-ES')
            print(f"Encontrada: {text}")

        except sr.UnknownValueError:
            print("No se pudo entender la palabra. Intenta de nuevo")
        except KeyboardInterrupt:
            break
