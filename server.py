from flask import Flask, render_template, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

audio_file1 = 'files/source/output1.wav'
audio_file2 = 'files/source/output2.wav'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audio1')
def audio_stream1():
    return send_file(audio_file1, mimetype='audio/wav')

@app.route('/audio2')
def audio_stream2():
    return send_file(audio_file2, mimetype='audio/wav')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)