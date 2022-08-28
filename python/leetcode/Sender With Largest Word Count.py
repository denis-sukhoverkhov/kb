from collections import defaultdict
from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        m = defaultdict(int)

        max_count = 0
        author_idx = 0
        for i in range(len(messages)):
            m[senders[i]] += len([i for i in messages[i].split(' ') if i])

            current_count = m[senders[i]]
            if current_count > max_count:
                max_count = current_count
                author_idx = i
            elif current_count == max_count:
                if senders[i] > senders[author_idx]:
                    author_idx = i

        return senders[author_idx]


if __name__ == "__main__":
    obj = Solution()

    messages = ["Hello userTwooo", "Hi userThree", "Wonderful day Alice",
                "Nice day userThree"]
    senders = ["Alice", "userTwo", "userThree", "Alice"]
    assert obj.largestWordCount(messages, senders) == "Alice"

    messages = ["How is leetcode for everyone", "Leetcode is useful for practice"]
    senders = ["Bob", "Charlie"]
    assert obj.largestWordCount(messages, senders) == "Charlie"