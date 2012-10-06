#!/bin/bash
# automatic ranking using the manual method from
# https://wiki.archlinux.org/index.php/Mirrors#List_by_speed

if [[ $USER != "root" ]]; then
    echo "You must be root to run this script!!!"
    echo "Change to root with 'sudo su' then try again"
    exit 1
fi

rm=$(type -P rankmirrors)
if [[ -f "$rm" ]]; then
    cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
    sed '/^#\S/ s|#||' -i /etc/pacman.d/mirrorlist.bak
    $rm -n 6 /etc/pacman.d/mirrorlist.bak > /etc/pacman.d/mirrorlist
    pacman -Syy
fi
