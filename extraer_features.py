from pathlib import Path
import io
import torchvision.transforms as transforms
from PIL import Image
from torchvision.models.feature_extraction import create_feature_extractor
from torchvision import models
import os

dir = '/media/disco-compartido/mc4/catalogo'

def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(255),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)


model = models.densenet121(pretrained=True)
model.eval()

feature_extractor = create_feature_extractor(
    model, return_nodes=['features.denseblock4.denselayer15.conv1'])


def get_features(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    out = feature_extractor(tensor)
    return out

for file in os.listdir(dir):
    with open(os.path.join(dir, file), 'rb') as imagen:
        imagen = imagen.read()
        image_bytes = transform_image(imagen)
        features = list(get_features(image_bytes = image_bytes).values())[0]
        features = features.numpy()
        features.save(os.path.join('features', file.split('.')[0] + '.npy'))



