#!/bin/bash
# vertically split the tmux console and run the passed command in lower pane
if [[ $# < 1 ]]; then
    echo "$0: FAILURE you did not pass a command to run?"
    echo "most likely opened a 'blank' tmux pane..."
fi

tmux split-window -v "$*"
