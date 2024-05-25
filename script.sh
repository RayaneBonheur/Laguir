#!/bin/bash

KEYSPACE="LAGUIRCAS"

for json in $(find /app -name *.json); do
    iconv -f original_encoding -t utf-8 $json -o $json
    TABLE=$(echo $json | sed 's@/@@g')

    echo "USE $KEYSPACE;" > insert.cql

    jq -c '.[]' $json | while read row; do
        echo "INSERT INTO $KEYSPACE.$TABLE JSON '$row';" >> insert.cql
    done
done



cqlsh -f insert.cql