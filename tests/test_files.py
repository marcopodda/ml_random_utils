from ml_random_utils.files import read_lines


def test_read_lines(tmp_path):
    fakefile = tmp_path / "test_file.txt"
    fakefile.write_text("Line one\n\nLine two \n Line three\n\n\n")
    lines = read_lines(tmp_path / "test_file.txt")
    assert lines == ["Line one", "Line two", "Line three"]


def test_read_lines_skip_blank_false(tmp_path):
    fakefile = tmp_path / "test_file.txt"
    fakefile.write_text("Line one\n\nLine two \n Line three\n\n\n")
    lines = read_lines(tmp_path / "test_file.txt", skip_blank=False)
    assert lines == ["Line one", "", "Line two", "Line three", "", ""]
