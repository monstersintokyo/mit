# coding=utf-8

import unittest

class EnvironmentTest(unittest.TestCase):

    def test_environments_exist(self):
        self.assertIsNotNone(__import__('mit.settings.development'))
        self.assertIsNotNone(__import__('mit.settings.production'))
        self.assertIsNotNone(__import__('mit.settings.test'))