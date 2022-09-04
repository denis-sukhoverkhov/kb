class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        l, r = 0, k - 1
        ln = len(blocks)

        max_b_blocks = sum([1 for i in blocks[:k] if i == 'B'])
        print(max_b_blocks)

        curr = max_b_blocks
        while r < ln:
            if max_b_blocks == k:
                return 0

            if blocks[l] == "B":
                curr -= 1

            if r + 1 < ln and blocks[r + 1] == "B":
                curr += 1

            max_b_blocks = max(max_b_blocks, curr)

            l += 1
            r += 1

        if max_b_blocks >= k:
            return 0

        return k - max_b_blocks


if __name__ == "__main__":
    obj = Solution()

    assert obj.minimumRecolors("WBBWWBBWBW", 7) == 3
