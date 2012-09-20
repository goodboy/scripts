#!/bin/bash
if [[ -n "$1" ]]; then
    suffix="$1"
else
    suffix='m4a'
fi
mkdir ./wavs

for file in *"$suffix"; do
    newfile="${file%%$suffix}wav"
    echo -e "converting $file to $newfile\n"
    faad -o "${newfile}" "${file}"
    mv "$newfile" ./wavs/
done
