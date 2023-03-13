from ml_random_utils.text import replace_char, ngrams, ngrams_vocabulary


def test_replace_char():
    base_string = "A string."
    replaced = replace_char(base_string, char="i", replacement="a")
    expected = "A strang."
    assert replaced == expected


def test_ngrams():
    base_string = "test string"
    ngrams_list = ngrams(base_string, n=4)
    assert ngrams_list == ["test", "est ", "st s", "t st", " str", "stri", "trin", "ring"]


def test_ngrams_vocabulary_contains():
    ngrams = ngrams_vocabulary(alphabet="ACTG", n=4)
    assert "TTTT" in ngrams


def test_ngrams_vocabulary_length():
    ngrams_voc = ngrams_vocabulary(alphabet="ACTG", n=4)
    assert all(len(ng) == 4 for ng in ngrams_voc)
