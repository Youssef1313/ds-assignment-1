# TODO: Remove noqa in all tests.

def test_none():
    input = None  # noqa: F841
    assert True  # TODO: Test against the 6 algorithms.


def test_not_a_list():
    input = "Hello world"  # noqa: F841
    assert True  # TODO: Test against the 6 algorithms.


def test_list_containing_none():
    input = [1, None, 5]  # noqa: F841
    assert True  # TODO: Test against the 6 algorithms.


def test_list_containing_string():
    input = [1, "Hello world", 5]  # noqa: F841
    assert True  # TODO: Test against the 6 algorithms.


def test_empty_list():
    input = []  # noqa: F841
    assert True  # TODO: Test against the 6 algorithms.


def test_single_element():
    input = [5]  # noqa: F841
    assert True  # TODO: Test against the 6 algorithms.


def test_two_elements_already_sorted():
    input = [1, 3]  # noqa: F841
    assert True  # TODO: Test against the 6 algorithms.


def test_two_elements_unsorted():
    input = [3, 1]  # noqa: F841
    assert True  # TODO: Test against the 6 algorithms.


def test_integers_and_floats():
    input = [5, 3.1, 3, 5.5, 1, 2.1]  # noqa: F841
    assert True  # TODO: Test against the 6 algorithms.


def test_repeated_values():
    input = [5, 3.1, 3, 5.5, 1, 2.1, 3.0, 1]  # noqa: F841
    assert True  # TODO: Test against the 6 algorithms.


def test_sorting1():
    input = [5, 3, 1, 9, 8, 4, 3, 2, 0, 9, 16, 15, 17]  # noqa: F841
    assert True  # TODO: Test against the 6 algorithms.
