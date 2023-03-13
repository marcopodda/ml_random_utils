import pytest

from ml_random_utils.dicts import (
    dictify,
    filter_keys,
    filter_values,
    reverse_dict,
    find_nested,
)

# pylint:disable=redefined-outer-name

@pytest.fixture
def adict():
    return {1: "a", 2: "b", 3: "c"}


@pytest.fixture
def nested_dict():
    return {
        "a": {
            "a1": {
                "a11": 1,
                "a12": 2,
                "a13": 3,
            },
            "a2": {
                "a21": 4,
                "a22": 5,
                "a23": 6,
            },
        },
        "b": {
            "b1": {
                "b11": 7,
                "b12": 8,
                "b13": 9,
            },
            "b2": {
                "b21": 10,
                "b22": 11,
                "b23": 12,
            },
        },
    }


def test_dictify(adict):
    A, B = [1, 2, 3], ["a", "b", "c"]
    assert dictify(A, B) == adict


def test_dictify_duplicate_key():
    A, B = [1, 1, 3], ["a", "b", "c"]

    with pytest.raises(ValueError):
        dictify(A, B)


def test_dictity_raises_value_error():
    A, B = [1, 2, 3], [1, 2]

    with pytest.raises(ValueError):
        dictify(A, B)


def test_dictify_empty_lists():
    A, B = [], []
    assert not dictify(A, B)


def test_filter_keys(adict):
    cond = lambda x: x % 2 == 0
    assert filter_keys(adict, cond) == {2: "b"}


def test_filter_keys_cond_true(adict):
    cond = lambda x: True
    assert filter_keys(adict, cond) == adict


def test_filter_keys_cond_false(adict):
    cond = lambda x: False
    assert not filter_keys(adict, cond)


def test_filter_values(adict):
    cond = lambda x: x == "a"
    assert filter_values(adict, cond) == {1: "a"}


def test_filter_values_cond_true(adict):
    cond = lambda x: True
    assert filter_values(adict, cond) == adict


def test_filter_values_cond_false(adict):
    cond = lambda x: False
    assert not filter_values(adict, cond)


def test_reverse_dict(adict):
    assert reverse_dict(adict) == {"a": 1, "b": 2, "c": 3}


def test_reverse_dict_empty():
    assert not reverse_dict({})


def test_find_nested(nested_dict):
    assert find_nested(nested_dict, "a.a1.a13") == 3


def test_find_nested_not_found(nested_dict):
    with pytest.raises(KeyError):
        find_nested(nested_dict, "a.c")


def test_find_nested_subdict(nested_dict):
    subdict = {"a11": 1, "a12": 2, "a13": 3}
    assert find_nested(nested_dict, "a.a1") == subdict


def test_find_nested_wrong_key(nested_dict):
    with pytest.raises(ValueError):
        assert find_nested(nested_dict, "a.a1.")
