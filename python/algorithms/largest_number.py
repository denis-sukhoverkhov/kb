
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


def largest_number(A):

    if sum(A) == 0:
        return '0'

    def compare(a, b):
        ab = str(a)+str(b)
        ba = str(b)+str(a)

        tmp = int(ba) - int(ab)
        return tmp

    res = sorted(A, key=cmp_to_key(compare))

    return ''.join(map(str, res))


if __name__ == "__main__":
    A = [3, 30, 34, 5, 9]
    print(largest_number(A))

    A = [ 0, 0, 0, 0, 0 ]
    print(largest_number(A))
