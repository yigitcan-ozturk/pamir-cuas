import unittest
from tools.spatial_validation import match_reference_tracks


def record(t, x, y, target="UAV-A"):
    return {"time_s": t, "x_m": x, "y_m": y, "target_id": target}


class SpatialValidationTests(unittest.TestCase):
    def test_valid_match(self):
        r = match_reference_tracks([record(1, 0, 0)], [record(1.1, 3, 4)], 0.2, 5)
        self.assertEqual(r["matched_count"], 1)

    def test_spatial_gate(self):
        r = match_reference_tracks([record(1, 0, 0)], [record(1, 10, 0)], 0.1, 5)
        self.assertEqual(r["unmatched_reference_indices"], [0])

    def test_identity_gate(self):
        r = match_reference_tracks([record(1, 0, 0)], [record(1, 0, 0, "UAV-B")], 0, 0)
        self.assertEqual(r["matched_count"], 0)

    def test_time_gate(self):
        r = match_reference_tracks([record(1, 0, 0)], [record(2, 0, 0)], 0.1, 5)
        self.assertEqual(r["matched_count"], 0)

    def test_duplicate_detection_not_reused(self):
        r = match_reference_tracks([record(1, 0, 0), record(1, 0, 0)], [record(1, 0, 0)], 0, 0)
        self.assertEqual(r["matched_count"], 1)

    def test_missing_ground_truth(self):
        with self.assertRaises(ValueError):
            match_reference_tracks(None, [], 0, 0)

    def test_invalid_measurement(self):
        with self.assertRaises(ValueError):
            match_reference_tracks([record(float("nan"), 0, 0)], [], 0, 0)

    def test_negative_tolerance(self):
        with self.assertRaises(ValueError):
            match_reference_tracks([], [], -1, 0)

    def test_no_reference_not_pass(self):
        r = match_reference_tracks([], [record(1, 0, 0)], 0, 0)
        self.assertEqual(r["status"], "NO_REFERENCE_EVENTS")


if __name__ == "__main__":
    unittest.main()
