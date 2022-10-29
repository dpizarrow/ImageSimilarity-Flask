from app import app
from utils import get_features
from flask import request
import io
import torch


@app.route('/redcnn', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()

        # Obtenemos las features
        deep_features = get_features(image_bytes=img_bytes)
        # deep_features es un diccionario bloque:features, pero solo usamos 1 bloque
        # (o sea, hay una sola llave).
        deep_features = list(deep_features.values())[0]
        # print(deep_features)

        # Las pasamos a bytes usando un buffer I/O
        buff = io.BytesIO()
        torch.save(deep_features, buff)
        buff.seek(0)
        return buff.read() # return buff.read()


if __name__ == "__main__":
    app.run(port=5001)
