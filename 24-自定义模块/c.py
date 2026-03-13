__all__ = ["test", "say_hello"]


def test(a, b):
    return a + b


def say_hello():
    print("hello")


def ttt():
    print("ttt")


if __name__ == "__main__":
    print(test(1, 2))
    say_hello()
