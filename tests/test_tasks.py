# -*- coding: UTF-8 -*-
"""
A suite of tests for the functions in tasks.py
"""
import unittest
from unittest.mock import patch, MagicMock

from vlab_cee_api.lib.worker import tasks


class TestTasks(unittest.TestCase):
    """A set of test cases for tasks.py"""
    @patch.object(tasks, 'vmware')
    def test_show_ok(self, fake_vmware):
        """``show`` returns a dictionary when everything works as expected"""
        fake_vmware.show_cee.return_value = {'worked': True}

        output = tasks.show(username='bob', txn_id='myId')
        expected = {'content' : {'worked': True}, 'error': None, 'params': {}}

        self.assertEqual(output, expected)

    @patch.object(tasks, 'vmware')
    def test_show_value_error(self, fake_vmware):
        """``show`` sets the error in the dictionary to the ValueError message"""
        fake_vmware.show_cee.side_effect = [ValueError("testing")]

        output = tasks.show(username='bob', txn_id='myId')
        expected = {'content' : {}, 'error': 'testing', 'params': {}}

        self.assertEqual(output, expected)

    @patch.object(tasks, 'vmware')
    def test_create_ok(self, fake_vmware):
        """``create`` returns a dictionary when everything works as expected"""
        fake_vmware.create_cee.return_value = {'worked': True}

        output = tasks.create(username='bob', machine_name='mycee', image='8.5.1', network='someNetwork', txn_id='myId')
        expected = {'content' : {'worked': True}, 'error': None, 'params': {}}

        self.assertEqual(output, expected)

    @patch.object(tasks, 'vmware')
    def test_create_value_error(self, fake_vmware):
        """``create`` sets the error in the dictionary to the ValueError message"""
        fake_vmware.create_cee.side_effect = [ValueError("testing")]

        output = tasks.create(username='bob', machine_name='mycee', image='8.5.1', network='someNetwork', txn_id='myId')
        expected = {'content' : {}, 'error': 'testing', 'params': {}}

        self.assertEqual(output, expected)

    @patch.object(tasks, 'vmware')
    def test_delete_ok(self, fake_vmware):
        """``delete`` returns a dictionary when everything works as expected"""
        fake_vmware.delete_cee.return_value = {'worked': True}

        output = tasks.delete(username='bob', machine_name='mycee', txn_id='myId')
        expected = {'content' : {}, 'error': None, 'params': {}}

        self.assertEqual(output, expected)

    @patch.object(tasks, 'vmware')
    def test_delete_value_error(self, fake_vmware):
        """``delete`` sets the error in the dictionary to the ValueError message"""
        fake_vmware.delete_cee.side_effect = [ValueError("testing")]

        output = tasks.delete(username='bob', machine_name='mycee', txn_id='myId')
        expected = {'content' : {}, 'error': 'testing', 'params': {}}

        self.assertEqual(output, expected)

    @patch.object(tasks, 'vmware')
    def test_image(self, fake_vmware):
        """``image`` returns a dictionary when everything works as expected"""
        fake_vmware.list_images.return_value = []

        output = tasks.image(txn_id='myId')
        expected = {'content' : {'image': []}, 'error': None, 'params': {}}

        self.assertEqual(output, expected)

    @patch.object(tasks, 'vmware')
    def test_modify_network(self, fake_vmware):
        """``modify_network`` returns an empty content dictionary upon success"""
        output = tasks.modify_network(username='pat',
                                      machine_name='myCEE',
                                      new_network='wootTown',
                                      txn_id='someTransactionID')
        expected = {'content': {}, 'error': None, 'params': {}}

        self.assertEqual(output, expected)

    @patch.object(tasks, 'vmware')
    def test_modify_network_error(self, fake_vmware):
        """``modify_network`` Catches ValueError, and sets the response accordingly"""
        fake_vmware.update_network.side_effect = ValueError('some bad input')

        output = tasks.modify_network(username='pat',
                                      machine_name='myCEE',
                                      new_network='wootTown',
                                      txn_id='someTransactionID')

        expected = {'content': {}, 'error': 'some bad input', 'params': {}}

        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
