import unittest
from enviz import Env
env = Env("./tests/.env.test")


class TestEnv(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.maxDiff = None

    def test_count(self):
        env_variables = env.keys()
        self.assertEqual(len(env_variables), 11)

    def test_keys(self):
        keys = [
            "SINGLE_QUOTE",
            "DOUBLE_QUOTE",
            "SINGLE_QUOTE_WITH_SPACE",
            "DOUBLE_QUOTE_WITH_SPACE",
            "DOTS.AS.SEPARATOR",
            "HYPHEN-AS-SEPARATOR",
            "TEST",
            "HASH_SIGN",
            "HASH_SIGN_WITH_SPACE",
            "HASH_SIGN_WITH_SPACE_AND_QUOTES",
            "HASH_IN_END",
        ]

        self.assertListEqual(list(env.keys()), keys)

    def test_values(self):
        test_env = {
            "SINGLE_QUOTE": "SINGLE_QUOTE",
            "DOUBLE_QUOTE": "DOUBLE_QUOTE",
            "SINGLE_QUOTE_WITH_SPACE": "SINGLE QUOTE WITH SPACE",
            "DOUBLE_QUOTE_WITH_SPACE": "DOUBLE QUOTE WITH SPACE",
            "DOTS.AS.SEPARATOR": "DOTS.AS.SEPARATOR",
            "HYPHEN-AS-SEPARATOR": "HYPHEN-AS-SEPARATOR",
            "TEST": "REDECLARED",
            "HASH_SIGN": "#",
            "HASH_SIGN_WITH_SPACE": "# WITH SPACE",
            "HASH_SIGN_WITH_SPACE_AND_QUOTES": "# WITH SPACE AND QUOTES",
            "HASH_IN_END": "HASH IN END #",
        }

        self.assertDictEqual(env, test_env)
