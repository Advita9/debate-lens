import streamlit as st
import requests


st.title("Debate Lens")

uploaded_file = st.file_uploader("Upload debate video or audio", type = ["mp4", "wav"])

if uploaded_file is not None:
    st.audio(uploaded_file)
    with st.spinner("Transcribing..."):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:5000/transcribe", files = {"file": uploaded_file})
        if response.status_code == 200:
            st.success("Transcription completed yay")
            transcript = response.text
            st.text_area("Transcript", transcript, height=300)
        else:
            st.error("failed to transcribe")