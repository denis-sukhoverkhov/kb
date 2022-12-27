class Solution:
    def interpret(self, command: str) -> str:
        s = []

        m = {
            '()': 'o',
            '(al)': 'al',
        }

        res = []
        for i in command:
            if i == 'G':
                res.append('G')
                continue

            if i == ')':
                s.append(i)
                res.append(m[''.join(s)])
                s = []
                continue

            s.append(i)

        return ''.join(res)


if __name__ == "__main__":
    obj = Solution()

    command = "G()(al)"
    assert obj.interpret(command) == 'Goal'
