import pandas as pd

from ml_random_utils.dataframes import rebuild_index


def test_rebuild_index():
    def fun():
        return pd.DataFrame(
            {"col1": ["a", "b", "c"], "col2": ["d", "e", "f"]}
        ).set_index("col1")

    decorated = rebuild_index(fun)
    result = decorated()
    assert result.index.tolist() == [0, 1, 2]
