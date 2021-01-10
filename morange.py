#! /usr/bin/env python3
import argparse
import os
"""
Using a tree to store and maintain all information.
A parent node: which contain indentifying information.
children node a: for inter node which have child node.
children node b: for document node.
"""


class Node:
    def __init__(self, nodeid, nodename='', nodetype=None):
        self.nodeid = nodeid
        self.nodename = nodename
        self.nodetype = nodetype


class DirNode(Node):
    def __init__(self, nodeid, nodename='', nodetype='dir'):
        Node.__init__(self, nodeid, nodename, nodetype)
    
    def add_node(self, parent):

        pass


class DocNode(Node):
    def __init__(self, nodeid, nodename='', nodetype='doc'):
        Node.__init__(self, nodeid, nodename, nodetype)
        self.title = None
        self.author = None
        self.journal = None
        self.pubtime = None

    pass


def main():
    pass


if __name__ == '__main__':
    k = DirNode()
    main()






