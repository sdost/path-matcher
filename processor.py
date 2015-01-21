import fileinput
from pattern_tree import PatternTree

class Processor:
    def __init__(self):
        self.pattern = False
        self.path = False
        self.count = 0
        self.tree = PatternTree()

    def process(self, line, line_no):
        if(line_no == 1):
            # starting state, begin with processing patterns
            self.pattern = True
            self.count = int(line)
            return
        elif(self.pattern and self.count == 0):
            # if pattern processing is done, process paths
            self.pattern = False
            self.path = True
            self.count = int(line)
            return

        if(self.count > 0):
            if(self.pattern):
                # load patterns into the tree
                self.tree.insert_pattern(line)
                self.count -= 1
            elif(self.path):
                # find match for path
                result = self.tree.match_path(line)
                if(result):
                    print result
                else:
                    print "NO MATCH"
                self.count -= 1
