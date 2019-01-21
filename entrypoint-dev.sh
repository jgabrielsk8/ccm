#!/usr/bin/env bash
# install any dependencies
alembic -c ccm/alembic.ini upgrade head
gunicorn --reload --bind 0.0.0.0:8000 'ccm.app:get_app()'
