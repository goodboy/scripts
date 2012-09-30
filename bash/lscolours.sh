#!/bin/bash
# list colours available in the 256 pallete

for i in {0..255} ; do
    printf "\x1b[38;5;${i}mcolour${i}\n"
done
