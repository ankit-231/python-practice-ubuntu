from collections import defaultdict


def test_func_normal(**kwargs):
    print("kwargs:", kwargs)
    print(kwargs["a"])
    # a normal function raise KeyError when trying to access a key which does not exist
    print(kwargs["b"])


def test_func_defaultdict_A(**kwargs):
    # https://docs.python.org/3/library/collections.html#collections.defaultdict
    # Also see defaultdict in python in obsidian
    kwargs = defaultdict(lambda: None, kwargs)
    print("kwargs:", kwargs)
    print(kwargs["a"])
    # it does not raise an error, rather it gives None as we've mentioned in the first parameter which is a factory function (callable)
    print(kwargs["b"])


def test_func_defaultdict_B():
    # https://docs.python.org/3/library/collections.html#collections.defaultdict
    def_dict = defaultdict(int)
    # gives 0, as the factory function is int. defaultdict initializes a non-existent key to 0 here. You can use list to make a non-existent key an empty list
    print(def_dict["any_key"])


if __name__ == "__main__":
    # test_func_normal(a=1)
    # test_func_defaultdict_A(a=1)
    test_func_defaultdict_B()
