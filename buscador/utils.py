import os
from collections import defaultdict
import numpy as np
import torch
import itertools

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

featurepath = '/home/usuario/mc4/features'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_closest_matches(features):
    results = defaultdict()
    for f in os.listdir(featurepath):
        fname = f.split('.')[0]
        fname += '.jpg'
        arr = np.load(os.path.join(featurepath, f))
        arr = torch.from_numpy(arr)
        d = torch.cdist(features, arr, p=2)
        results[fname] = d
    print(results)
    results = dict(sorted(results.items(), key=lambda x:x[1]))
    top_3 = []
    for k in results:
        top_3.append(k)
    return top_3[0]
 
