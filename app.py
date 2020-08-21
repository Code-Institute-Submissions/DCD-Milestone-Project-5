# imports
import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

# creating flask instance
app = Flask(__name__)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)  # remove debug for release version
