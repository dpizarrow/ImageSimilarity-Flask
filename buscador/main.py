import os
import json
from app import app, API_URL
import requests
from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from utils import allowed_file, get_closest_matches
import secrets
import torch
import io

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
        # hash para evitar sobreescribir
        filename = secrets.token_hex(nbytes=8) + '_' + secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        files = {'file': open(filepath, 'rb')}
        apicall = requests.post(API_URL, files=files)
        if apicall.status_code == 200:
            error = None
            features = torch.load(io.BytesIO(apicall.content))
            closest_filename = get_closest_matches(features)
            print(closest_filename)
            result = {'closest_filename_1': closest_filename[0], 'closest_filename_2': closest_filename[1], 'closest_filename_3': closest_filename[2]}
        else:
            error = 'Error al procesar la imagen'
            result = None
        return render_template('index.html', filename=filename, result=result, error=error)
    else:
        error = 'Archivo no permitido. Solo se permite JPG, JPEG o PNG.'
        return render_template('index.html', error=error)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/results/<filename>')
def display_results(filename):
    return redirect(url_for('static', filename='catalogo/' + filename), code=301)


if __name__ == "__main__":
    app.run(port=5000)
