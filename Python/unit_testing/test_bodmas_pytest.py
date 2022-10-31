import bodmas


def test_addition():  # test case
    assert bodmas.addition(3, 1) == 4
    assert bodmas.addition(5, 3) == 8
    assert bodmas.addition(33, 11) != 4


# assert bodmas.addition(3, 11) == 4  # This will return an error

def test_subtraction():  # test case2
    assert bodmas.subtraction(20, 10) == 10
    assert bodmas.subtraction(3, 1) != 4
