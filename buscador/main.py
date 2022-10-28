import os
import json
from app import app, API_URL
import requests
from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from utils import allowed_file, get_closest_match
import secrets
import torch
import io