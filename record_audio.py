import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from pydub import AudioSegment
import keyboard
import os
from dotenv import load_dotenv
load_dotenv()

def record_audio_to_mp3(output_filename="output.mp3"):
    """
    Records audio using the microphone and saves it as an MP3 file.

    Press 'r' to start recording, and 's' to stop and save.

    Args:
        output_filename (str): Filename to save the MP3 as.
    """
    fs = 44100
    channels = 1
    is_recording = False
    recording_data = []

    
    os.environ["PATH"] += os.pathsep + os.getenv("FFMPEG_PATH")

    def callback(indata, frames, time, status):
        nonlocal recording_data
        if is_recording:
            recording_data.append(indata.copy())

    print("Press 'r' to start recording, 's' to stop and save as MP3.")

    stream = sd.InputStream(samplerate=fs, channels=channels, callback=callback)

    with stream:
        while True:
            if keyboard.is_pressed('r') and not is_recording:
                print("🎙️  Recording started...")
                recording_data = []
                is_recording = True
                sd.sleep(500)

            elif keyboard.is_pressed('s') and is_recording:
                print("🛑 Recording stopped. Saving...")
                is_recording = False
                sd.sleep(500)

                audio_np = np.concatenate(recording_data, axis=0)

                # Save to temp WAV file
                tmp_wav_path = "temp_audio.wav"
                wav.write(tmp_wav_path, fs, audio_np)

                # Convert WAV to MP3
                print("WAV file exists?", os.path.exists(tmp_wav_path))
                print("WAV path:", tmp_wav_path)

                sound = AudioSegment.from_wav(tmp_wav_path)
                sound.export(output_filename, format="mp3")

                os.remove(tmp_wav_path)
                print(f"✅ Saved as '{output_filename}'")
                break
