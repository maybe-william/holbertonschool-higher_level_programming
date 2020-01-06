#!/bin/bash
# Post json to a json api
curl -d "$(cat "$2")" -H "Content-Type: application/json" -X POST "$1"
