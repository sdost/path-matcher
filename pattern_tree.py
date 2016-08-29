import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def get_child(self, value):
        for child in self.children:
            if(child.value == value):
                return child
        return None

    def output(self, depth):
        prefix = ""
        for num in range(0,depth):
            prefix += "\t"
        output = prefix + "val => " + str(self.value) + "\n"
        for child in self.children:
            output += child.output(depth + 1)
        return output

class PatternTree:
    def __init__(self):
        self.root = Node(None)

    def insert_pattern(self, pattern):
        curr = self.root # set root to the current node for our algo

        # turn the string into a list, using comma as a delimiter
        pattern_arr = pattern.split(",")

        # filter out empty strings that may have been created with split
        pattern_arr = filter(None, pattern_arr)

        while pattern_arr:
            # pop the first element
            matcher = pattern_arr.pop(0)

            child = curr.get_child(matcher)
            if(child):
                # the current node already has a child with this same string
                # continue traversing the tree
                curr = child
            else:
                # this is a new string, so insert a new child and make it the current node
                curr = self.__insert(matcher, curr)

        # insert a terminating None here so we know we can match this pattern
        self.__insert(None, curr)

    def __insert(self, value, node):
        new_node = Node(value)
        node.add_child(new_node)
        return new_node

    def match_path(self, path):
        # turn the string into a list, using slash as the delimiter
        path_arr = path.split("/")

        # filter out empty string that may have been create with split
        path_arr = filter(None, path_arr)

        # begin walking the tree to find a match
        return self.__match_path(self.root, path_arr)

    def __match_path(self, curr_node, path_arr):
        if(path_arr):
            # we have more path elements
            # pop the first element
            element = path_arr.pop(0)

            paths = []
            for child in curr_node.children:
                if(child.value == element or child.value == "*"):
                    # if this element matches or is a wildcard, recurse on the children
                    paths.append(self.__match_path(child, path_arr[:]))

            # this block does two major things
            # 1. prioritizes fewer wildcards for the matches
            # 2. prioritizes wildcards be futher right in the matches
            least_wildcards = sys.maxint
            best_fit = None
            for path in paths:
                if(path):
                    wildcards = path.count("*")
                    if(wildcards < least_wildcards):
                        least_wildcards = wildcards
                        best_fit = path
                    elif(wildcards == least_wildcards):
                        if(best_fit.find("*") < path.find("*")):
                            best_fit = path

            if(curr_node.value and best_fit):
                # this is kind of a cheat since the root has a value of None
                # we're prepending this nodes value on the path match
                best_fit = curr_node.value + "," + best_fit

            return best_fit
        elif(curr_node.children):
            # we have no more path elements, so we need to find a terminating None
            for child in curr_node.children:
                if(child.value == None):
                    # found a terminating None, so we have a match
                    return curr_node.value

            # otherwise there are no matching pattern with a matching number of fields
            return None
        else:
            # this shouldn't really happen, but it is a fail state
            return None

    def __str__(self):
        return str(self.root.output(0))
