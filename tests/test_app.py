import unittest
from app.main import main

class TestMainFunction(unittest.TestCase):
    def test_main_runs_without_error(self):
        try:
            main()
        except Exception as e:
            self.fail(f"main() raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
