#!/bin/bash
# Send a POST request with email subject set with values
curl -sd "email=hr%40holbertonschool%2Ecom&subject=I+will+always+be+here+for+PLD" "$1"
