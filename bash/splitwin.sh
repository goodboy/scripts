#!/bin/bash
# vertically split the tmux console and run the passed command in lower pane
# this script is mostly used for help docs called from vim
args="$*"
declare -i lines=1
# shopt -s checkwinsize

if [[ $# < 1 ]]; then

    echo "$0: FAILURE you did not pass a command to run?"
    echo "most likely opened a 'blank' tmux pane..."

elif [[ $args  =~ hoogle ]]; then

    # output="$($args)"
    # while read line; do
    #     if [[ $line =~ "\n" ]]; then
    #         lines=+1
    #     fi
    #     if (( $lines > 26 )); then
    #         lines= 26
    #         break
    #     fi
    # done <<< $output
    args="$args |less"

    # echo "output = $output"
    # echo "and is $lines lines long"

    # tmux split-window -l $lines -v "less <<< $output"
# fi
    tmux split-window -l 15 -v "$args"
fi
