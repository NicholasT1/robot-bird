import torch
import torchaudio
import whisper 
from datasets import load_dataset

dataset = load_dataset("/home/jupyter/novice/audio/audio_0.wav")

# audio = whisper.load_audio(audio_path)
# audio = whisper.pad_or_trim(audio)
# model = whisper.load_model("tiny").to('cuda')
# mel = whisper.log_mel_spectrogram(audio).to('cuda')
# options = whisper.DecodingOptions()
# result = whisper.decode(model, mel, options)
print(dataset)

class ASRManager:
    def __init__(self):
        # self.model = whisper.load_model("tiny.en")
        pass

    def transcribe(self, audio_bytes: bytes) -> str:
        # return self.model.transcribe(audio_bytes)
        return '';
    