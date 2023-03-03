import unittest as ut
import os
import src.config as config

class TestConfig(ut.TestCase):
    def test_getDir(self):
        os.chdir("./src")
        self.assertEqual(type(config.getDir()), list)

    def test_readconfigFile(self):
        self.assertEqual(type(config.readconfigFile()), int)