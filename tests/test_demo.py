import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from demo import run_demo

class DemoTest(unittest.TestCase):
    def test_group_split_and_metrics(self):
        result = run_demo()
        self.assertEqual(result["train_subjects"] + result["test_subjects"], 30)
        self.assertGreater(result["test_subjects"], 0)
        self.assertTrue(0 <= result["balanced_accuracy"] <= 1)
        self.assertTrue(0 <= result["auroc"] <= 1)

if __name__ == "__main__":
    unittest.main()