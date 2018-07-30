# -*- coding: UTF-8 -*-
"""
A suite of tests for the HTTP API schemas
"""
import unittest

from jsonschema import Draft4Validator, validate, ValidationError
from vlab_cee_api.lib.views import cee


class TestCEEViewSchema(unittest.TestCase):
    """A set of test cases for the schemas of /api/1/inf/cee"""

    def test_post_schema(self):
        """The schema defined for POST is valid"""
        try:
            Draft4Validator.check_schema(cee.CEEView.POST_SCHEMA)
            schema_valid = True
        except RuntimeError:
            schema_valid = False

        self.assertTrue(schema_valid)

    def test_delete_schema(self):
        """The schema defined for DELETE is valid"""
        try:
            Draft4Validator.check_schema(cee.CEEView.DELETE_SCHEMA)
            schema_valid = True
        except RuntimeError:
            schema_valid = False

        self.assertTrue(schema_valid)

    def test_get_schema(self):
        """The schema defined for GET is valid"""
        try:
            Draft4Validator.check_schema(cee.CEEView.GET_SCHEMA)
            schema_valid = True
        except RuntimeError:
            schema_valid = False

        self.assertTrue(schema_valid)

    def test_images_schema(self):
        """The schema defined for GET on /images is valid"""
        try:
            Draft4Validator.check_schema(cee.CEEView.IMAGES_SCHEMA)
            schema_valid = True
        except RuntimeError:
            schema_valid = False

        self.assertTrue(schema_valid)

    def test_delete(self):
        """The DELETE schema happy path test"""
        body = {'name': "mycee"}
        try:
            validate(body, cee.CEEView.DELETE_SCHEMA)
            ok = True
        except ValidationError:
            ok = False

        self.assertTrue(ok)

    def test_delete_required(self):
        """The DELETE schema requires the parameter 'name'"""
        body = {}
        try:
            validate(body, cee.CEEView.DELETE_SCHEMA)
            ok = False
        except ValidationError:
            ok = True

        self.assertTrue(ok)

    def test_post(self):
        """The POST schema happy path test"""
        body = {'name': "mycee", 'network': "someNetwork", 'image': "CE8.5.1"}
        try:
            validate(body, cee.CEEView.POST_SCHEMA)
            ok = True
        except ValidationError:
            ok = False

        self.assertTrue(ok)

    def test_post_name_required(self):
        """The POST schema requires the 'name' parameter"""
        body = { 'network': "someNetwork", 'image': "CE8.5.1"}
        try:
            validate(body, cee.CEEView.POST_SCHEMA)
            ok = False
        except ValidationError:
            ok = True

        self.assertTrue(ok)

    def test_post_network_required(self):
        """The POST schema requires the 'network' parameter"""
        body = { 'name': "mycee", 'image': "CE8.5.1"}
        try:
            validate(body, cee.CEEView.POST_SCHEMA)
            ok = False
        except ValidationError:
            ok = True

        self.assertTrue(ok)

    def test_post_image_required(self):
        """The POST schema requires the 'image' parameter"""
        body = { 'name': "mycee", 'network': "someNetwork"}
        try:
            validate(body, cee.CEEView.POST_SCHEMA)
            ok = False
        except ValidationError:
            ok = True

        self.assertTrue(ok)


if __name__ == '__main__':
    unittest.main()
