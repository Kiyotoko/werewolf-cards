import pytest

import main

def test_success():
    try:
        main.create("Villager", "?village", 1)
        assert True
    except Exception:
        assert False

def test_failure():
    try:
        main.create("Failure Test", "?failure", 999)
        assert False
    except Exception:
        assert True