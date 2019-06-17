"""
    Test the single linked list implementation

    1. Cover all the edge cases (!important)

    Edge Cases:
    1. removing ite ms from an empty list
"""

import unittest
from src.data_structures.single_linked_list import SingleLinkedList


class TestSingleLinkedList(unittest.TestCase):
    """Single Linked List Unit Test Case"""

    def setUp(self):
        """Is run before each test"""
        self._list = SingleLinkedList()

    def test_insert_at_start(self):
        """Test the insert at start for normal and edge cases"""
        new_node = self._list.insert_at_start(1)
        self.assertIsNotNone(new_node)
        self.assertEqual(self._list.size, 1)
        print(self._list.head)
        self.assertEqual(self._list.head, 1)

    def test_insert_at_start_for_multiple_values(self):
        """Insert multiple values and test the order"""
        self._list.insert_at_start(1)
        self._list.insert_at_start(1)
        self._list.insert_at_start(2)
        self._list.insert_at_start(3)
        self._list.insert_at_start(5)
        self.assertEqual(self._list.size, 5)
        self.assertListEqual(self._list.to_array(), [5, 3, 2, 1, 1])

    def test_insert_at_end_when_list_is_empty(self):
        """Test insert a value at the end"""
        new_node = self._list.insert_at_end(2)
        self.assertIsNotNone(new_node)
        self.assertEqual(self._list.size, 1)
        self.assertEqual(self._list.head, 2)

    def test_insert_at_end_by_inserting_multiple_values(self):
        """Insert multiple values and test the order"""
        self._list.insert_at_end(1)
        self._list.insert_at_end(1)
        self._list.insert_at_end(2)
        self._list.insert_at_end(3)
        self._list.insert_at_end(5)
        self.assertEqual(self._list.size, 5)
        self.assertListEqual(self._list.to_array(), [1, 1, 2, 3, 5])

    def test_insert_at_node(self):
        """Insert node into a linked list by storing a reference to prev node"""
        node = self._list.insert_at_start(1)
        new_node = self._list.insert_at_node(node, 2)
        self.assertEqual(self._list.size, 2)
        self.assertListEqual(self._list.to_array(), [1, 2])

    def test_remove_at_start(self):
        """Fill the list and remove nodes and test"""
        self._list.insert_at_end(1)
        self._list.insert_at_end(2)
        self._list.insert_at_end(3)
        self._list.insert_at_end(5)

        removed_node = self._list.remove_at_start()
        self.assertEqual(removed_node.val, 1)
        self.assertListEqual(self._list.to_array(), [2, 3, 5])

        removed_node_2 = self._list.remove_at_start()
        self.assertEqual(removed_node_2.val, 2)
        self.assertListEqual(self._list.to_array(), [3, 5])

    def test_remove_at_end(self):
        """"""
        self._list.insert_at_start(3)
        self._list.insert_at_start(2)
        self._list.insert_at_start(1)

        val = self._list.remove_at_end()
        self.assertEqual(val, 3)
        self.assertListEqual(self._list.to_array(), [1, 2])

    def test_remove(self):
        """Test if the value is removed"""
        self._list.insert_at_start(1)
        self._list.insert_at_start(1)
        node = self._list.insert_at_start(2)

        self._list.remove(2)
        self.assertEqual(self._list.size, 2)
        self.assertEqual(self._list.has_value(2), False)


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
        self._list.insert_at_start(1)
        self._list.insert_at_start(2)
        self._list.insert_at_start(3)

        self.assertListEqual(self._list.to_array(), [3,2,1])

    def test_get_size_when_list_is_empty(self):
        """Size should be zero when list is empty"""
        self.assertEqual(self._list.size, 0)

    def test_get_size_after_item_removal_at_start(self):
        """After removing the item at start size should decrement"""
        self._list.insert_at_start(20)
        self._list.remove_at_start()
        self.assertEqual(self._list.size, 0)
