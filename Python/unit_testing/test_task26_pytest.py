from Python.unit_testing import task26


def test_compare_string():  # test case

    assert task26.compare_string("boy", "girl") != True
    assert task26.compare_string("goat", "goat") == True
    assert task26.compare_string("bill", "goat") == False


def test_compare_num():  # test case2
    assert task26.compare_num(3, 4) == False
    assert task26.compare_num(8, 8) == True
    assert task26.compare_num(3, 4) != True
