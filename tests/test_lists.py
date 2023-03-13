import pytest

from ml_random_utils.lists import flatten, filter_list, intersection, union, difference


# pylint:disable=redefined-outer-name


@pytest.fixture
def both_nonempty():
    return [[1, 2, 3], [2, 3, 4]]


@pytest.fixture
def both_empty():
    return [[], []]


@pytest.fixture
def A_empty():
    return [[], [2, 3, 4]]


@pytest.fixture
def B_empty():
    return [[1, 2, 3], []]


def test_flatten(both_nonempty):
    assert flatten(both_nonempty) == [1, 2, 3, 2, 3, 4]


def test_flatten_with_A_empty(A_empty):
    A, B = A_empty
    assert flatten([A, B]) == B


def test_flatten_with_B_empty(B_empty):
    A, B = B_empty
    assert flatten([A, B]) == A


def test_flatten_both_empty(both_empty):
    assert not flatten(both_empty)


def test_filter_list(both_nonempty):
    A = flatten(both_nonempty)
    cond = lambda x: x % 2 == 0
    assert filter_list(A, cond) == [2, 2, 4]


def test_filter_list_cond_false(both_nonempty):
    A = flatten(both_nonempty)
    cond = lambda _: False
    assert not filter_list(A, cond)


def test_filter_list_cond_true(both_nonempty):
    A = flatten(both_nonempty)
    cond = lambda _: True
    assert filter_list(A, cond) == A


def test_filter_list_empty_list():
    cond = lambda _: True
    assert not filter_list([], cond)


def test_intersection(both_nonempty):
    A, B = both_nonempty
    assert intersection(A, B) == [2, 3]


def test_intersection_A_empty(A_empty):
    A, B = A_empty
    assert not intersection(A, B)


def test_intersection_B_empty(B_empty):
    A, B = B_empty
    assert not intersection(A, B)


def test_intersection_both_empty(both_empty):
    A, B = both_empty
    assert not intersection(A, B)


def test_union(both_nonempty):
    A, B = both_nonempty
    assert union(A, B) == [1, 2, 3, 4]


def test_union_A_empty(A_empty):
    A, B = A_empty
    assert union(A, B) == B


def test_union_B_empty(B_empty):
    A, B = B_empty
    assert union(A, B) == A


def test_union_both_empty(both_empty):
    A, B = both_empty
    assert not union(A, B)


def test_difference(both_nonempty):
    A, B = both_nonempty
    assert difference(A, B) == [1]


def test_difference_A_empty(A_empty):
    A, B = A_empty
    assert not difference(A, B)


def test_difference_B_empty(B_empty):
    A, B = B_empty
    assert difference(A, B) == A


def test_difference_both_empty(both_empty):
    A, B = both_empty
    assert not difference(A, B)
