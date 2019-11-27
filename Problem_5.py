class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return TrieNode()
            current_node = current_node.children[char]
        return current_node


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        pass

    def insert(self, char):
        self.children[char] = TrieNode()
        pass

    def suffixes(self, suffix=''):

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


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory", "fact", "funp",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def get_suffixes(prefix):
    if prefix != '':
        prefix_node = MyTrie.find(prefix)
        if prefix_node:
            print('\n'.join(prefix_node.suffixes(prefix)))
        else:
            print(prefix + " not found")
    else:
        print('')


print("---------Test Case 1--------------")
get_suffixes("t")
print("---------Test Case 2--------------")
get_suffixes("fu")
print("---------Test Case 3--------------")
get_suffixes("fa")
print("---------Test Case 4--------------")
get_suffixes("a")
