import pytest

from utils import arrs


@pytest.mark.parametrize("array, index, default, expected", [
    ([1, 2, 3], 1, "test", 2),
    ([], 0, "test", "test"),
    ([1, 2, 3], -1, "test", "test")])
def test_get(array, index, default, expected):
    assert arrs.get(array, index, default) == expected
    # assert arrs.get([1, 2, 3], 1, "test") == 2
    # assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice([1, 2, 3, 4], -5, 3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -3, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
