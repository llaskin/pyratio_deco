#!/usr/bin/env python

""" A python implementation of Ratio Deco """

import math
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


def ndl(depth):
    if depth <= 50:
        no_deco = 150
    elif depth <= 60:
        no_deco = 70
    elif depth <= 70:
        no_deco = 60
    elif depth <= 80:
        no_deco = 40
    elif depth <= 90:
        no_deco = 35
    elif depth <= 100:
        no_deco = 30
    elif depth <= 110:
        no_deco = 25
    elif depth <= 120:
        no_deco = 20
    elif depth <= 130:
        no_deco = 15
    else:
        no_deco = None
    return no_deco


def o2_deco(depth, bottom_time):
    ascent_time = (depth * .5) / 10
    if depth <= 100:
        o2_segment = float(.5 * (bottom_time - ndl(depth) + ascent_time))
    elif depth <= 150:
        o2_segment = .5 * bottom_time
    elif depth <= 200:
        o2_segment = 1 * bottom_time
    elif depth <= 250:
        o2_segment = 1.2 * bottom_time
    elif depth <= 300:
        o2_segment = 1.5 * bottom_time
    elif depth <= 350:
        o2_segment = 2.2 * bottom_time
    elif depth <= 400:
        o2_segment = 3 * bottom_time
    else:
        o2_segment = None
        print("Error: The depth of {} is out of the scope of this app.")
    return o2_segment

if __name__ == '__main__':
    args = arguments()
    depth = int(args['depth'])
    bottom_time = int(args['bottom_time'])
    o2_deco = o2_deco(depth, bottom_time)
    ndl(depth)
    first_stop = math.floor((depth * float(.5)) / 10) * 10
    first_stop = int(first_stop)

    if bottom_time <= ndl(depth):
        print("Dive Details:")
        print("Depth: {} feet".format(depth))
        print("Bottom Time: {} minutes".format(int(math.ceil(bottom_time))))
        while first_stop > 0:
            print("Stop {} feet for one minute.".format(first_stop))
            first_stop = first_stop - 10
    elif depth <= 400:
        if args['nosaturation']:
            if int(math.ceil(o2_deco)) >= 150:
                print("INFO: Saturation reached.")
                o2_deco = 150
        print("Dive Details:")
        print("Depth: {} feet".format(depth))
        print("Bottom Time: {} minutes".format(int(math.ceil(bottom_time))))
        print("First Deco Stop: {} feet".format(first_stop))
        print("O2 Segment: {} minutes".format(int(math.ceil(o2_deco))))
        total_deco = int(o2_deco)
        if first_stop >= 30 <= 90:
            print("70 Segment: {} minutes".format(int(o2_deco)))
            total_deco = o2_deco + int(o2_deco)
        if first_stop >= 100 <= 140:
            print("120 Segment: {} minutes".format(
                int(math.ceil(int(o2_deco) * .5))))
            total_deco = total_deco + int(math.ceil(int(o2_deco) * .5))
        if first_stop >= 150 <= 190:
            print("190 Segment: {} minutes".format(
                int(math.ceil(int(math.ceil(int(o2_deco) * .5)) * .5))))
            total_deco = total_deco + \
                int(math.ceil(int(math.ceil(int(o2_deco) * .5))))
        print("Total deco time is {} minutes.".format(int(total_deco)))
