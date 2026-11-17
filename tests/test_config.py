import unittest
from config_check import validate_config

class TestConfig(unittest.TestCase):
    def test_required_keys(self):
        good_data = {"host": "localhost", "port": 8080, "log_level": "INFO"}
        self.assertEqual(validate_config(good_data), [])

        bad_data = {"host": "localhost", "log_level": "INFO"}
        self.assertTrue(len(validate_config(bad_data)) > 0)
        self.assertIn("port", str(validate_config(bad_data)))

if __name__ == '__main__':
    unittest.main()