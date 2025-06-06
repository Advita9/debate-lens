from pyannote.audio import Pipeline
from dotenv import load_dotenv
import os

load_dotenv()

HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token=HUGGINGFACE_TOKEN)

diarization = pipeline("../harvard.wav")

print(f"Hugging Face token loaded: {HUGGINGFACE_TOKEN[:5]}...") 

for turn, _, speaker in diarization.itertracks(yield_label = True):
    print(f"{turn.start:.1f}s - {turn.end:.1f}s: {speaker}")
