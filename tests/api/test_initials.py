def test_lists():
    # if [1, 2, 3] != [1, 2, 3]:
    #     raise AssertionError("Not equal")
    # identical to \/
    assert [1, 2, 3] == [1, 2, 3]


def test_lists_ok():
    # if ["a", 3, 3] == [1, 2, 3]:
    #     raise AssertionError("Not equal")
    # identical to \/
    assert ["a", 3, 3] != [1, 2, 3]


def test_lists_neok():
    # if ["a", 3, 3] != [1, 2, 3]:
    #     raise AssertionError("Not equal")
    # identical to \/
    assert ["a", 3, 3] != [1, 2, 3]
