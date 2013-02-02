import unittest

import blimp


class BlimpClientTestCase(unittest.TestCase):

    def test_client_init(self):
        with self.assertRaises(TypeError):
            blimp.Client()
