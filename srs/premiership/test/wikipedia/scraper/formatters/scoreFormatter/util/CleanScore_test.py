import unittest

from srs.premiership.main.wikipedia.scraper.formatters.dateFormatter.util.CleanDate import clean_date

valid_score_string_1: str = "36 – 40[j]"
valid_score_string_2: str = "[j]36 – 40"
valid_score_string_3: str = "36 [j]– 40"
valid_score_string_4: str = "[j]36 – 40[j]"
valid_expected_cleaned_score_string: str = "36 – 40"

invalid_score_type_int: int = 10
invalid_score_type_float: float = 1.0
invalid_score_type_bool: bool = True


class CleanScoreTest(unittest.TestCase):

    def test_valid_score_string_1(self):
        self.assertEqual(
            clean_date(valid_score_string_1), valid_expected_cleaned_score_string
        )

    def test_valid_score_string_2(self):
        self.assertEqual(
            clean_date(valid_score_string_2), valid_expected_cleaned_score_string
        )

    def test_valid_score_string_3(self):
        self.assertEqual(
            clean_date(valid_score_string_3), valid_expected_cleaned_score_string
        )

    def test_valid_score_string_4(self):
        self.assertEqual(
            clean_date(valid_score_string_4), valid_expected_cleaned_score_string
        )

    def test_invalid_score_type_int(self):
        self.assertEqual(
            clean_date(invalid_score_type_int), "N/A"
        )

    def test_invalid_score_type_float(self):
        self.assertEqual(
            clean_date(invalid_score_type_float), "N/A"
        )

    def test_invalid_score_type_bool(self):
        self.assertEqual(
            clean_date(invalid_score_type_bool), "N/A"
        )


if __name__ == '__main__':
    unittest.main()
