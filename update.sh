#!/bin/sh
git submodule foreach git reset --hard
git reset --hard
git pull
git submodule update
python3 translate.py
