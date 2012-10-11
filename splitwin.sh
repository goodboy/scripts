#!/bin/bash
# vertically split the tmux console and run the passed command in lower pane
# this script is mostly used for help docs called from vim
args="$*"

if [[ $# < 1 ]]; then
    echo "$0: FAILURE you did not pass a command to run?"
    echo "most likely opened a 'blank' tmux pane..."
elif [[ $args  =~ hoogle ]]; then
    args="$args |less"
fi

tmux split-window -v "$args"
