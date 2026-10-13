from validator import validate_config


def test_valid(tmp_path):
    p = tmp_path / "app.env"
    p.write_text("APP_NAME=demo\nENVIRONMENT=dev\n", encoding="utf-8")
    assert validate_config(str(p))


def test_missing_key(tmp_path):
    p = tmp_path / "app.env"
    p.write_text("APP_NAME=demo\n", encoding="utf-8")
    assert not validate_config(str(p))


def test_missing_file(tmp_path):
    assert not validate_config(str(tmp_path / "missing.env"))
