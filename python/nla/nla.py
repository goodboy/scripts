#/usr/bin/env python
# a tool for analyzing NCA logs - NCA Log Analyzer

# TODO: 
# -implement front end logfile segmenter
# -implement stats computation
# -implement xml parser
# -implement signalling parser
# -implement wav file plotter

import csv 
import sys, getopt

def open_csv(f):
    # open and close the file resource all in one block
    # try / catch to validate csv file
    try:
        csvfile = open(f, 'rb')
        print "opening csv file:", f
        loglist = csv.reader(csvfile)  # delimiter=','
        return loglist
    
    except csv.Error, err:
        print "Error:", exc
        sys.exit(1)

def usage():
    """help function"""
    explanation = "This tool parse the NCE stats file for and provides a disposition summary and conducts log segmentation by classification\n"
    print "Usage: ./nla.py <cpa-stats.csv>\n" + explanation
      
# parse the cpa-stats.csv file
def main(argv):
    """main entry point"""
    try:
        (optlist, args) = getopt.gnu_getopt(argv[1:], "h:s:", ("help","stats"))
    except getopt.GetoptError, exc:
        print "Error:", exc
        sys.exit(usage())

    for opt in optlist:
        if opt[0] == "-h" or opt[0] == "--help":
            usage()
            sys.exit(0)
        if opt[0] == "-s" or opt[0] == "--stats":
            showstats = True
            print "enabled stats!"
            continue

    try:
        row = open_csv(args[0])
        print "row = ", row.next()

    except cvs.error, err:
        print "Error:", exc
        sys.exit(1)

    if len(args) > 1:
        print "Error: excess args '%s ...'" % args[0]
        sys.exit(usage())

main(sys.argv)
(optlist, args) = getopt.gnu_getopt(sys.argv[1:], "h:s:", ("help","stats"))
row = open_csv(args[0])
