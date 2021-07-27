#!/bin/sh
echo "Starting consumer"
python ./consumer/main.py

exec "$@"
