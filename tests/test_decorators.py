from ml_random_utils.decorators import parallelize, timeit, dedup


def test_parallelize():
    def square(number):
        return number**2

    decorated = parallelize(backend="threading")(square)
    data = list(range(5))
    result = decorated(data)
    assert result == [0, 1, 4, 9, 16]


def test_parallelize_n_jobs(capsys):
    def square(number):
        return number**2

    n_jobs = 2
    decorated = parallelize(verbose=1, n_jobs=n_jobs, backend="threading")(square)
    data = list(range(5))
    _ = decorated(data)

    _, err = capsys.readouterr()
    assert f"n_jobs={n_jobs}" in err


# def test_parallelize_backend(capsys):
#     def square(number):
#         return number**2

#     decorated = parallelize(verbose=1, backend="threading")(square)
#     data = list(range(5))
#     _ = decorated(data)

#     _, err = capsys.readouterr()
#     assert "ThreadingBackend" in err


def test_parallelize_backend(capsys):
    def square(number):
        return number**2

    decorated = parallelize(verbose=1, n_jobs=1, backend="threading")(square)
    data = list(range(5))
    _ = decorated(data)

    _, err = capsys.readouterr()
    assert "SequentialBackend" in err


def test_timeit(capsys):
    decorated = timeit(lambda: None)
    decorated()

    out, _ = capsys.readouterr()

    assert "Running time" in out


def test_dedup():
    def fun():
        return [1, 1, 2, 3, 3, 4, 4, 5]

    decorated = dedup(fun)
    result = decorated()
    assert result == [1, 2, 3, 4, 5]


def test_dedup_empty():
    def fun():
        return []

    decorated = dedup(fun)
    result = decorated()
    assert not result
