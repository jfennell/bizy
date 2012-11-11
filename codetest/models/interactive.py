"""
Easy setup to get an interactive db session.
"""
from codetest import models

models.setup_model()
session = models.Session()
