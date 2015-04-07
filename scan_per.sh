#!/bin/sh
TARGETS="-iL target_list.txt"
OPTIONS="-v -T4 --top-ports 1000"
date=`date +%F+%R`
cd /root/scans
nmap $OPTIONS $TARGETS -oA scan-$date > /dev/null
if [ -e scan-prev.xml ]; then
    ndiff scan-prev.xml scan-$date.xml > diff-$date
    echo "*** NDIFF RESULTS ***"
    cat diff-$date
    echo
fi
echo "*** NMAP RESULTS ***"
#cat scan-$date.nmap
ln -sf scan-$date.xml scan-prev.xml
#python sendmail.py diff-$date >> sendmail.log
python nmap_call_hydra.py $date scan-$date.xml
