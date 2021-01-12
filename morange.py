#! /usr/bin/env python3
import argparse
import os
import re
import pickle
import pathlib
import configparser
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
            child.list(i + 1)


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


def config(args_list):
    # next part. 20210111
    def parse_args(args_list):
        parser = argparse.ArgumentParser()
        parser.add_argument('-db_path', type=pathlib.Path, default=None, help='morange database path.')
        parser.add_argument('-doc_path', type=pathlib.Path, default=None, help='morange document storage path.')
        parser.add_argument('-pdf_opener', type=str, default=None, help='program handle pdf file.')
        parser.add_argument('-doc_opener', type=str, default=None, help='program handle otc/doc office file.')
        parser.add_argument('-txt_opener', type=str, default=None, help='program handle txt plat file.')
        args = parser.parse_args(args_list)
        return args.db_path, args.doc_path, args.pdf_opener, args.doc_opener, args.txt_opener

    home = os.getenv("HOME")
    """
    the location of configfile must fixed. it is under $
    creat default configuration file and write default configure entry is work of setup.py. after the setup
    process, the default db_path, doc_path directory should be exists also.
    """
    config = configparser.ConfigParser()
    config.read(config_path)
    section = config['morange config']
    if len(section) > 0:
        print('Previous configure information:')
        for key in section:
            print(key, '=', section[key])
    dt_path, args.doc_path,



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
    """
    First step is initate(), it function following:
    1) check if 
    """
    home = os.getenv('HOME')
    config_path = os.path.join(home, '.config/morange.conf')
    if os.path.exists(config_path):
        print('the utility not initately configured, please run "morange config", to configure.')
        exit(0)
    else:
        with open(config_path) as config_file:
            db_path = None
            doc_path = None
            pdf_opener = None
            doc_opener = None
            txt_opener = None
            """Read morange configure information."""
            for line in config_file:
                eles = line.rstrip().split('=')
                if len(eles) == 2:
                    var_ = eles[0].strip()
                    if var_ == 'db_path':
                        exec('global db_path; ' + line)
                    elif var_ == 'doc_path':
                        exec('global doc_path; ' + line)
                    elif var_ == 'pdf_opener':
                        exec('global pdf_opener; ' + line)
                    elif var_ == 'doc_opener':
                        exec('global doc_opener; ' + line)
                    elif var_ == 'txt_opener':
                        exec('global txt_opener; ' + line)
        if not (db_path and doc_path and pdf_opener and doc_opener and txt_opener):
            print('there are some information not configured, please use "morange config" to configure.')
            exit(0)
        db_infor_path = os.path.join(db_path, '__db_infor__')
        doc_infor_path = os.path.join(doc_path, '__doc_infor__')
        if (not os.path.exists(db_infor_path)) or (not os.path.exists(doc_infor_path)):
            print('there not a db initated, please use "morange init" to initate a db.')
            exit(0)
        with open(os.path.join(db_path, '__db_infor__')) as db_config:
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
        if not (dbs and current_db and docs and current_doc):
            print('there not a db initated, please use "morange init" to initate a db.')
    db_data = pickle.load(open(current_db), 'rb')
    return (home, config_path, db_path, doc_path, db_infor_path, dbs,
        current_db, doc_infor_path, docs, current_doc, db_data)


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
