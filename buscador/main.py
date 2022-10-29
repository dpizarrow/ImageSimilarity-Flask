import os
import json
from app import app
import requests
from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from utils import allowed_file

@app.route('/')
def index_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_image():
    if 'file' not in request.files:
        error = 'No se envió ningún archivo'
        return render_template('index.html', error=error)
    file = request.files['file']
    if file.filename == '':
        error = 'No se seleccionó ningún archivo'
        return render_template('index.html', error=error)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        files = {'file': open(filepath, 'rb')}
        apicall = requests.post('http://127.0.0.1:5001/predict', files=files)
        if apicall.status_code == 200:
            error = None
            pass
    else:
        error = 'Archivo no permitido. Solo se permite JPG, JPEG o PNG.'
        return render_template('index.html', error=error)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run(port=5000)