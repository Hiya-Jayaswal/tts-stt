import streamlit as st
import os
import io
from record_audio import record_audio_to_mp3
from utils import upload_file, create_labelled_transcript, create_summary
from dotenv import load_dotenv
import zipfile

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

speaker_colors = [
    "#FF6B6B",  # Red
    "#4ECDC4",  # Teal
    "#FFD93D",  # Yellow
    "#1A535C",  # Dark Blue
    "#FF9F1C",  # Orange
]

st.set_page_config(page_title="Audio Transcriber & Summarizer", layout="centered")
st.title("🎙️ Audio Transcriber & Summarizer App")

st.markdown("Record or upload audio, get transcription & summary instantly!")

# Record Audio Section
st.header("1. Record Audio")
st.info("Press 'R' to start recording. Press 'S' when finished.")
if st.button("Start Recording"):
    record_audio_to_mp3("output.wav")
    st.success("Recording complete! Saved as output.wav")

# Upload Audio Section
st.header("2. Or Upload Audio")
uploaded_file = st.file_uploader("Upload your audio file (.wav, .mp3)", type=["wav", "mp3"])

if uploaded_file is not None:
    with open("uploaded_audio.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("Audio uploaded successfully!")

# Transcription & Summarization
st.header("3. Transcribe & Summarize")

if st.button("Process Audio"):
    audio_path = "output.wav" if uploaded_file is None else "uploaded_audio.wav"

    with st.spinner("Uploading audio..."):
        audio_url = upload_file(API_TOKEN, audio_path)

    with st.spinner("Transcribing audio..."):
        transcript = create_labelled_transcript(API_TOKEN, audio_url)

    with st.spinner("Generating summary..."):
        summary = create_summary(API_TOKEN, audio_url)

    with st.expander("Transcript", expanded=False):
        st.write(transcript['text'])
        
    transcript_text = transcript['text']
    
    st.markdown("---")  
    st.subheader("Speaker-wise Transcript")

    speaker_transcript_text = ""
    
    for idx, utterance in enumerate(transcript['utterances']):
        speaker = utterance['speaker']
        text = utterance['text']
        confidence = utterance['confidence']
        
        speaker_index = ord(speaker[-1].upper()) - ord('A')
        
        color = speaker_colors[speaker_index % len(speaker_colors)]
        
        speaker_transcript_text += f"Speaker {speaker}:\n{text}\nConfidence: {confidence}\n\n"

        with st.expander(f"Speaker {speaker}", expanded=True):
            st.markdown(
                f"<h5 style='color:{color};'>Speaker {speaker}</h5>", 
                unsafe_allow_html=True)
            st.write(text)
            st.caption(f"Confidence: {confidence}")
    
    st.markdown("---")
    
    with st.expander("Summary", expanded=False):
        st.write(summary['summary'])
        
    summary_text = summary['summary'] 
        
    st.markdown("---")
    
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        zip_file.writestr("transcript.txt", transcript_text)
        zip_file.writestr("summary.txt", summary_text)
        zip_file.writestr("speaker_transcript.txt", speaker_transcript_text)

    zip_buffer.seek(0)  

    st.download_button(
        label="Download All Files (ZIP)",
        data=zip_buffer,
        file_name="transcription_files.zip",
        mime="application/zip"
    )
    