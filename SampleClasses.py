

class A:

    def __init__(self):
        self.field = "field of A"

    @staticmethod
    def method():
        print("method of A")


class B:

    def __init__(self):
        self.field = "field of B"
        self.field_2 = "other field of B"

    @staticmethod
    def method():
        print("method of B")

    @staticmethod
    def method_2():
        print("other method of B")