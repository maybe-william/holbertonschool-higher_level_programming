#!/bin/bash
# send a request with a header variable set
curl -H "X-HolbertonSchool-User-Id: 98" -sX GET "$1"
