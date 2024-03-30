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


if __name__ == "__main__":

    words = []
    with open("input.txt", "r") as fi:
        n = int(fi.readline().strip())
        for i in range(n):
            w = fi.readline().strip()
            words.append(w)

    prefix_cache = {}
    root = TrieNode('')
    root.built_trie_by_words(words, cache=prefix_cache)

    suffix_root = TrieNode('')
    suffix_cache = {}
    suffix_root.built_trie_by_words([w[::-1]for w in words], suffix_cache)

    ans = []
    for k in range(len(words)):
        w = words[k]
        for i in range(1, len(w)+1):
            pref = w[0:i]
            suff = w[::-1][0:i]
            obj1 = prefix_cache[pref]
            obj2 = suffix_cache[suff]

            res = obj1.values.intersection(obj2.values)
            r = {len(words[i]) for i in res}
            if len(res) == 1 or len(res) == len(r):
                l =len(pref + pref)
                if l == len(w):
                    ans.append(w)
                    break
                else:
                    l1 = len(w)-l
                    ans.append(f"{pref}{l1}{suff}")
                    break

    with open("output.txt", "w") as fo:
        for a in ans:
            fo.write(f"{a}\n")
