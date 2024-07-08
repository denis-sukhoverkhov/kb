from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        covered_tile_start = 1
        covered_tile_end = carpetLen

        tiles.sort(key=lambda n: n[0])
        max_tile_number = tiles[-1][-1]

        p1 = 0
        p2 = 0
        mx = 0
        while covered_tile_end != max_tile_number + 1 and p1 < len(tiles) and p2 < len(tiles):

            interval1 = tiles[p1]
            if covered_tile_start > interval1[1]:
                p1 += 1
                covered_tile_start = tiles[p1][0]
                covered_tile_end = covered_tile_start + carpetLen - 1
                continue

            interval2 = tiles[p2]
            if covered_tile_end > interval2[1] and p2 < len(tiles) - 1:
                p2 += 1
                continue

            if p1 == p2:
                return carpetLen

            summ = 0
            for i in tiles[p1 + 1:p2]:
                summ += i[1] - i[0] + 1

            first_part = (tiles[p1][1] - covered_tile_start) + 1
            second_part = (covered_tile_end - tiles[p2][0]) + 1
            summ += first_part + second_part
            mx = max(mx, summ)

            covered_tile_start += 1
            covered_tile_end += 1

        pass
        return mx


if __name__ == "__main__":
    obj = Solution()

    tiles = [[8051, 8057], [8074, 8089], [7994, 7995], [7969, 7987], [8013, 8020], [8123, 8139],
             [7930, 7950], [8096, 8104], [7917, 7925], [8027, 8035], [8003, 8011]]
    carpetLen = 9854
    assert obj.maximumWhiteTiles(tiles, carpetLen) == 126

    tiles = [[10, 11], [1, 1]]
    carpetLen = 2
    assert obj.maximumWhiteTiles(tiles, carpetLen) == 2

    tiles = [[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]]
    carpetLen = 10
    assert obj.maximumWhiteTiles(tiles, carpetLen) == 9
