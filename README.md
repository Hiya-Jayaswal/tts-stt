# 🎙️ Audio Transcriber & Summarizer App

A Streamlit-based web application that lets you **record or upload audio**, transcribes it using **AssemblyAI**, identifies different speakers, and generates a clean, concise **summary** — all within a seamless and user-friendly interface.

---

## 🚀 Features

- 🎤 **Record Audio** via microphone using hotkeys:
  - Press `R` to start recording
  - Press `S` to stop recording
- 📤 **Upload Audio** in `.wav` or `.mp3` format
- 🧠 **Automatic Transcription** using [AssemblyAI](https://www.assemblyai.com/)’s advanced speech recognition
- 👥 **Speaker Diarization** (Speaker-wise segmentation)
- 📝 **Conversation Summarization** (paragraph-style summary)
- 🔍 **Expandable Views** for:
  - Full Transcript
  - Conversation Summary
  - Speaker-wise Transcript
- 📦 **Download All Files** (Transcript, Summary, Speaker-wise Transcript) as a ZIP archive

---

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)** – UI framework for building the web app
- **[AssemblyAI API](https://www.assemblyai.com/)** – Audio transcription and summarization
- **[pydub](https://github.com/jiaaro/pydub)**, **[sounddevice](https://python-sounddevice.readthedocs.io/)** – For audio recording and processing
- **Python** – Core scripting and orchestration

---

## 🧰 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Speech-Recognition-and-Summarization-Application.git
cd Speech-Recognition-and-Summarization-Application
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up Environment Variables

Create a .env file in the root directory:
```bash
API_TOKEN=your_assemblyai_api_key
MP3_FILE_PATH=output.mp3
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📂 Output Files

Upon transcription completion, the app generates and allows you to download:
- **transcript.txt** — Full conversation transcript
- **summary.txt** — Paragraph-formatted summary of the conversation
- **speaker_transcript.txt** — Speaker-wise segmented transcription

All three are conveniently packaged in a downloadable .zip file.
