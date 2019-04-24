#!/bin/sh
# set -x

keyboard_map () {
    # apply keyboard re-maps
    setxkbmap -option caps:ctrl_modifier
}


# get display names
EXT=`xrandr --current | sed 's/^\(.*\) connected.*$/\1/p;d' | grep -v ^eDP | head -n 1`
echo "EXT is '$EXT'"
INT=`xrandr --current | sed 's/^\(.*\) connected.*$/\1/p;d' | grep -v ^DP | head -n 1`
echo "INT is '$INT'"

function extend() {
    # extend non-HiDPI external display on DP* above HiDPI internal display eDP*
    # see also https://wiki.archlinux.org/index.php/HiDPI
    # you may run into https://bugs.freedesktop.org/show_bug.cgi?id=39949
    #                  https://bugs.launchpad.net/ubuntu/+source/xorg-server/+bug/883319

    # get dimensions
    ext_w=`xrandr | sed 's/^'"${EXT}"' [^0-9]* \([0-9]\+\)x.*$/\1/p;d'`
    echo "ext_w is '$ext_w'"
    ext_h=`xrandr | sed 's/^'"${EXT}"' [^0-9]* [0-9]\+x\([0-9]\+\).*$/\1/p;d'`
    echo "ext_h is '$ext_h'"
    int_w=`xrandr | sed 's/^'"${INT}"' [^0-9]* \([0-9]\+\)x.*$/\1/p;d'`
    echo "int_w is '$int_w'"
    off_w="$(echo $(( ($int_w-$ext_w) / 2 )) | sed 's/^-//')"
    echo "off_w is '$off_w'"

    # xrandr --output "${INT}" --auto --pos ${off_w}x${ext_h} --scale 1x1  --output "${EXT}" --auto --scale 2.3x2.3 --pos 0x0
    # xrandr --output "${INT}" --pos ${off_w}x${ext_h} --auto --scale 1x1  --output "${EXT}" --right-of $INT --pos 0x0
    xrandr --output "${INT}" --pos ${off_w}x${ext_h} --auto --scale 1x1  --output "${EXT}" --right-of $INT --pos 0x0
}


function display_off() {
    xrandr --output eDP-1 --auto --output $EXT --off
}

keyboard_map

 # xrandr --output eDP-1 --auto --output HDMI-1 --auto

xrandr --output $INT --right-of $EXT --output $EXT --auto

extend
