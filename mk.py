#!/usr/bin/env python

import fnmatch
import os
import md5
import sys

class MarkelTree:
    def __init__(self, root):
        self._root      = root
        self._files     = []
        self._top_hash  = 0
        self._dirs      = []

    def GetDirs(self, directory):
        for root, dirnames, filenames in os.walk(directory):
            for dirname in dirnames:
                self._dirs.append(os.path.join(root, dirname))
        # Add the root to the list of directories 
        self._dirs.append(self._root)
        self._dirs.sort()
        return

    def GetFiles(self, directory):
        for root, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                self._files.append(os.path.join(root, filename))
        self._files.sort()
        return

    def sumfile(self, fobj):
        '''Returns an md5 hash for an object with read() method.'''
        m = md5.new()
        while True:
            d = fobj.read(8096)
            if not d:
                break
            m.update(d)
        return m.hexdigest()

    def md5sum(self, fname):
        '''Returns an md5 hash for file fname, or stdin if fname is "-".'''
        if fname == '-':
            ret = self.sumfile(sys.stdin)
        else:
            try:
                f = file(fname, 'rb')
            except:
                return 'Failed to open file'
            ret = self.sumfile(f)
            f.close()
        return ret

    def PrintItems(self):
        print "files: "
        for filename in self._files:
            #print "%s - %32s" % (item, self.md5sum(item))
            print "%s" % filename
        print "Directories: "
        for dirname in self._dirs:
            print "%s" % dirname

    def run(self):
        self.GetDirs(self._root)
        self.GetFiles(self._root)
        if not self._files and not self._dirs:
            return 0
        self.PrintItems()
        
if __name__ == "__main__":
        mk_a = MarkelTree('/home/sangeeth/work/github/merkle-trees/testA'); 
        mk_a.run();
        # one = MarkelTree("/home/sangeeth/work/github/merkle-trees/testB"); 

