"""
    Test the single linked list implementation

    1. Cover all the edge cases (!important)

    Edge Cases:
    1. removing items from an empty list
"""

import unittest
from src.single_linked_list import SingleLinkedList

class TestSingleLinkedList(unittest.TestCase):
    """Single Linked List Unit Test Case"""

    def setUp(self):
        """Is run before each test"""
        self._list = SingleLinkedList()

    def test_insert_at_start(self):
        """Test the insert at start for normal and edge cases"""
        self._list.insert_at_start(1)
        self.assertEqual(self._list.size, 1)
        self.assertEqual(self._list.head, 1)

    def test_insert_at_start_for_multiple_values(self):
        """Insert multiple values and test the order"""
        self._list.insert_at_start(2)
        self._list.insert_at_start(3)
        self._list.insert_at_start(4)
        self._list.insert_at_start(5)
        self.assertListEqual(self._list.to_array(), [5, 4, 3, 2, 1])
        
    def test_insert_at_end_when_list_is_empty(self):
        """Test insert a value at the end"""
        self._list.insert_at_end(2)
        self.assertEqual(self._list.size, 1)
        self.assertEqual(self._list.head, 2)

    def test_insert_at_end_by_inserting_multiple_values(self):
        """Insert multiple values and test the order"""
        self._list.insert_at_end(1)
        self._list.insert_at_end(1)
        self._list.insert_at_end(2)
        self._list.insert_at_end(3)
        self._list.insert_at_end(5)
        self.assertListEqual(self._list.to_array(), [1, 1, 2, 3, 5])

    def test_insert(self):
        """"""
        self.assertEqual(True, False)

    def test_remove_at_start(self):
        """"""
        self.assertEqual(True, False)

    def test_remove_at_end(self):
        """"""
        self.assertEqual(True, False)

    def test_remove(self):
        """"""
        self.assertEqual(True, False)

    def test_has_value(self):
        """"""
        self._list.insert_at_start(10)
        self._list.insert_at_start(20)
        self._list.insert_at_start(25)
        self.assertEqual(self._list.has_value(10), True)
        self.assertEqual(self._list.has_value(20), True)
        self.assertEqual(self._list.has_value(25), True)
        self.assertEqual(self._list.has_value(-100), False)

    def test_has_value_empty_list(self):
        self.assertEqual(self._list.has_value(0), False)

    def test_to_array(self):
        """"""
        self.assertEqual(True, False)

    def test_get_size_when_list_is_empty(self):
        """Size should be zero when list is empty"""
        self.assertEqual(self._list.size, 0)

    def test_get_size_after_item_removal_at_start(self):
        """After removing the item at start size should decrement"""
        self._list.insert_at_start(20)
        self._list.remove_at_start()
        self.assertEqual(self._list.size, 0)
    