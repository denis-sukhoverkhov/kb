from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        visited = {}
        len_cards = len(cards)
        min_len = len_cards
        has_match = False
        for i in range(0, len_cards):
            visited_val_idx = visited.get(cards[i])

            if visited_val_idx is not None:
                has_match = True

                min_len = min(i + 1 - visited_val_idx, min_len)

                if min_len == 2:
                    return min_len

            visited[cards[i]] = i

        return min_len if has_match else -1


if __name__ == "__main__":
    obj = Solution()

    cards = [0, 0]
    assert obj.minimumCardPickup(cards) == 2

    cards = [70, 37, 70, 41, 1, 62, 71, 49, 38, 50, 29, 76, 29, 41, 22, 66, 88, 18, 85, 53]
    assert obj.minimumCardPickup(cards) == 3

    cards = [1, 0, 5, 3, 3, 3, 3]
    assert obj.minimumCardPickup(cards) == 2

    cards = [1, 0, 5, 3]
    assert obj.minimumCardPickup(cards) == -1

    cards = [3, 4, 2, 3, 4, 7]
    assert obj.minimumCardPickup(cards) == 4
