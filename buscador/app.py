from flask import Flask

#UPLOAD_FOLDER = 'static/uploads/'
UPLOAD_FOLDER = '/home/usuario/mc4/buscador/static/uploads/'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
#API_URL = 'http://127.0.0.1:5001/redcnn-mc4'
API_URL = 'http://127.0.0.1/redcnn-mc4'
