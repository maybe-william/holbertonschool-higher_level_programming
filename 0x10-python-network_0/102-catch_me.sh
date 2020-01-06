#!/bin/bash
# Catches you
curl -d "user_id=98" -H "Origin: HolbertonSchool" -sLX PUT 0.0.0.0:5000/catch_me
