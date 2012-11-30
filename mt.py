#!/usr/bin/env python

import os
import hashlib

class MarkleTree:
    def __init__(self, root):
        self._linelength = 30
        self._root = root
        self._mt = {}
        self._hashlist = {}
        self._tophash = ''
        self.__MT__()

    def Line(self):
        print self._linelength*'-'

    def PrintHashList(self):
        self.Line()
        for item, itemhash in self._hashlist.iteritems():
            print "%s %s" % (itemhash, item)
        self.Line()
        return

    def PrintMT(self, hash):
        value = self._mt[hash]
        item = value[0]
        child = value[1]
        print "%s %s" % (hash, item)
        if not child:
            return
        for itemhash, item in child.iteritems():  
            print "    -> %s %s" % (itemhash, item)
        for itemhash, item in child.iteritems():  
            self.PrintMT(itemhash)

    def MT(self):
        for node, hash in self._hashlist.iteritems():
            print "nodes : ", node
            print "hash  : ", hash
            items = self.GetItems(node)
            value = []
            value.append(node)
            list = {}
            for item in items:
                if node == self._root:
                    list[self._hashlist[item]] = item
                else: 
                    list[self._hashlist[os.path.join(node, item)]] = os.path.join(node, item)
            value.append(list)
            self._mt[hash] = value
        self._tophash = self._hashlist[self._root]

    def __MT__(self):
        self.HashList(self._root)
        #self.PrintHashList()
        self.MT()
        #self.PrintMT(self._tophash)

    def md5sum(self, data):
        m = hashlib.md5()
        print "md5sum: incoming data: %s" % data
        fn = os.path.join(self._root, data)
        if os.path.isfile(fn):
            print "md5sum: %s is a FILE" % fn
            try:   
                f = file(fn, 'rb')
            except:
                return 'ERROR: unable to open %s' % fn
            while True:
                d = f.read(8096)
                if not d:
                    break
                m.update(d)
            f.close()
        else:
            print "md5sum: %s is a STRING" % data
            m.update(data)
        return m.hexdigest()

    def GetItems(self, directory):
        value = []
        if directory != self._root:
            directory = os.path.join(self._root, directory)
        if os.path.isdir(directory):
            items = os.listdir(directory)
            for item in items:
                value.append(item)
                #value.append(os.path.join(".", item))
            value.sort()
        print "GetItems: directory = %s" % directory
        print "GetItems: value = ", value
        return value
    
    def HashList(self, rootdir):
        self.HashListChild(rootdir)
        print "*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@"
        self.PrintHashList()
        print "*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@"
        items = self.GetItems(rootdir)
        if not items:
            self._hashlist[rootdir] = ''
            return
        s = ''
        for subitem in items:
            s = s + self._hashlist[subitem]
        self._hashlist[rootdir] = self.md5sum(s)

    def HashListChild(self, rootdir):
        items = self.GetItems(rootdir)
        if not items:
            self._hashlist[rootdir] = ''
            return
        #digest = ''
        for item in items:
            itemname = os.path.join(rootdir, item)
            print "itemname = %s" % itemname
            if os.path.isdir(itemname):
                print "%s is directory" % itemname
                self.HashListChild(item)
                subitems = self.GetItems(item)
                print "subitems for %s" % item
                print subitems
                print self._hashlist
                s = ''
                for subitem in subitems:
                    s = s + self._hashlist[os.path.join(item, subitem)]
                if rootdir == self._root:
                    self._hashlist[item] = self.md5sum(s)
                else:
                    self._hashlist[itemname] = self.md5sum(s)
            else:
                print "%s is file" % itemname
                if rootdir == self._root:
                    self._hashlist[item] = self.md5sum(item)
                else:
                    self._hashlist[itemname] = self.md5sum(itemname)
   
        #    if rootdir == self._root: 
        #        digest = digest + self._hashlist[item]
        #    else:
        #        digest = digest + self._hashlist[itemname]
        #self._hashlist[rootdir] = self.md5sum(digest)


def MTDiff(mt_a, a_tophash, mt_b, b_tophash):
    if a_tophash == b_tophash:
        print "EQUAL TOPHASH - %s" % a_tophash
    else:
        a_value = mt_a._mt[a_tophash] 
        a_item = a_value[0] 
        a_child = a_value[1] 
        b_value = mt_b._mt[b_tophash] 
        b_item = b_value[0] 
        b_child = b_value[1]

        print a_item    
        print a_child
        print b_item    
        print b_child
        

        for itemhash, item in a_child.iteritems():
            try:
                if b_child[itemhash] == item:
                    print "SAME : %s" % item
            except:
                print "DIFFERENT : %s" % item
                temp_value = mt_a._mt[itemhash]
                if len(temp_value[1]) > 0:
                    print "%s is a dir" % item
                    diffhash = list(set(b_child.keys()) - set(a_child.keys()))
                    
                    MTDiff(mt_a, itemhash, mt_b, diffhash[0])
                else:
                    print "%s is a file" % item
                

if __name__ == "__main__":
    mt_a = MarkleTree('testA')
    mt_b = MarkleTree('testB')
    MTDiff(mt_a, mt_a._tophash, mt_b, mt_b._tophash)

