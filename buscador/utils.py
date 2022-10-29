import os

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

featurepath = 'features'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_closest_matches(features):
    print(os.getcwd())

get_closest_matches("hola")
