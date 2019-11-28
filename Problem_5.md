# Problem 5 
## Design Insert
Every character of input word is inserted as a trie node. Each trie node has children. Children array pointers to next level trie nodes.
## Time Complexity Insert
Insertion of word is directly proportional to length of the word that is inserted.
**Time complexity of O(n)** 
n is number of characters in the word to be inserted
## Design Suffixes
In order to find all the suffixes for a given prefix, we have to loop through all the letters of the word. When we find the trie node of the last letter, we can list all the suffixes by traversing through all the trie nodes and recursively traversing through other branches from end of prefix.
## Time Complexity Suffixes
Time complexity is directly proportional to number of words which start with same prefix and length of the word 
**Time complexity of O(k * n)** 
k is the number of words start with same prefix and n is the length of word
## Space Complexity
Space complexity is directly proportional to total number of alphabets, length of the word and number of words in the Trie.
**Space complexity of O(n)** 