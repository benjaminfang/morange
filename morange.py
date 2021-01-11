#! /usr/bin/env python3
import argparse
import os
import re
import sys
import pickle
"""
Using a tree to store and maintain all information.
A parent node: which contain indentifying information.
children node a: for inter node which have child node.
children node b: for document node.
"""


class Node:
    def __init__(self, nodeid, nodename=''):
        self.nodeid = nodeid
        self.nodename = nodename
        self.parent = None
        self.child = []

    def detach(self):
        if self.parent:
            self.parent.remove_child(self)
        self.parent = None

    def list(self, i=0):
        print('\t' * i, end='')
        print(self)
        for child in self.child:
            child.list(i+1)


class DirNode(Node):
    def __init__(self, nodeid, nodename=''):
        Node.__init__(self, nodeid, nodename)
        self.nodetype = 'dir'
        self.parent = None
        self.child = []

    def __str__(self):
        return str(self.nodeid) + ': ' + self.nodename

    def add_child(self, child):
        self.child.append(child)
        child.parent = self

    def remove_child(self, child):
        if child in self.child:
            self.child.remove(child)
            child.parent = None

    def delete(self):
        for ele in self.child:
            self.parent.add_child(ele)
        self.child = []
        self.parent = Node


class DocNode(Node):
    def __init__(self, nodeid, nodename=''):
        Node.__init__(self, nodeid, nodename)
        self.nodetype = 'doc'
        self.title = None
        self.author = None
        self.journal = None
        self.pubtime = None

    def __str__(self):
        return str(self.nodeid) + ': ' + self.nodename

    def delete(self):
        self.detach()


def init():
    pass


def switch():
    pass


def help():
    pass


def config():
    pass


def list():
    pass


def add():
    pass


def remove():
    pass


def move():
    pass


def infor():
    pass


def search():
    pass


def open_():
    pass


def export():
    pass


def import_():
    pass


def parse_main_args():
    parser = argparse.ArgumentParser(description='morange')
    parser.add_argument('args', nargs='*')
    args = parser.parse_args()
    args = args.args
    return args


def parse_config_args():
    parser = argparse.ArgumentParser(description='configration.')
    pass


def initate():
    home = os.getenv('HOME')
    config_path = os.path.join(home, '.config/morange.conf')
    if not os.path.exist(config_path):
        print('creat a initate config file.')
    else:
        with open(config_path) as config_file:
            db_path = None
            doc_path = None
            for line in config_file:
                eles = line.rstrip().split('=')
                if len(eles) == 2:
                    if eles[0].strip() == 'db_path':
                        exec('global db_path; ' + line)
                    elif line[0].strip() == 'doc_path':
                        exec('global doc_path; ' + line)
        with open(os.path.join(db_path, 'db_config')) as db_config:
            dbs = None
            current_db = None
            for line in db_config:
                eles = line.rstrip().split('=')
                if len(eles) == 2:
                    if eles[0].strip() == 'current_db':
                        exec('global current_db' + line)
                    elif line[0].strip() == 'dbs':
                        exec('global dbs; ' + line)
        with open(os.path.join(doc_path, 'doc_path')) as doc_config:
            docs = None
            current_doc = None
            for line in doc_config:
                eles = line.rstrip().split('=')
                if len(eles) == 2:
                    if eles[0].strip() == 'current_doc':
                        exec('global current_doc; ' + line)
                    elif line[0].strip() == 'docs':
                        exec('global docs; ' + line)
    db_data = pickle.load(open(current_db), 'rb')
    return home, config_path, db_path, doc_path, dbs, current_db, docs, current_doc, db_data


def main():
    initate()
    args = parse_main_args()
    if len(args) == 0:
        input()
    elif args[0] == 'help':
        pass
    elif args[0] == 'config':
        pass
    elif args[0] == 'list':
        pass
    elif args[0] == 'add':
        pass
    elif args[0] == 'remove':
        pass
    elif args[0] == 'move':
        pass
    elif args[0] == 'search':
        pass
    elif args[0] == 'export':
        pass
    elif args[0] == 'import':
        pass
    elif args[0] == 'switch':
        pass
    else:
        print('Usage: morange cmd [options]')
        print('use "morange help" for more information.')
        exit(0)
    pass


if __name__ == '__main__':
    main()






