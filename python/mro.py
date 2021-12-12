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


obj = D()
obj.process()
print(C.mro())  # print MRO for class C
