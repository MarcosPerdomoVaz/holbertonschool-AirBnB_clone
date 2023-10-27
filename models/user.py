#!/usr/bin/python3
"""User man"""

from models.base_model import BaseModel


class User(BaseModel):
    """User clase pa"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
