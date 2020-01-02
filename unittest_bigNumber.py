# -*- coding: utf-8 -*-
import unittest
from BigNumber import *


class TestBigNumber(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_big_number(self):
        self.assertEqual('2', add_big_number('1', '1'))
        self.assertEqual('456', add_big_number('123', '333'))
        self.assertEqual('-357', add_big_number('-123', '-234'))
        self.assertEqual('-1777', add_big_number('-3011', '1234'))
        self.assertEqual('198567812345678173625352372138321363721837236213782163', add_big_number('0','198567812345678173625352372138321363721837236213782163'))
        self.assertEqual('0', add_big_number('198567812345678173625352372138321363721837236213782163', '-198567812345678173625352372138321363721837236213782163'))
        self.assertEqual('90',add_big_number('-1234', '1324'))
        self.assertEqual('-90',add_big_number('-1324', '1234'))
        self.assertEqual('0',add_big_number('0', '0'))
        self.assertEqual('-1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000028374822',add_big_number('-28374823', '-999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999'))
        self.assertEqual('-1234', add_big_number('234', '-1468'))
        self.assertEqual('100000000012344', add_big_number('99999999999999', '12345'))
        self.assertEqual('0', add_big_number('0', '-0'))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestBigNumber('test_add_big_number')]
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
