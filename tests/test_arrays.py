import pytest
from "01-Arrays/Searching/Linear-Search/linear_search" import linear_search
from "01-Arrays/Searching/Binary-Search/binary_search" import binary_search
from "01-Arrays/Sorting/Bubble-Sort/bubble_sort" import bubble_sort
from "01-Arrays/Sorting/Selection-Sort/selection_sort" import selection_sort
from "01-Arrays/Sorting/Insertion-Sort/insertion_sort" import insertion_sort
from "01-Arrays/Sorting/Merge-Sort/merge_sort" import merge_sort
from "01-Arrays/Sorting/Quick-Sort/quick_sort" import quick_sort

def test_linear_search():
    assert linear_search([10, 20, 30], 20) == 1
    assert linear_search([10, 20, 30], 40) == -1

def test_binary_search():
    assert binary_search([10, 20, 30, 40, 50], 40) == 3
    assert binary_search([10, 20, 30, 40, 50], 10) == 0
    assert binary_search([10, 20, 30, 40, 50], 60) == -1

def test_bubble_sort():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]

def test_selection_sort():
    assert selection_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]

def test_insertion_sort():
    assert insertion_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13]

def test_merge_sort():
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]

def test_quick_sort():
    assert quick_sort([10, 80, 30, 90, 40, 50, 70]) == [10, 30, 40, 50, 70, 80, 90]
