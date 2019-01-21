#!/bin/sh

python wait_for_db.py

alembic -c ccm/alembic.ini upgrade head
gunicorn --reload --bind 0.0.0.0:8000 'ccm.app:get_app()'
