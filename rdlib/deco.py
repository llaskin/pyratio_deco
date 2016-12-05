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


def o2_segment(depth, bottom_time):
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
    return o2_segment


def calc_deco(depth, bottom_time, nosaturation):
    import math
    deco_data = dict()
    deco_data['depth'] = depth
    deco_data['bottom_time'] = bottom_time
    deco_data['nosaturation'] = nosaturation
    o2_deco = o2_segment(int(depth), int(bottom_time))
    first_stop = int(math.floor((int(depth) * float(.5)) / 10) * 10)
    deco_data['first_stop'] = first_stop

    if int(depth) > 400:
        deco_data['out_of_range'] = "Error: Depth is out of range."

    if int(bottom_time) <= ndl(int(depth)):
        md_stops = list()
        while first_stop > 0:
            md_stops.append(first_stop)
            first_stop = first_stop - 10
        deco_data['minimum_deco'] = md_stops[::-1]
        deco_data['total_deco'] = len(md_stops)
    elif int(depth) <= 400:
        if nosaturation:
            if int(math.ceil(o2_deco)) >= 150:
                o2_deco = 150
                deco_data['20'] = o2_deco
        deco_data['20'] = int(math.ceil(o2_deco))
        total_deco = int(math.ceil(o2_deco))
        if first_stop >= 30 <= 90:
            deco_data['70'] = deco_data['20']
            total_deco = int(math.ceil(o2_deco + o2_deco))
        if first_stop >= 100 <= 140:
            deco_data['120'] = int(math.ceil(o2_deco * .5))
            total_deco = int(math.ceil(total_deco + o2_deco * .5))
        if first_stop >= 150 <= 190:
            deco_data['190'] = int(math.ceil((o2_deco * .5)) * .5)
            total_deco = int(math.ceil(total_deco + o2_deco * .5))
        deco_data['total_deco'] = total_deco
    return deco_data
