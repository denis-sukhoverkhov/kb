from typing import List
from python.leetcode.libs.trie import TrieNode


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        root = TrieNode('')
        root.built_trie_by_words(products)

        res = []
        current = root
        not_found = False
        for ch in searchWord:
            if ch not in current.childs or not_found:
                res.append([])
                not_found = True
                continue

            res.append(current.childs[ch].values)
            current = current.childs[ch]

        result = []
        for i in res:
            tmp = [products[k] for k in i]
            tmp.sort()

            result.append(tmp[:3])

        return result


if __name__ == "__main__":
    obj = Solution()

    products = ["havana"]
    searchWord = "tatiana"
    assert obj.suggestedProducts(products, searchWord) == [[], [], [], [], [], [], []]

    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    assert obj.suggestedProducts(products, searchWord) == [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"]
    ]
