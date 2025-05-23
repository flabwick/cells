#!/bin/bash
export FLASK_APP=web/app.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=6969
export PYTHONPATH=.
flask run --debug