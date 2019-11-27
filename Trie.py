#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[3]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def __str__():
        return "{}".format(self.root)

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return TrieNode()
            current_node = current_node.children[char]
        return current_node


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[4]:


class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.is_word = False
        pass

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        pass

    def __str__():
        return "{} {}".format(self.children, self.is_word)

    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point

        if suffix == '':
            return []

        results = []

        curr = self
        char = ""
        for char in curr.children:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return results
        self.find_all(curr, suffix + char, results)
        return results

    def find_all(self, node, suffix, results):

        for char, next_node in node.children.items():

            if next_node.is_word:
                results.append(suffix + char)
            self.find_all(next_node, suffix + char, results)
        pass


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[5]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory", "fact", "funp",
    "trie", "trigger", "trigonometry", "tripod", "top"
]
for word in wordList:
    MyTrie.insert(word)

# In[1]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes(prefix)))
        else:
            print(prefix + " not found")
    else:
        print('')


interact(f, prefix='');

# In[ ]:
