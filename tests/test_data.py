from ml_random_utils.data import train_val_test_split


def test_train_val_test_split():
    expected_train = ([2, 3, 1, 4, 6, 9], [0, 1, 1, 0, 0, 1])
    expected_val = ([5, 0], [1, 0])
    expected_test = ([8, 7], [0, 1])

    X = list(range(10))
    y = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

    X_train, X_val, X_test = train_val_test_split(
        X,
        y,
        val_size=0.2,
        test_size=0.2,
        random_state=0,
    )

    assert X_train == expected_train
    assert X_val == expected_val
    assert X_test == expected_test
