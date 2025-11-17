#!/bin/sh
set -e
cd brendonmay.github.io
git reset --hard
cd ..
git reset --hard
git pull
git submodule update
python3 translate.py
