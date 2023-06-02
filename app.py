from flask import Flask, after_this_request, render_template, send_file
import vidgen
import random
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/getvid/")
def get_vid():
    while True:
        try:
            vidgen.vidgen()
            break
        except Exception as e:
            print("Trying again")
    try:
        return send_file('out.mp4')
    except Exception as e:
        return str(e)
