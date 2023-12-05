#!/usr/bin/bash
# get the size of the body 
crul -s "$1" | wc -c 
