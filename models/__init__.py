#!/usr/bin/python3
"""
create a unique FileStorage instance
"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
