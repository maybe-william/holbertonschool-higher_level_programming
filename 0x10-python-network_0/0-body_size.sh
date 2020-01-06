#!/bin/bash
# This script shows the body size of a response
curl -o /dev/null -sw "%{size_download}\n" "$1"
