import unittest
from enviz import env

class TestEnv(unittest.TestCase):
    def test_count(self):
        # there are 17 variables in .env
        # 2 of them are comments
        env_variables = env.keys()
        self.assertEqual(len(env_variables), 17)
