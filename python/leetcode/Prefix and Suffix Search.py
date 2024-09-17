from typing import List
from python.leetcode.libs.trie import TrieNode


class WordFilter:

    def __init__(self, words: List[str]):

        self.prefix_root = TrieNode(key='', )
        self.suffix_root = TrieNode(key='', )
        self.prefix_cache = {}
        self.suffix_cache = {}
        self.answer_cache = {}

        self.prefix_root.built_trie_by_words(words, self.prefix_cache)
        self.suffix_root.built_trie_by_words([w[::-1]for w in words], self.suffix_cache)

    def f(self, prefix: str, suffix: str) -> int:
        key = (prefix, suffix)

        if key in self.answer_cache:
            return self.answer_cache[key]

        node_with_prefix = self.prefix_cache.get(prefix, None)
        node_with_suffix = self.suffix_cache.get(suffix[::-1], None)

        if node_with_suffix == -1 or node_with_prefix == -1 or node_with_prefix is None or node_with_suffix is None:
            return -1

        common_indexes = node_with_prefix.values.intersection(node_with_suffix.values)
        res = max(common_indexes)

        self.answer_cache[key] = res
        return self.answer_cache[key]


if __name__ == "__main__":
    obj = WordFilter(["apple", ])
    assert obj.f('b', 'e') == -1

    obj = WordFilter(["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa", "accabaccaa",
       "cabcbbbcca", "ababccabcb", "caccbbcbab", "bccbacbcba"])
    assert obj.f('ab', 'abcaccbcaa') == 4
    assert obj.f('ccbca', 'cbcababac') == 1
    assert obj.f('bccbacbcba', 'a') == 9

    assert obj.f('a', 'aa') == 5
    assert obj.f('cabaaba', 'abaaaa') == 0
    assert obj.f('cacc', 'accbbcbab') == 8
    assert obj.f('ccbcab', 'bac') == 1
    assert obj.f('bac', 'cba') == 2
    assert obj.f('ac', 'accabaccaa') == 5
    assert obj.f('bcbb', 'aa') == 3

    obj = WordFilter(["apple", 'elephant', 'and', 'elent'])
    assert obj.f('a', 'e') == 0

    obj = WordFilter(["apple", 'elephant', 'and', 'elent', 'antre'])
    assert obj.f('a', 'e') == 4
