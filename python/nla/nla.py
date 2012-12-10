#/usr/bin/python2
# a tool for analyzing NCA logs - NCA Log Analyzer

# TODO: 
# -implement front end logfile segmenter
# -implement stats computation
# -implement xml parser
# -implement signalling parser
# -implement wav file plotter

import csv 
import sys
import getopt

def open_csv(fname):
    # try to open csv file and return a reader/iterator 
    try:
        csvfile = open(fname, 'rb')
        print("opening csv file: '" + fname + "'")
        reader = csv.reader(csvfile)  # delimiter=','
        return reader
    
    except csv.Error, err:
        print("Error:", exc)
        sys.exit(1)

def usage():
    """help function"""
    explanation = "This tool parse the NCE stats file for and provides a disposition summary and conducts log segmentation by classification\n"
    print("Usage: ./nla.py <cpa-stats.csv>\n" + explanation)
      
# parse the cpa-stats.csv file
# def main(argv):
"""main entry point"""
argv = sys.argv
try:
    (optlist, args) = getopt.gnu_getopt(argv[1:], "h:s:", ("help","stats"))
except getopt.GetoptError, exc:
    print("Error:" +  exc)
    sys.exit(usage())

for opt in optlist:
    if opt[0] == "-h" or opt[0] == "--help":
        usage()
        sys.exit(0)
    if opt[0] == "-s" or opt[0] == "--stats":
        showstats = True
        print("enabled statistics!")
        continue
try:
    s = 0
    csv_reader = open_csv(args[0])
    for row in csv_reader:
        s += 1
    print("there are " + str(s) + " records in the stats file")

except csv.Error, err:
    print("Error:", exc)
    sys.exit(1)

if len(args) > 1:
    print("Error: excess args '%s ...'" % args[0])
    sys.exit(usage())

# main(sys.argv)
# (optlist, args) = getopt.gnu_getopt(sys.argv[1:], "h:s:", ("help","stats"))
# row = open_csv(args[1])
