#!/bin/bash

for route in "" "team" "car"
do
	if [[ $(curl -s -o /dev/null -w "%{http_code}" localhost:8000/$route) = 404 ]]; then
		exit 1
	fi
done
exit 0
