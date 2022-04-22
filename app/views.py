from flask import jsonify

from app import app
from app import process_data


@app.route('/', methods=['GET'])
def index():
    return jsonify(process_data.process())
