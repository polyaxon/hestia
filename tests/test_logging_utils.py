from unittest import TestCase

from mock import patch

from hestia.logging_utils import log_spec, DATETIME_REGEX


class TestLoggingUtils(TestCase):
    def test_has_timestamp(self):
        self.assertEqual(
            log_spec(log_line='foo', timestamp='2018-12-11 10:24:57 UTC'),
            '2018-12-11 10:24:57 UTC -- foo'
        )

    def test_has_no_timestamp(self):
        with patch('hestia.logging_utils.now') as now_patch:
            log_spec(log_line='foo')

        self.assertEqual(now_patch.call_count, 1)

    def test_log_line_has_datetime(self):
        self.assertEqual(
            log_spec(log_line='2018-12-11 10:24:57 UTC foo', check_timestamp=True),
            '2018-12-11 10:24:57 UTC -- foo'
        )

    def test_log_line_has_iso_datetime(self):
        self.assertEqual(
            log_spec(log_line='2018-12-11T08:49:07.163495183Z foo', check_timestamp=True),
            '2018-12-11 08:49:07 UTC -- foo'
        )

    def test_log_line_has_level(self):
        self.assertEqual(
            log_spec(log_line='2018-12-11T08:49:07.163495183Z foo',
                     check_timestamp=True,
                     log_level='INFO'),
            '2018-12-11 08:49:07 UTC INFO -- foo'
        )
