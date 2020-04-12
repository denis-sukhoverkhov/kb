

def is_number(A):
    import re

    a = A.strip(' ')
    parsed = \
        re.search(r"(?P<num>^([+-]?\.?\d+)(\.\d+)?(?:[Ee][+-]?\d*)?)", a)

    if not parsed:
        return 0

    num = parsed.group('num')

    return 1 if num == a else 0


if __name__ == "__main__":
    assert is_number("+    ") == 0
    assert is_number("0.123") == 1
    assert is_number("005") == 1
    assert is_number(" 0 ") == 1
    assert is_number("2e10") == 1
    assert is_number("232e-10") == 1
    assert is_number("-2e-10") == 1
    assert is_number(".342") == 1
    assert is_number("122") == 1

    assert is_number("   ") == 0
    assert is_number("1U") == 0
    assert is_number("0xFF") == 0
    assert is_number("3.") == 0
    assert is_number("3e0.2") == 0


