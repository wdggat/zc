#!/usr/bin/env python 

import unittest
import zc

class ZCtest(unittest.TestCase):
    def test_get_all_buyarrs(self):
        buy_max, length = 2, 3
	expected = [[1,1,1], [1,1,2], [1,2,1], [1,2,2],[2,1,1], [2,1,2],[2,2,1]]

	actual = []
	for buy_arr in zc._get_all_buyarrs(buy_max, length, 1):
	    actual.append(buy_arr)
	self.assertListEqual(expected, actual)

    def test_check_2s1(self):
        sp_arra = [1.59, 3.45, 4.9]
	sp_arrb = [6.05, 4.0, 1.4]
	self.assertTrue(zc.check_2s1(sp_arra, sp_arrb))

        sp_arra = [1.59, 3.45, 3.5]
	sp_arrb = [6.05, 4.0, 1.4]
	self.assertFalse(zc.check_2s1(sp_arra, sp_arrb))

if __name__=='__main__':
    unittest.main()

