def correct(expr: str) -> str:
    brackets_dict = {
        "[": "]",
        "(": ")",
        "{": "}",
    }

    inverse_brackets_dict = {v: k for k, v in brackets_dict.items()}

    pos = 0
    stack = []
    corrected_expression = []
    while pos < len(expr):
        s = expr[pos]
        if s in ("[", "(", "{"):
            stack.append(s)
            corrected_expression.append(s)
            pos += 1
        elif s in ("]", ")", "}"):
            if len(stack) > 0 and s != brackets_dict[stack[-1]]:
                corrected_expression.append(brackets_dict[stack[-1]])
                del stack[-1]
            elif len(stack) == 0:
                corrected_expression.append(inverse_brackets_dict[s])
                corrected_expression.append(s)
                break
            else:
                corrected_expression.append(s)
                pos += 1
                del stack[-1]

    for i in stack:
        corrected_expression.append(brackets_dict[i])

    return "".join(corrected_expression)


assert correct("[(])") == "[()]()"
assert correct("[{{}]{(})") == "[{{}}]{()}()"
assert correct(")") == "()"
assert correct("") == ""
assert correct("((") == "(())"
