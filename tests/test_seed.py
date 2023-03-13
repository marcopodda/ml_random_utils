import os
from ml_random_utils.seed import seed_everything


def test_seed_everything():
    seed_everything(1234897)
    assert os.environ["PYTHONHASHSEED"] == str(1234897)
