import unittest
from tools.pilot_validation import missed_detections, association_divergence


class PilotValidationTests(unittest.TestCase):
    def test_temporal_match(self):
        result = missed_detections([1, 2, 3], [1.02, 3.01], 0.05)
        self.assertEqual(result["unmatched_reference_indices"], [1])
        self.assertEqual(result["matched_count"], 2)

    def test_no_reference_is_not_success(self):
        with self.assertRaises(ValueError):
            missed_detections(None, [1], 0.1)

    def test_no_reuse_of_detection(self):
        result = missed_detections([1, 1.01], [1.005], 0.01)
        self.assertEqual(result["matched_count"], 1)

    def test_bad_tolerance(self):
        with self.assertRaises(ValueError):
            missed_detections([1], [1], -0.1)

    def test_first_association_divergence(self):
        expected = [[1, "A", "obs1"], [2, "A", "obs2"]]
        observed = [[1, "A", "obs1"], [2, "B", "obs2"]]
        result = association_divergence(expected, observed)
        self.assertEqual(result["first_index"], 1)

    def test_missing_expected_lineage(self):
        with self.assertRaises(ValueError):
            association_divergence(None, [])

    def test_identical_lineage(self):
        self.assertEqual(association_divergence([[1, "A", "o"]], [[1, "A", "o"]])["status"], "AGREEMENT")


if __name__ == "__main__":
    unittest.main()
