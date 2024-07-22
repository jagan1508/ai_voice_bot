import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from groq_ai import *
from stt import *
from tts import *
import base64

def autoplay_audio(file_path:str):
    print(file_path)
    with open(file_path,"rb") as f:
        data=f.read()
        b64=base64.b64encode(data).decode()
        md=f"""
        <audio controls autoplay="true">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

def main():
    st.title("AI Assistant🤖 by Jaganath")
    st.write("Please click the button which is in the box below to start speaking !!")

    stt_button = Button(label="Speak🎙️",height=65 ,width=690,button_type="primary")
    stt_button.js_on_event("button_click", CustomJS(code="""
        var recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = true;

        recognition.onresult = function(e) {
            var value = "";
            for (var i = e.resultIndex; i < e.results.length; ++i) {
                if (e.results[i].isFinal) {
                    value += e.results[i][0].transcript;
                }
            }
            if (value != "") {
                document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
            }
        }
        recognition.start();
    """))

    result = streamlit_bokeh_events(
        stt_button,
        events="GET_TEXT",
        key="listen",
        refresh_on_update=False,
        override_height=75,
        debounce_time=0
    )

    if result and "GET_TEXT" in result:
        response=generate_response(result.get("GET_TEXT"))
        text=result.get("GET_TEXT")
        print(text)
        st.caption("User: "+text)
        file=TTS(response)
        st.caption("AI: "+convert_wav_to_text())
        st.session_state['file']=file
        st.audio("output.wav",format="audio/wav")    
if __name__ == "__main__":
    main()

