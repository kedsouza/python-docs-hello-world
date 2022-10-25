from flask import Flask
from gdal import gdal

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
