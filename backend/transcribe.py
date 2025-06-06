import whisper
import sys

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Please provide a file path: python transcribe.py <path_to_audio_or_video_file>")
        sys.exit(1)

    path = sys.argv[1]
    output = transcribe_audio(path)
    print(output)

