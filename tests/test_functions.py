from ml_random_utils.functions import compose

def test_compose():
    def square(x: int) -> int:
        print("First", end=" ")
        return x ** 2

    def add2(x: int) -> int:
        print("Second", end=" ")
        return x + 2

    def times2(x: int) -> int:
        print("Third")
        return x * 2

    composed = compose(square, add2, times2)  # type: ignore
    assert composed(2) == 12


def test_compose_order(capsys):
    def square(x: int) -> int:
        print("First", end=" ")
        return x ** 2

    def add2(x: int) -> int:
        print("Second", end=" ")
        return x + 2

    def times2(x: int) -> int:
        print("Third")
        return x * 2

    composed = compose(square, add2, times2)  # type: ignore
    _ = composed(2)

    out, _ = capsys.readouterr()
    assert out.strip() == "First Second Third"
