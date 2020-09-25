#! /bin/bash

if [[ -z "${1}" ]]; then
    NAME="idealista"
else
    NAME=${1}
fi

scrapy crawl idealista -o /data/${NAME}.csv -t csv
