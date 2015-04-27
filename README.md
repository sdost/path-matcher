Path Matcher Test by Samuel Dost
================================

#Purpose
This program is intended to solve the problem put forth in the document 'Pattern-Matching Paths'. Given formatted input with a series of patterns, process a series of paths and find the pattern which best matches them.

#Usage
python main.py < inputfile > outputfile

#Process
The application grabs input from stdin line by line in main.py, and processes it in a simple state machine in the Processor class. This class contains the logic which parses the input based on the specifications set forth. The count is read for patterns, and then that many patterns are processed and added to a tree structure called PatternTree. The pattern tree breaks down the pattern by element and creates a hierarchy representing it within the tree. Any common elements from other patterns are reused within the tree to provide branching hierarchies, e.g. '*,b,*' and '*,*,c' have a common starting wildcard, and would be represented as:
```
val => *
	val => b
		val => *
			val => None
	val => *
		val => c
			val => None
```
The end of patterns are denoted with a None child.

Once all patterns are read in the Processor class changes state to process the paths one by one. The paths are similarly broken down into elements, and the tree is recursed to find matching elements. At each tree level, the first element of the path is consumed, and when there are no more elements to consume, we check for a None element to see if there is a valid pattern. All other outcomes bubble up as None. At each recursion level, the possible solutions are prioritized by minimum number of wildcards, and by first occurance of a wildcard in the path so far. Ultimately, the search should find only one solution and print it to stdout. If no solution can be found, then "NO MATCH" is printed.

#Methodology
I chose to use an N-ary tree in this fashion because of the potential commonality within the data set of both the patterns and the paths, and the hierarchical nature of the matching (one needs to match the left most portion before considering the rest).

#Performance
The insertion time of the patterns should be about O(log n) or logarithmic time. The recursive search should also be around O(log n), but I could see the possibility for certain data sets to produce nodes with many children, e.g. 'a,a', 'a,b', 'a,c'...'a,zzz', which may in certain cases cause the search to approach O(n).

Thanks!
