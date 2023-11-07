from flask import Flask, render_template, request, send_file
from text_to_speech import text_to_speech

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        mp3_fp = text_to_speech(text)
        return send_file(
            mp3_fp,
            mimetype="audio/mpeg",
            as_attachment=False,
            download_name="speech.mp3"
        )

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
