import unittest
from config_check import validate_config

class TestConfig(unittest.TestCase):
    def test_required_keys(self):
        good_data = {"host": "localhost", "port": 8080, "log_level": "INFO"}
        self.assertEqual(validate_config(good_data), [])

        bad_data = {"host": "localhost", "log_level": "INFO"}
        self.assertIn("port", str(validate_config(bad_data)))

    def test_port_type(self):
        # Порт строкой — ошибка
        bad_data = {"host": "localhost", "port": "8080", "log_level": "INFO"}
        self.assertIn("port", str(validate_config(bad_data)))
        
        # Порт числом — ошибки нет
        good_data = {"host": "localhost", "port": 8080, "log_level": "INFO"}
        self.assertEqual(validate_config(good_data), [])

    def test_port_range(self):
        # Порт вне диапазона
        bad_data = {"host": "localhost", "port": 70000, "log_level": "INFO"}
        self.assertIn("диапазоне", str(validate_config(bad_data)))
        
        # Порт 0
        zero_data = {"host": "localhost", "port": 0, "log_level": "INFO"}
        self.assertIn("диапазоне", str(validate_config(zero_data)))

if __name__ == '__main__':
    unittest.main()