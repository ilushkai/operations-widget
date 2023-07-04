import json
import pytest


def load_file(filename):
    with open(filename, "r") as f:
        open_json = json.load(f)
    return open_json


def test_json_key():
    date = load_file('tests/testfile.json')
    for i in date:
        assert "1" in i, "ключ не найден"


def test_json_value():
    date = load_file('tests/testfile.json')
    for i in date:
        assert i["1"] == "one", "значение неверное"


if __name__ == "__main__":
    pytest.main()
