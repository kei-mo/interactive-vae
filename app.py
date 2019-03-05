#app.py
from flask import Flask, request, render_template
import urllib
import numpy as np
import json

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.dates import date2num

from io import BytesIO

import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)