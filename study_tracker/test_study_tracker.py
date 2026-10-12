import tempfile
import unittest
from pathlib import Path

from openpyxl import Workbook, load_workbook

from study_tracker import Topic, load_topics, save_topic_completion


class StudyTrackerWorkbookTests(unittest.TestCase):
    def create_workbook(self, path: Path) -> None:
        workbook = Workbook()
        summary = workbook.active
        summary.title = "Summary"
        summary["A1"] = "Study Progress Tracker"
        sheet = workbook.create_sheet("Python")
        sheet.append(("Done", "#", "Topic", "Subtopic", "What to cover", "Notes"))
        sheet.append((None, 1, "Functions", "Arguments", "Parameters and values", "Review"))
        workbook.save(path)
        workbook.close()

    def test_load_topics_reads_fields_and_completion_status(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "tracker.xlsx"
            self.create_workbook(path)
            workbook = load_workbook(path)
            workbook["Python"]["A2"] = "✔"
            workbook.save(path)
            workbook.close()

            topics = load_topics(path)

        self.assertEqual(len(topics), 1)
        self.assertEqual(
            topics[0],
            Topic(
                area="Python",
                row=2,
                number=1,
                title="Functions",
                subtopic="Arguments",
                coverage="Parameters and values",
                notes="Review",
                done=True,
            ),
        )

    def test_completion_is_saved_without_overwriting_summary_formulas(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            path = Path(temporary_directory) / "tracker.xlsx"
            self.create_workbook(path)
            workbook = load_workbook(path)
            workbook["Summary"]["A2"] = "=COUNTA(Python!C2:C2)"
            workbook.save(path)
            workbook.close()

            topic = load_topics(path)[0]
            save_topic_completion(path, topic, completed=True)

            workbook = load_workbook(path, data_only=False)
            self.assertEqual(workbook["Python"]["A2"].value, "✔")
            self.assertEqual(workbook["Summary"]["A2"].value, "=COUNTA(Python!C2:C2)")
            workbook.close()

            self.assertTrue(load_topics(path)[0].done)
            save_topic_completion(path, topic, completed=False)
            self.assertFalse(load_topics(path)[0].done)

    def test_missing_workbook_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            missing_path = Path(temporary_directory) / "missing.xlsx"

            with self.assertRaisesRegex(FileNotFoundError, "Workbook not found"):
                load_topics(missing_path)


if __name__ == "__main__":
    unittest.main()
