#!/usr/bin/env python

""" A python implementation of Ratio Deco """

from rdlib.deco import calc_deco

import argparse


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        '--bottom-time',
        help='Bottom Time',
        required=True)
    parser.add_argument(
        '-d',
        '--depth',
        help='Depth',
        required=True)
    parser.add_argument(
        '--nosaturation',
        help='Disable saturation of tissues',
        nargs='?',
        default=True)
    return vars(parser.parse_args())


if __name__ == '__main__':
    args = arguments()
    deco = calc_deco(depth=args['depth'],
                     bottom_time=args['bottom_time'],
                     nosaturation=args['nosaturation'])
    print('***************************')
    print('Dive Details:')
    print('Depth: {} feet'.format(deco['depth']))
    print('Bottom Time: {} minutes'.format(deco['bottom_time']))
    if 'total_deco' in deco:
        print('Total Deco: {} minutes'.format(deco['total_deco']))
    print('***************************')
    if 'out_of_range' in deco:
        print(deco['out_of_range'])
    if 'minimum_deco' in deco:
        for item in deco['minimum_deco']:
            print('Stop at {} for 1 minute'.format(item))
    else:
        if '20' in deco:
            print(' 20 ft segment: {} minutes'.format(deco['20']))
        if '70' in deco:
            print(' 70 ft segment: {} minutes'.format(deco['70']))
        if '120' in deco:
            print('120 ft segment: {} minutes'.format(deco['120']))
        if '190' in deco:
            print('190 ft segment: {} minutes'.format(deco['190']))
