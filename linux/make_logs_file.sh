#!/bin/bash

FILE_TO_MONITOR="Documents/dog.txt"
LOGS_FILE="Documents/filelogs.txt"
BLOCKCHAIN_APPEND="scripts/blockchain_append.rs"

if ! command -v inotifywait &> /dev/null; then
    echo "inotify-tools is not installed, doing now"
    sudo apt-get install inotify-tools
fi

log_event() {
    EVENT=$1
    DATE=$(date ["+%M-%m-%d %H:%M:%S"])
    USER_NAME=$(whoami)
    FILE_STATE=$(cat $FILE_TO_MONITOR)
    echo "$DATE [$USER_NAME] The event $EVENT has taken place, state before changes $FILE_STATE"
}

execute_append_script_linux() {
    $BLOCKCHAIN_APPEND
}

inotifywait -m -e modify,close_write,open --format "%e" $FILE_TO_MONITOR | while read EVENT
do
    log_event $EVENT
    #execute_append_script_linux
done
