def test_add_two():
    x = 2
    y = 2
    assert x + y == 4


def test_dict_contains():
    x = {"a": 1, "b": 2}
    expected = {"a": 1}
    assert expected.items() <= x.items()
