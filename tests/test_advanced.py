# -*- coding: utf-8 -*-

from .context import camera_window

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(camera_window.hmm())


if __name__ == '__main__':
    unittest.main()
