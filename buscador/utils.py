import os
from collections import defaultdict
import numpy as np

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

featurepath = '/home/usuario/mc4/features'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_closest_matches(features):
    results = defaultdict()
    i = 0
    for f in os.listdir(featurepath):
        fname = f.split('.')[0]
        fname += '.jpg'
        arr = np.load(f)
        print(type(arr))
 

get_closest_matches("hola")
