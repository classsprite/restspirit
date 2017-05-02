# coding: utf-8
"""
    restspirit::apis
    ``````````````
"""

import os
from flask import Blueprint, jsonify, redirect


api = Blueprint('apis',
     __name__
)

from . import login, register