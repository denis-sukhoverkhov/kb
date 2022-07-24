class TrieNode:

    def __init__(self, key, values=None, childs=None):
        self.key = key

        if not values:
            values = {}

        self.values = values

        if not childs:
            childs = {}

        self.childs = childs

    def get_parent_node(self, ch):
        if ch not in self.childs:
            return self

        return self.get_parent_node(self.childs[ch])

    def built_trie_by_words(self, words, cache=None):
        for j in range(len(words)):
            word = words[j]
            self.__build_trie(j, word, cache)

    def __build_trie(self, idx, word, cache=None):
        current = self

        for i in range(len(word)):
            ch = word[i]

            node_to_insert = current.get_parent_node(ch)

            if ch not in node_to_insert.childs:
                node_to_insert.childs[ch] = TrieNode(key=ch, values={idx})
            else:
                node_to_insert.childs[ch].values.add(idx)

            if cache is not None:
                cache[word[:i+1]] = current.childs[ch]
            current = current.childs[ch]
