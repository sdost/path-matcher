import sys
import os
import fileinput
from processor import Processor

# check for input before attempting to process stdin
has_input = os.fstat(sys.stdin.fileno()).st_size > 0
if(has_input):
    processor = Processor()
    for line in fileinput.input():
        processor.process(line.rstrip(), fileinput.lineno())
else:
    print "Usage: python main.py < inputfile [> outputfile]"
