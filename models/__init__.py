#!/usr/bin/env python3
"""__init__ magic method initializes the package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
