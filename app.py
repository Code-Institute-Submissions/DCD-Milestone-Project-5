import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
