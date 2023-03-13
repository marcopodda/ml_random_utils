from ml_random_utils.paths import listdir, dir_is_empty


def test_listdir(tmp_path):
    some_dir = tmp_path / "somedir"
    some_dir.mkdir()

    (some_dir / "file5.txt").touch()
    (some_dir / "file2.txt").touch()
    (some_dir / "file3.txt").touch()
    (some_dir / "file1.txt").touch()
    (some_dir / "file4.txt").touch()

    paths = listdir(some_dir)
    expected = [
        some_dir / "file1.txt",
        some_dir / "file2.txt",
        some_dir / "file3.txt",
        some_dir / "file4.txt",
        some_dir / "file5.txt",
    ]
    assert paths == expected


def test_dir_is_empty(tmp_path):
    some_dir = tmp_path / "somedir"
    some_dir.mkdir()
    assert dir_is_empty(some_dir)
