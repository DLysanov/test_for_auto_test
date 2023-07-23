import pytest

#returne assert expect
@pytest.fixture
def spam(spam):
     spam * 2


def test_spam(spam):
     spam == "spamspam"
