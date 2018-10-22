from unittest import TestCase

from hestia.units import to_percentage


class ToPercentageTest(TestCase):
    """A test case for the `to_percentage`."""
    def test_works_as_expected_for_valid_values(self):
        test_data = [
            (0, '0%'),
            (0.25, '25%'),
            (-0.25, '-25%'),
            (12, '1200%'),
            (0.123, '12.3%'),
            (0.12345, '12.35%'),
            (0.12001, '12%'),
            (0.12101, '12.1%'),
            ('0', '0%'),
            ('0.25', '25%'),
        ]
        for value, expected in test_data:
            result = to_percentage(value)
            self.assertEqual(result, expected)

    def test_raises_value_error_for_invalid_types(self):
        with self.assertRaises(ValueError):
            to_percentage('foo')
