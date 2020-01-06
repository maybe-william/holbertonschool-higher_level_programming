#!/bin/bash
# request all http verbs available
curl -sIX OPTIONS "$1" | grep -Po "(?<=Allow: ).*"
