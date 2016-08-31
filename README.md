pyratio_deco
============

A Python Implementation of Ratio Deco.

Currently depth is only displayed in feet.

## CLI APP

The help menu:
```
$ ./maximum_deco.py --help
usage: maximum_deco.py [-h] -t BOTTOM_TIME -d DEPTH
                       [--nosaturation [NOSATURATION]]

optional arguments:
  -h, --help            show this help message and exit
  -t BOTTOM_TIME, --bottom-time BOTTOM_TIME
                        Bottom Time
  -d DEPTH, --depth DEPTH
                        Depth
  --nosaturation [NOSATURATION]
                        Disable saturation of tissues
```

An example profile requiring minimal deco:
```
$ ./maximum_deco.py --depth 100 --bottom-time 30
***************************
Dive Details:
Depth: 100 feet
Bottom Time: 30 minutes
***************************
Stop: 50 feet for one minute
Stop: 40 feet for one minute
Stop: 30 feet for one minute
Stop: 20 feet for one minute
Stop: 10 feet for one minute
```

An example profile requiring staged decompression:
```
$ ./maximum_deco.py --depth 200 --bottom-time 30
***************************
Dive Details:
Depth: 200 feet
Bottom Time: 30 minutes
***************************
First Deco Stop: 100 feet
O2 Segment: 30 minutes
70 Segment: 30 minutes
120 Segment: 15 minutes
Total deco time is 75 minutes.
```
