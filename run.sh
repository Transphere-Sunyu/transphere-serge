#!/bin/bash
while :
do
    # run the localization cycle (and rewrite the log)
    serge sync /Users/JohnCurtis/Desktop/serge/serge-1.4/bin/ > C:/Users/JohnCurtis/Desktop/serge/serge-1.4/log/serge.log 2>&1

    # clean up orphaned translation interchange files (and append to the log)
    serge clean-ts /Users/JohnCurtis/Desktop/serge/serge-1.4/bin/ >> C:/Users/JohnCurtis/Desktop/serge/serge-1.4/log/serge.log 2>&1

    echo "Waiting 10 seconds till the next cycle. Press [Ctrl+C] to stop..."
    sleep 10
done
