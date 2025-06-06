from pyannote.audio import Pipeline

pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization", use_auth_token="REMOVED")

diarization = pipeline("../harvard.wav")

for turn, _, speaker in diarization.itertracks(yield_label = True):
    print(f"{turn.start:.1f}s - {turn.end:.1f}s: {speaker}")