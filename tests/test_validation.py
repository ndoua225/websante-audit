import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from websante.validation import validate

def test_valid():
    assert validate("monsite.ci")[0] is True

def test_localhost():
    assert validate("localhost")[0] is False

def test_private():
    assert validate("192.168.1.1")[0] is False

def test_url_path():
    assert validate("monsite.ci/page")[0] is False
