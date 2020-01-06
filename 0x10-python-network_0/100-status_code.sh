#!/bin/bash
# Print only the code
curl -o /dev/null -sw "%{http_code}" "$1"
