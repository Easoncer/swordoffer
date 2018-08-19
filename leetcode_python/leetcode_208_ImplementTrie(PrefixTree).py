# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_208_ImplementTrie(PrefixTree).py

@time: 2018/8/18 下午5:28

'''
class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

# The Trie Tree find the data in the tree

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root

        for i in word:
            Node = current.child.get(i, None)
            if not Node:
                Node = TrieNode()
                current.child[i] = Node
            current = Node
        current.end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for i in word:
            node = current.child.get(i)
            if not node:
                return False
            current = node
        return current.end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for i in prefix:
            node = current.child.get(i)
            if not node:
                return False
            current = node
        return True

if __name__ == '__main__':
    obj = Trie()
    obj.insert('apple')
    print obj.search('app')