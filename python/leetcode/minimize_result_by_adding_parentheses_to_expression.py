from copy import copy


class Solution:
    def minimizeResult(self, expression: str) -> str:

        result_expr = f"({expression})"
        min_result = eval(expression)

        num1, num2 = expression.split('+')
        num1_digits = [i for i in num1]
        num2_digits = [i for i in num2]
        for i in range(len(num1)):
            num1_digits_copy = copy(num1_digits)
            v1 = '*(' if i != 0 else '('
            num1_digits_copy.insert(i, v1)
            first_part = ''.join(num1_digits_copy)
            for j in range(len(num2)):
                num2_digits_copy = copy(num2_digits)

                v = ')*' if j != 0 else ')'
                num2_digits_copy.insert(len(num2) - j, v)
                second_part = ''.join(num2_digits_copy)
                current_expression = f"{first_part}+{second_part}"

                current_eval = eval(current_expression)
                if current_eval < min_result:
                    min_result = current_eval
                    result_expr = current_expression

        return result_expr.replace('*', '')


if __name__ == "__main__":
    obj = Solution()

    assert obj.minimizeResult("999+999") == "(999+999)"

    assert obj.minimizeResult("12+34") == "1(2+3)4"

    assert obj.minimizeResult("247+38") == "2(47+38)"