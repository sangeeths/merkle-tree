#!/usr/bin/env python

import fnmatch
import os
import md5
import sys
import hashlib

class MarkleTree:
    def __init__(self, root):
        self._root      = root
        self._files     = []
        self._top_hash  = 0
        self._dirs      = []
        self._mk        = {}
        self._tophash   = ''

    def GetAllDirs(self, directory):
        for root, dirnames, filenames in os.walk(directory):
            for dirname in dirnames:
                self._dirs.append(os.path.join(root, dirname))
        # Add the root to the list of directories 
        self._dirs.append(self._root)
        self._dirs.sort()
        return
    
    def GetAllFiles(self, directory):
        for root, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                self._files.append(os.path.join(root, filename))
        self._files.sort()
        return

    def GetDirs(self, directory):
        items = os.listdir(directory)
        dirs = []
        for item in items:
            if os.path.isdir(item):
                dirs.append(os.path.join(directory, item))
        dirs.sort()
        return dirs

    def GetItems(self, directory):
        items = os.listdir(directory)
        value = []
        for item in items:
            value.append(os.path.join(directory, item))
        value.sort()
        #print value
        return value

    def DirDigest(self, directory):
        items = self.GetItems(directory)
        if not items:
            self._mk[directory] = ''
            return
        digest = ''
        for item in items:
            if os.path.isdir(item):
                self.DirDigest(item)
                subitems = self.GetItems(item)
                s = ''
                for subitem in subitems:
                    s = s + self._mk[subitem]
                self._mk[item] = self.md5sum(s)
            else:
                self._mk[item] = self.md5sum(item)
            digest = digest + self._mk[item]
        self._mk[directory] = self.md5sum(digest)        

    def TopHash(self):
        return self._tophash

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

    def PrintItems(self):
        print "files: "
        for filename in self._files:
            print "%s - %32s" % (filename, self.md5sum(filename))
            #print "%s" % filename
        print "Directories: "
        for dirname in self._dirs:
            print "%s" % dirname
    
    def PrintMTree(self):
        print "---------------------------------------"
        for key, value in self._mk.iteritems():
            print "Key      : %s" % key
            print "Value    : %s" % value
        print "---------------------------------------"
        return

    def run(self):
        #self.GetDirs(self._root)
        #self.GetAllFiles(self._root)
        #if not self._files and not self._dirs:
        #    return 0
        #self.PrintItems()
        #self.GetItems(self._root)
        #self.GetMTree(self._root)
        #self.PrintMTree()
        #self.A(self._root)
        self.DirDigest(self._root)
        self.PrintMTree()


if __name__ == "__main__":
        mt_a = MarkleTree('/home/sangeeth/work/github/merkle-tree/testA')
        mt_a.run()
        # one = MarkelTree("/home/sangeeth/work/github/merkle-trees/testB"); 

