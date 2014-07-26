#!/usr/bin/env python

''' A python implementation of Ratio Deco '''

import math, argparse

depth = ''
bottom_time = ''

def arguments():
	global depth, bottom_time
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--bt', help="Bottom Time", required=True)
	parser.add_argument('-d', '--depth' ,help="Depth", required=True)
	
	args = vars(parser.parse_args())

	if args['bt']:
		bottom_time = args['bt']
	if args['depth']:
		depth = args['depth']

	return depth, bottom_time
	
arguments()

depth = int(depth)
bottom_time = int(bottom_time)

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
		print "Error: The depth of", depth, "is out of the scope of this app."
	return o2_segment
	return depth
	return bottom_time

o2_deco = o2_deco(depth, bottom_time)
ndl(depth)
first_stop = math.floor((depth * float(.5)) / 10) * 10
first_stop = int(first_stop)

if bottom_time <= ndl(depth):
	print "Your dive is a no-decompression dive. Your depth is", depth, "feet and your bottom time is", bottom_time,"minutes."
	print "Your deco profile is printed below."
	while first_stop > 0:
		print "Stop", first_stop, "feet for one minute."
		first_stop = first_stop - 10
elif depth <= 400:
	if int(math.ceil(o2_deco)) >= 150:
		print "Your O2 Segment is 150 minutes, therefore reached max deco and will not incur any more deco."
		o2_deco = 150
	print "Dive Details:"
	print "Depth:", depth, "feet"
	print "Bottom Time:", int(math.ceil(bottom_time)), "minutes"
        print "First Deco Stop:", first_stop, "feet"
	print "O2 Segment:", int(math.ceil(o2_deco)), "minutes"
	total_deco = int(o2_deco)
	if first_stop >= 30 <= 90:
		seventy_segment = int(o2_deco)
		print "70 Segment:", seventy_segment, "minutes"
		total_deco = o2_deco + seventy_segment
	if first_stop >= 100 <= 140:
		onetwenty_segment = int(math.ceil(seventy_segment * .5))
		print "120 Segment:", onetwenty_segment, "minutes"
		total_deco = total_deco + onetwenty_segment
	if first_stop >= 150 <= 190:
		oneninety_segment = int(math.ceil(onetwenty_segment * .5))
		print "190 Segment:", oneninety_segment, "minutes"
		total_deco = total_deco + oneninety_segment
	print "Your total deco time is", int(total_deco), "minutes."
