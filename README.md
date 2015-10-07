Merkle-Trees
============

## Directory - testA:
```
testA
|-- dir1
|   |-- file11.txt
|   |-- file12.txt
|   |-- file13.txt
|   `-- tempdir
|-- dir2
|   |-- file21.txt
|   |-- file22.txt
|   |-- file23.txt
|   `-- file24.txt
|-- file1.txt
|-- file2.txt
|-- file3.txt
`-- file4.txt
```

## Merkle Tree for testA (output of in-order traversal): 
```
975d3cfb91c68616410d9fb0e582edfd testA                          <---- Top Hash
    -> 78e1885a370bc213414858c648e916fb file3.txt               <--   Child of testA
    -> e4069a89d02170a56e27daaa6ea81859 file2.txt               <--   Child of testA
    -> c97336b6e52347826f8c7b0168049909 file4.txt               <--   Child of testA
    -> 9a8be8bd88caa906ac72e7ae1613e4ef dir1                    <--   Child of testA
    -> f41fba8a445fe47182a474534b3ee47f dir2                    <--   Child of testA
    -> cdd60fb7f1b59f3461895fb238c77a0a file1.txt               <--   Child of testA
78e1885a370bc213414858c648e916fb file3.txt                      --->  Leaf Nodes (No Children)
e4069a89d02170a56e27daaa6ea81859 file2.txt
c97336b6e52347826f8c7b0168049909 file4.txt
9a8be8bd88caa906ac72e7ae1613e4ef dir1
    -> 61ba29b15e22f3030c0a0ce4e36c00da dir1/file12.txt
    -> 27064003da39a4a8bda08730b06fc7b9 dir1/file11.txt
    -> b7973c0623ce39225d8e7681c32c6ec7 dir1/tempdir
    -> bd7b8b855864cf813a5e9ff0f79ab350 dir1/file13.txt
61ba29b15e22f3030c0a0ce4e36c00da dir1/file12.txt
27064003da39a4a8bda08730b06fc7b9 dir1/file11.txt
b7973c0623ce39225d8e7681c32c6ec7 dir1/tempdir
bd7b8b855864cf813a5e9ff0f79ab350 dir1/file13.txt
f41fba8a445fe47182a474534b3ee47f dir2
    -> c8d661a948cf8dc9a70f9ca75633c34f dir2/file21.txt
    -> 59ee8564e4d1a52c17557f447bb98f40 dir2/file22.txt
    -> dc6d821c596f9cde0967875fa8de90fe dir2/file23.txt
    -> 0c9643339784601bb3f6f43e63d1604b dir2/file24.txt
c8d661a948cf8dc9a70f9ca75633c34f dir2/file21.txt
59ee8564e4d1a52c17557f447bb98f40 dir2/file22.txt
dc6d821c596f9cde0967875fa8de90fe dir2/file23.txt
0c9643339784601bb3f6f43e63d1604b dir2/file24.txt
cdd60fb7f1b59f3461895fb238c77a0a file1.txt
```

## Python Data Structure for the above Merkle Tree:
```
mt_a = MarkleTree('testA')
print mt_a._mt
{'78e1885a370bc213414858c648e916fb': ['file3.txt', {}], '61ba29b15e22f3030c0a0ce4e36c00da': ['dir1/file12.txt', {}], 'e4069a89d02170a56e27daaa6ea81859': ['file2.txt', {}], 'c97336b6e52347826f8c7b0168049909': ['file4.txt', {}], '59ee8564e4d1a52c17557f447bb98f40': ['dir2/file22.txt', {}], '9a8be8bd88caa906ac72e7ae1613e4ef': ['dir1', {'61ba29b15e22f3030c0a0ce4e36c00da': 'dir1/file12.txt', '27064003da39a4a8bda08730b06fc7b9': 'dir1/file11.txt', 'b7973c0623ce39225d8e7681c32c6ec7': 'dir1/tempdir', 'bd7b8b855864cf813a5e9ff0f79ab350': 'dir1/file13.txt'}], 'b7973c0623ce39225d8e7681c32c6ec7': ['dir1/tempdir', {}], 'bd7b8b855864cf813a5e9ff0f79ab350': ['dir1/file13.txt', {}], '975d3cfb91c68616410d9fb0e582edfd': ['testA', {'78e1885a370bc213414858c648e916fb': 'file3.txt', 'e4069a89d02170a56e27daaa6ea81859': 'file2.txt', 'c97336b6e52347826f8c7b0168049909': 'file4.txt', '9a8be8bd88caa906ac72e7ae1613e4ef': 'dir1', 'f41fba8a445fe47182a474534b3ee47f': 'dir2', 'cdd60fb7f1b59f3461895fb238c77a0a': 'file1.txt'}], 'f41fba8a445fe47182a474534b3ee47f': ['dir2', {'c8d661a948cf8dc9a70f9ca75633c34f': 'dir2/file21.txt', '59ee8564e4d1a52c17557f447bb98f40': 'dir2/file22.txt', 'dc6d821c596f9cde0967875fa8de90fe': 'dir2/file23.txt', '0c9643339784601bb3f6f43e63d1604b': 'dir2/file24.txt'}], 'dc6d821c596f9cde0967875fa8de90fe': ['dir2/file23.txt', {}], 'cdd60fb7f1b59f3461895fb238c77a0a': ['file1.txt', {}], '0c9643339784601bb3f6f43e63d1604b': ['dir2/file24.txt', {}], 'c8d661a948cf8dc9a70f9ca75633c34f': ['dir2/file21.txt', {}], '27064003da39a4a8bda08730b06fc7b9': ['dir1/file11.txt', {}]}
```

## Dictionary to represent Merkle Tree:
```
MerkleTrees._mt (dictionary)
{
TopHash : [root file-/folder-name, {child1hash:child1, child2hash:child2, ...., childnhash:childn}],
child1hash : [child1 file-/folder-name, {grandchild1hash:grandchild1, ...., grandchildnhash:grandchildn}],
...
..
.
grandchildn : [grandchildn file-/folder-name, {}]       <-- NOTE: hash with empty child is a LEAF node
}
```

## MD5 for directories:
```
Dir1 contains File1.txt, File2.txt, File3.txt (the contents inside the Dir1 is sorted)
md5sum(Dir1) = md5sum(strcat(md5sum(File1.txt), md5sum(File2.txt), md5sum(File3.txt))
File1.txt -> md5sum(File1.txt)
File2.txt -> md5sum(File2.txt)
File3.txt -> md5sum(File3.txt)
```

## TODO:

### Handling empty directory 

Currently, the md5sum for any folder is md5sum(strcat(md5sum(all_files_in_this_folder_sorted))). If the folder is empty, then this is will be an empty string. the md5sum of '' is always the same. This will lead to collision. So for an empty folder, instead of an empty string, we should use something unique about the folder, may be the folder name. 

### Directory tree representation in the merkle tree python dictionary 
The files and the folders inside the given base directory (in the above example, testA) are represented in relative path and not absolute path. Representing those files and folders in absolute path leads to problems when two merkle trees are compared to find the data to be synced. But using the relative path leads to lots of if's and else's in the code as the merkle tree algorithm for finding md5sum is based on the recursion function. These frequent use of if's and else's should be removed. 

```
if node == self._root:
    list[self._hashlist[item]] = .....  
else:
    list[self._hashlist[item]] = .....
```

### Pre-/post-order traversal 
Currently, the PrintMT() does an inorder traversal and prints the values accordingly. The per- and post-order traversals should also be implemented.

### Handling file/folder adding and deleting 
When two merkle trees are compared, other than modification/updation of file/folder, the comparison algorithm should also look out for the new added or deleted files. The following will cover all the cases.

```
for hashes in treeA
    check the same hash in treeB
_and_
for hashes in treeB
    check the same hash in treeA

set(treeA) - set(treeB)
_and_
set(treeB) - set(treeA)
```

### More get/set functions as a part of MerkleTree class
The MerkleTree variables are directly accessed outside by main and tree traversal algorithm. Get/Set functions should be provided to access them from outside. For example:
GetChildOf(hash) -> Given a hash, return the list of subitems, if any. Empty if null. None if the given hash is not found in the Merkle Tree.
GetChildHashOf(hash) -> Given a hash, return the list of subitems hash. Empty if null and None if given hash is not found in the Merkle Tree.
GetNameOfItem(hash) -> Given a hash, return the name of the item (file/folder).

### Files with the same content
Two files with different name (in same or different directory) but has the same content will generate the same md5sum. This is a straight forward case of collision. When the same hash is added to the dictionary, the old one will get overwritten by the new one. The Merkle tree should handle the collision. Before adding the hash to the Merkle tree, look it up and add it only if they are not present. If they are present, then rehash it by adding the filename prefix (or find a better method).




