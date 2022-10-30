import json
from torchvision import models
from flask import Flask
from torchvision.models.feature_extraction import get_graph_node_names
from torchvision.models.feature_extraction import create_feature_extractor
import os

app = Flask(__name__)

jsonpath = '/home/usuario/mc4/redcnn'

imagenet_class_index = json.load(open(os.path.join(jsonpath, './imagenet_class_index.json')))
model = models.densenet121(pretrained=True)
model.eval()

nodes, _ = get_graph_node_names(model)


feature_extractor = create_feature_extractor(
    model, return_nodes=['features.denseblock4.denselayer15.conv1'])
