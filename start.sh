#!/bin/bash
pip install -r requirements.txt
gunicorn main:app
