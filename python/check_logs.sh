#!/bin/bash
# find files listed in the passed csv file
csvfile="$1"
newarch="./new_log_archive"
mkdir $newarch

# an array of log files
declare -a loglist
row=0

while read line; do
    pat="${line%,2012*}"
    echo "looking for $pat ..."

    # create an array of the found log files
    loglist=("$(find ./ -regex "^.*${pat}.*")")

    if [[ -n "${loglist[*]}" ]]; then
        echo "found log files:"
        echo "${loglist[*]}"
        echo
        ((count++))
        for file in ${loglist}; do
            echo "copying file: $file to $newarch"
            cp --parents $file $newarch
        done
        echo
    else
        echo "NO LOG FILES FOUND!"
        echo
    fi
    unset loglist

done < $csvfile

linecount="$(gawk '/\,/ { if(NR == 2){next}; count++ } END { print count}' $csvfile )"
echo
echo "number of files found = $count"
echo "line count in provided csv file '$csvfile' is $linecount"
unset count

cp $csvfile "$newarch/cpa-stats.csv"
cd $newarch
zip -r package.zip ./*
