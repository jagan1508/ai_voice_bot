import speech_recognition as sr

def convert_wav_to_text():
    wav_file_path="output.wav"
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Google Web Speech API could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Web Speech API; {e}"

