#!/bin/sh

# this script will run speedtest and route the output to a logfile

speedtest -f tsv >> /var/log/speedtest/speedtest.txt

# add timestamp

sed -i "$ s/$/\t$(date "+%Y-%m-%d %T")/" /var/log/speedtest/speedtest.txt
