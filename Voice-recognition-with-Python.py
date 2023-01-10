import speech_recognition as s_recognition

def main():
    r = s_recognition.Recognizer()

    with s_recognition.Microphone() as voice_source:
        r.adjust_for_ambient_noise(voice_source)
        print("Please say something...")
        audio = r.listen(voice_source)
        print("Please wait. Voice recognizing now...")

        try:
            print("You have said : \n " + r.recognize_google(audio))
            print("Your audio has been successfully recorded")

        except Exception as e:
            print("Error : " + str(e))
        
        with open ("recorded_audio.waw", "wb") as file:
            file.write(audio.get_wav_data())


if __name__ == "__main__":
    main()