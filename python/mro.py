class A:
    def process(self):
        print("A process()")


class B:
    def process(self):
        print("B process()")


class C(A, B):
    pass


class D(C, B):
    pass


if __name__ == "__main__":
    obj = D()
    obj.process()
    print(C.mro())  # print MRO for class C

    data = {1, True, 1.0}

    print(len(data))

    a = [3, 4]

    a.extend([5])

    print(a)
