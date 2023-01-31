from main import bool_to_str, sum_list


def test_bool_to_str():
    assert bool_to_str(True) == 'True'
    assert bool_to_str(False) == 'False'


def test_sum():
    assert sum_list([1, 2, 3]) == 6
