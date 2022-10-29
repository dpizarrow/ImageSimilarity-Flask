import os

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

featurepath = '/home/usuario/mc4/features'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_closest_matches(features):
    for f in os.listdir(featurepath):
        print(f)

get_closest_matches("hola")
