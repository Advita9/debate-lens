from flask import Flask, request, jsonify
from transcribe import transcribe_audio
import os 

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    file = request.files['file']
    os.makedirs("temp", exist_ok=True)
    file_path = os.path.join("temp", file.filename)
    file.save(file_path)
    result = transcribe_audio(file_path)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)