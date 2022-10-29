import os
import json
from app import app
import requests
from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from utils import allowed_file

@app.route('/')
def index_form():
    return render_template('index.html')