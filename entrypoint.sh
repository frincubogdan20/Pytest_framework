#!/bin/bash
# Start virtual display for headed browser
Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99

# Run your tests
pytest -m basic_search --maxfail=1 --disable-warnings -q
