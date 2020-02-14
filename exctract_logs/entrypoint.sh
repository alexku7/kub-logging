#!/bin/bash


python /etc/extracter.py &
nginx -g "daemon off;"

