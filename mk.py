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
        self.HashList(self._root)

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
            items = self.GetItems(node)
            value = []
            value.append(node)
            list = {}
            for item in items:
                list[self._hashlist[item]] = item
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
        if os.path.isfile(data):
            try:   
                f = file(data, 'rb')
            except:
                return 'ERROR: unable to open %s' % data 
            while True:
                d = f.read(8096)
                if not d:
                    break
                m.update(d)
            f.close()
        else:
            m.update(data)
        return m.hexdigest()

    def GetItems(self, directory):
        value = []
        if os.path.isdir(directory):
            items = os.listdir(directory)
            for item in items:
                value.append(os.path.join(directory, item))
            value.sort()
        return value

    def HashList(self, rootdir):
        items = self.GetItems(rootdir)
        if not items:
            self._hashlist[rootdir] = ''
            return
        digest = ''
        for item in items:
            if os.path.isdir(item):
                self.HashList(item)
                subitems = self.GetItems(item)
                s = ''
                for subitem in subitems:
                    s = s + self._hashlist[subitem]
                self._hashlist[item] = self.md5sum(s)
            else:
                self._hashlist[item] = self.md5sum(item)
            digest = digest + self._hashlist[item]
        self._hashlist[rootdir] = self.md5sum(digest)

def MTDiff(mt_a, mt_b):
    mt_a.PrintMT(mt_a._tophash)
    print 45*'*'
    mt_b.PrintMT(mt_b._tophash)
    print 45*'*'
     

if __name__ == "__main__":
        mt_a = MarkleTree('/home/sangeeth/work/github/merkle-tree/testA')
        #mt_a.PrintMT(mt_a._tophash)
        #print 30*'#'
        mt_b = MarkleTree('/home/sangeeth/work/github/merkle-tree/testB')
        #mt_b.PrintMT(mt_b._tophash)
        MTDiff(mt_a, mt_b)
        #print mt_b._tophash
        #mt_a = MarkleTree('/home/sangeeth/work/github/dltb')
        #mt_a.run()
        # one = MarkelTree("/home/sangeeth/work/github/merkle-trees/testB"); 

