#!/bin/bash
# find files listed in the passed csv file
csvfile="$1"
newarch="./new_log_archive"
mkdir $newarch

# routines
have() { type -P "$1" > /dev/null; }

# an array of log files
declare -a loglist
row=0

# config
z=1
we='.*\.analyzer-engine\.0\.?' # to search for wavs
re='.analyzer-engine.0.?'      # to remove in wavs

# pre-detect tools
if have sox; then
    sox_exits=1
else
    echo "SOX is not installed!"
    echo "NOTE: all wav files must be converted to 16 bit LPCM prior to use with cpe offline tool"
    sox_exits=0
fi

while read line; do

    # strip everything after the first delimiter (comma)
    pat="${line%,*}"
    echo "looking for $pat ..."

    # create an array of the found log files
    loglist=("$(find ./ -regex "^.*${pat}.*")")

    if [[ -n "${loglist[*]}" ]]; then
        echo "found log files:"
        echo "${loglist[*]}"
        echo

        # keep track of the number of files
        ((count++))

        # keep track of number of wavs (i.e. if there are multiples for a given call log)
        wavs=("$(gawk '/.wav/ { print }' <<< "${loglist[*]}")")

        # number of additionally segmented wav files
        duplicate=1     
        combine_flag=""


        for file in ${loglist}; do

            if [[ $file =~ $re ]]; then

                echo "found audio file: $file"

                # keep note of which wav file
                newname="${file/$re/}"
                echo "should be renamed to: $newname"

                # check if there is more then one wave file in this log set
                if (( ${#wavs[@]} > 1)); then
                    echo "more then one wav file detected!"
                    combine_flag="--combine concatenate"

                    # echo "file $newname already exists!"
                    # newname="${newname/'.wav'/-${duplicate}}.wav"
                    # echo "renaming to $newname"
                    # ((duplicate += 1))

                    # if there are > 1 wav files : concatenate with sox
                fi

                # check for sox conversion tool
                # convert audio to linear for cpe offline tool
                if (($sox_exits)); then

                    sox -S ${combine_flag} <infile> -b 16 -e signed ${newname}
                fi
                cp $file "$newarch/$newname"
            else

                echo "copying file: $file to $newarch"
                cp --parents $file $newarch
            fi
        done
        echo
    else
        echo "NO LOG FILES FOUND!"
        echo
    fi
    unset loglist

done < $csvfile

# filter csv to skip title and field names
linecount="$(gawk '/\,/ { if(NR == 2){next}; count++ } END { print count}' $csvfile )"
echo
echo "number of files found = $count"
echo "line count in provided csv file '$csvfile' is $linecount"
unset count

cp $csvfile "$newarch/cpa-stats.csv"
cd $newarch
if (( z == 1 )); then
    zip -r package.zip ./*
fi
