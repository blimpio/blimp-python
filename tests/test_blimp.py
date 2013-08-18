import unittest

import blimp


class BlimpClientTestCase(unittest.TestCase):

    def setUp(self):
        self.api = blimp.Client('username', 'api_key', 'app_id', 'secret')

    def test_client_init(self):
        self.assertRaises(TypeError, blimp.Client)

    def test_available_resource_company(self):
        self.assertTrue(hasattr(self.api, 'Company'))

    def test_available_resource_project(self):
        self.assertTrue(hasattr(self.api, 'Project'))

    def test_available_resource_goal(self):
        self.assertTrue(hasattr(self.api, 'Goal'))

    def test_available_resource_task(self):
        self.assertTrue(hasattr(self.api, 'Task'))

    def test_available_resource_comment(self):
        self.assertTrue(hasattr(self.api, 'Comment'))

    def test_available_resource_file(self):
        self.assertTrue(hasattr(self.api, 'File'))

    def test_available_resource_user(self):
        self.assertTrue(hasattr(self.api, 'User'))
