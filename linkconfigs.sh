#!/bin/bash
# EXAMPLE Parameter Expansion
#
# file=foo/bar/baz/test.a.b.c
# echo ${file%.*}  -> foo/bar/baz/test.a.b
# echo ${file%%.*} -> foo/bar/baz/test
# echo ${file#*/}  -> bar/baz/test.a.b.c
# echo ${file##*/} -> test.a.b.c
#
if [ $1 == '-r' ]; then
    echo remove flag parsed, attempting to remove symlinked dotfiles...
    cd && PWD=$(pwd)
    echo PWD=$PWD
    for path in $PWD/.*
    do
        if [ -h $path ]; then
            echo removing link $path from $PWD 2>&1
            rm $path
        fi
    done
else

    # link against tyler's dotfiles
    USER=tyler
    SOURCEDIR=/home/$USER/
    cd && PWD=$(pwd)
    echo "inserting links from $SOURCEDIR to $PWD!"
    echo

    for path in $SOURCEDIR.*
    do
      if [ -h $path ]; then
        echo $path
        ln -fs "$path" "$PWD/${path##*/}"
        echo linking $path to $PWD 
      fi
    done
fi


