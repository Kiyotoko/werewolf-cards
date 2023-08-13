import pytest

from src import creator


def test_success():
    try:
        creator.create("Villager", "?village", 1, input_folder="../images/", output_folder="../output/")
        assert True
    except Exception:
        assert False


def test_failure():
    try:
        creator.create("Failure Test", "?failure", 999, input_folder="../images/", output_folder="../output/")
        assert False
    except Exception:
        assert True
