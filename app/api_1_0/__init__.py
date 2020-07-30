from flask import Blueprint

api_text_label = Blueprint('text_label', __name__)
from . import text_label
