# Problem 7
## Design Add handler
Given a path and handler. path can be split by "/" to form path list. Each element in the path list can be inserted as RouterTrieNode. 
Each trie node has children. Children is an array of pointers to next level of trie nodes. RouterTrieNode also has attribute handler, handler provides the routing capability.
## Time Complexity Insert
Insertion of path is directly proportional to length of the path list that is inserted.
**Time complexity of O(n)** 
n is number of paths in the path to be inserted
## Design Lookup
Path to be searched or looked up can be split based on "/" which provides with the list of paths with which the the RouteTrieNodes are inserted. Lookup loops through all the elements of path list and traverse through the RouterTrie and return the handler of the appropriate RouterTrieNode.
## Time Complexity Lookup
Time complexity is directly proportional to number of elements in the path list.
**Time complexity of O(n)** 
## Space Complexity
Space complexity is directly proportional to total number of path in path list and number of paths in the RouterTrie.
**Space complexity of O(k * n)** 
K is the depth of the RouterTrie.