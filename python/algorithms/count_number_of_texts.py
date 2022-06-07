class Solution:

    def __init__(self):
        self.keyboard = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

    def countTexts(self, pressedKeys: str) -> int:
        part = ''

        counts = []
        for n in pressedKeys:
            if part and n not in part:
                curr_ct = 1

                key = part[0]
                len_part = len(part)
                for i in range(len(self.keyboard[key]), -1, 1):
                    curr_ct += len_part // i

                part = ''

            part += n


if __name__ == "__main__":
    obj = Solution()

    pressedKeys = "22233"
    assert obj.countTexts(pressedKeys) == 8
