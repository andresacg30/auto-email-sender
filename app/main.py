from flask import Flask, render_template, request, flash, redirect
from app.script.emails import send_email
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 
UPLOAD_FOLDER = os.fsdecode("app/script/Enviar")
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        files = request.files.getlist("file[]")
        for file in files:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        flash('Se subieron tus archivos correctamente')
        return redirect('/')


@app.route("/send", methods=["GET", "POST"])
def send():
    send_email()
    return render_template("send.html")

