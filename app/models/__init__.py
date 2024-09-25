from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .Color import Color
from .Model import Model
from .Owner import Owner
from .Car import Car