#/usr/bin/env python
# a tool for analyzing NCA logs - NCA Log Analyzer

import csv

def parse_csv(f):
    try:
        csvfile = open(f, 'rb')
    except:
        print >> sys.stderr, "Error: couldn't open csv file!"

def usage():
    """help function"""
    explanation = "This tool parse the NCE stats file for and provides a disposition summary and conducts log segmentation by classification\n"
    print "Usage: ./nla.py <cpa-stats.csv>\n" + explanation
      
# parse the cpa-stats.csv file
def main(argv):
    "main entry point"
    try:
        (optlist, args) = getopt.getopt(argv[1:], "h:", ("help",))
    except getopt.GetoptError, exc:
        print "Error:", exc
        sys.exit(usage())

        # make sure we pass a filename
        if opt[0] == "":
            usage()
            sys.exit(0)

    for opt in optlist:

    if len(args) > 0:
        print "Error: excess args '%s ...'" % args[0]
        sys.exit(usage())


main(sys.argv)
