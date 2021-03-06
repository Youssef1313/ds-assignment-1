import random
import pytest
from src.sorting.bubble_sort import bubble_sort
from src.sorting.heap_sort import heap_sort
from src.sorting.insertion_sort import insertion_sort
from src.sorting.merge_sort import merge_sort
from src.sorting.selection_sort import selection_sort
from src.sorting.quick_sort import quick_sort_last_pivot
from src.sorting.quick_sort import quick_sort_random_pivot


def test_none(sort_algorithm):
    _input = None
    with pytest.raises(TypeError):
        assert_sorted(_input, sort_algorithm)


def test_not_a_list(sort_algorithm):
    _input = "Hello world"
    with pytest.raises(TypeError):
        assert_sorted(_input, sort_algorithm)


def test_list_containing_none(sort_algorithm):
    _input = [1, None, 5]
    with pytest.raises(TypeError):
        assert_sorted(_input, sort_algorithm)


def test_list_containing_string(sort_algorithm):
    _input = [1, "Hello world", 5]
    with pytest.raises(TypeError):
        assert_sorted(_input, sort_algorithm)


def test_empty_list(sort_algorithm):
    _input = []
    assert_sorted(_input, sort_algorithm)


def test_single_element(sort_algorithm):
    _input = [5]
    assert_sorted(_input, sort_algorithm)


def test_two_elements_already_sorted(sort_algorithm):
    _input = [1, 3]
    assert_sorted(_input, sort_algorithm)


def test_two_elements_unsorted(sort_algorithm):
    _input = [3, 1]
    assert_sorted(_input, sort_algorithm)


def test_integers_and_floats(sort_algorithm):
    _input = [5, 3.1, 3, 5.5, 1, 2.1]
    assert_sorted(_input, sort_algorithm)


def test_repeated_values(sort_algorithm):
    _input = [5, 3.1, 3, 5.5, 1, 2.1, 3.0, 1]
    assert_sorted(_input, sort_algorithm)


def test_sorting1(sort_algorithm):
    _input = [5, 3, 1, 9, 8, 4, 3, 2, 0, 9, 16, 15, 17]
    assert_sorted(_input, sort_algorithm)


def test_sorting_random_input(sort_algorithm):
    _input = [random.randrange(10000) for i in range(10000)]
    assert_sorted(_input, sort_algorithm)


@pytest.fixture(params=[
    bubble_sort,
    heap_sort,
    insertion_sort,
    merge_sort,
    selection_sort,
    quick_sort_last_pivot,
    quick_sort_random_pivot
    ])
def sort_algorithm(request):
    return request.param


def assert_sorted(_input, sort_algorithm):
    expected = sorted(_input)
    sort_algorithm(_input)
    assert _input == expected
