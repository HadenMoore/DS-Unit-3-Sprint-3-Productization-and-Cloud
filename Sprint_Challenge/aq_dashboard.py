# Part 1: If I could put Flask in a File:
#Importing Packages:
#Importing Python Wrapper for the API:
#Importing flask_sqlalchemy for Part 3:
"""OpenAQ Air Quality Dashboard with Flask."""
import openaq
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)


@APP.route('/')
def root():
    """Base view."""
    return 'TODO - part 2 and beyond!'
