"""
Easy setup to get an interactive db session.
"""
import codetest.models

codetest.models.setup_model()
session = codetest.models.Session()
