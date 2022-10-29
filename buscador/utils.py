import os
from collections import defaultdict

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

featurepath = '/home/usuario/mc4/features'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_closest_matches(features):
    results = {}
    i = 0
    for f in os.listdir(featurepath):
        i+= 1
        fname = f.split('.')[0].join('jpg')
        print(fname)
        if i == 3:
            break

get_closest_matches("hola")
