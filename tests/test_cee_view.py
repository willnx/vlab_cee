# -*- coding: UTF-8 -*-
"""
A suite of tests for the CEEView object
"""
import unittest
from unittest.mock import patch, MagicMock

import ujson
from flask import Flask
from vlab_api_common import flask_common
from vlab_api_common.http_auth import generate_v2_test_token


from vlab_cee_api.lib.views import cee


class TestCEEView(unittest.TestCase):
    """A set of test cases for the CEEView object"""
    @classmethod
    def setUpClass(cls):
        """Runs once for the whole test suite"""
        cls.token = generate_v2_test_token(username='bob')

    @classmethod
    def setUp(cls):
        """Runs before every test case"""
        app = Flask(__name__)
        cee.CEEView.register(app)
        app.config['TESTING'] = True
        cls.app = app.test_client()
        # Mock Celery
        app.celery_app = MagicMock()
        cls.fake_task = MagicMock()
        cls.fake_task.id = 'asdf-asdf-asdf'
        app.celery_app.send_task.return_value = cls.fake_task

    def test_v1_deprecated(self):
        """CEEView - GET on /api/1/inf/cee returns an HTTP 404"""
        resp = self.app.get('/api/1/inf/cee',
                            headers={'X-Auth': self.token})

        status = resp.status_code
        expected = 404

        self.assertEqual(status, expected)

    def test_get_task(self):
        """CEEView - GET on /api/2/inf/cee returns a task-id"""
        resp = self.app.get('/api/2/inf/cee',
                            headers={'X-Auth': self.token})

        task_id = resp.json['content']['task-id']
        expected = 'asdf-asdf-asdf'

        self.assertEqual(task_id, expected)

    def test_post_task(self):
        """CEEView - POST on /api/2/inf/cee returns a task-id"""
        resp = self.app.post('/api/2/inf/cee',
                             headers={'X-Auth': self.token},
                             json={'name': "myCEE", 'image': "CE8.5.1", 'network': "someNetwork"})

        task_id = resp.json['content']['task-id']
        expected = 'asdf-asdf-asdf'

        self.assertEqual(task_id, expected)

    def test_delete_task(self):
        """CEEView - DELETE on /api/2/inf/cee returns a task-id"""
        resp = self.app.delete('/api/2/inf/cee',
                               headers={'X-Auth': self.token},
                               json={'name': "myCEE"})

        task_id = resp.json['content']['task-id']
        expected = 'asdf-asdf-asdf'

        self.assertEqual(task_id, expected)

    def test_get_image_task(self):
        """CEEView - GET on /api/2/inf/cee/image returns a task-id"""
        resp = self.app.get('/api/2/inf/cee/image',
                            headers={'X-Auth': self.token})

        task_id = resp.json['content']['task-id']
        expected = 'asdf-asdf-asdf'

        self.assertEqual(task_id, expected)


if __name__ == '__main__':
    unittest.main()
