import pytest
from divisors import find_divisors


@pytest.mark.parametrize('number, expected', [(2, [1,2]), (20, [1,2,4,5,10,20])])
def test_divisors(number, expected):

    assert find_divisors(number) == expected

