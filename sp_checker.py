#!/usr/bin/env python
#-*-encoding: utf-8-*-

"""
an -> 倍数, sn -> sp值
a1s1, a2s2, a3s3 ... ansn
cost: 2 * ( a1 + a2 + ... + an)
如果需要任意sn命中，都有盈利 ->  2*aksk >= 2 * (a1 + a2 + ... + an) -> 1/sk <= ak/(a1 + a2 + ... + an)
->  1/s1 + 1/s2 + ... + 1/sn <= 1 (必要不充分条件)
"""

import sys
import argparse

def sum_reciprocal(arr):
    return  sum([ 1 / float(sp) for sp in arr])

def check(params):
    sp_arr = params.sps
    s = sum_reciprocal(sp_arr)
    print 'sp check value: %f' % s
    return s,s <= 1

def check_arr2(params):
    sp_arra, sp_arrb = params.sp_arra, params.sp_arrb
    arr = []
    for i in sp_arra:
        for j in sp_arrb:
	    arr.append(float(i) * float(j))
    s = sum_reciprocal(arr)
    print 'sp check value: %f' % s
    return s, s<=1

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    parser_check1 = subparsers.add_parser('s1')
    parser_check1.add_argument('sps', nargs='+')
    parser_check1.set_defaults(func=check)

    parser_check2 = subparsers.add_parser('s2')
    parser_check2.add_argument('-a', dest='sp_arra', nargs = '+')
    parser_check2.add_argument('-b', dest='sp_arrb', nargs = '+')
    parser_check2.set_defaults(func=check_arr2)

    args = parser.parse_args()
    args.func(args)
#    sps = [float(i) for i in sys.argv[1:]]
#    s,legal = check(sps)
#    print s,legal

