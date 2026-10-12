import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path

from day_counter.day_counter import get_day_number, get_start_date


class DayCounterTests(unittest.TestCase):
    def test_today_is_day_one_and_saved_start_date_is_reused(self) -> None:
        today = date(2026, 10, 12)
        with tempfile.TemporaryDirectory() as temporary_directory:
            storage_file = Path(temporary_directory) / "data" / "start_date.txt"

            first_start = get_start_date(storage_file, today)
            later_start = get_start_date(storage_file, today + timedelta(days=5))

        self.assertEqual(first_start, today)
        self.assertEqual(later_start, today)
        self.assertEqual(get_day_number(first_start, today), 1)
        self.assertEqual(get_day_number(first_start, today + timedelta(days=1)), 2)

    def test_day_number_does_not_fall_below_one(self) -> None:
        start_date = date(2026, 10, 12)

        self.assertEqual(
            get_day_number(start_date, start_date - timedelta(days=1)),
            1,
        )

    def test_invalid_saved_date_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            storage_file = Path(temporary_directory) / "start_date.txt"
            storage_file.write_text("not-a-date", encoding="ascii")

            with self.assertRaisesRegex(ValueError, "saved start date.*invalid"):
                get_start_date(storage_file, date(2026, 10, 12))


if __name__ == "__main__":
    unittest.main()
