import unittest

import blimp


class BlimpClientTestCase(unittest.TestCase):

    def test_client_init(self):
        self.assertRaises(TypeError, blimp.Client)
