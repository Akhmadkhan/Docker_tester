#!/usr/bin/env bash

echo "start xvfb"
Xvfb :1 -screen 0 1024x768x16 &> xvfb.log  &

DISPLAY=:1.0
export DISPLAY

echo "run tests"

pytest --pylint --pylint-rcfile=./test/pylintrc --pep8 1> >(tee stdout.log) 2> >(tee stderr.log) 2>&1 | tee /proc/1/fd/1

rcode=$?
echo "stop xvfb"
kill "$(pgrep -f Xvfb)"
exit ${rcode}
