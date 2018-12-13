from unittest import TestCase

from hestia.list_utils import to_list


class ToListTest(TestCase):
    def test_to_list(self):
        assert to_list(None) == [None]
        assert to_list(None, check_none=True) is None
        assert to_list([]) == []
        assert to_list(()) == []
        assert to_list([1, 3]) == [1, 3]
        assert to_list((1, 3)) == [1, 3]
        assert to_list(1) == [1]
        assert to_list('foo') == ['foo']
