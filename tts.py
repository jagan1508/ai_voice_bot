import os


from deepgram import (
    DeepgramClient,
    SpeakOptions,
)


filename = "output.wav"


def TTS(text):
    try:
        SPEAK_OPTIONS={"text":text}
        deepgram = DeepgramClient(api_key="6e65cba7408314cbe7ef8f9a3b2c4777cdf6da3f")

        options = SpeakOptions(
            model="aura-asteria-en",
            encoding="linear16",
            container="wav"
        )

        response = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
        return filename

    except Exception as e:
        print(f"Exception: {e}")


