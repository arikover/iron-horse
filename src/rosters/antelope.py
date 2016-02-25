from roster import Roster

from vehicles import antlion
from vehicles import baby_boat
from vehicles import big_boat
from vehicles import bigfoot
from vehicles import savannah_slammer
from vehicles import smokey_mountain

# speed for wagons in mph (some generations may optionally have no speed set)
# format is [standard, speedy]
speeds = dict(gen_1_wagon_speeds = [55, None], # no point setting an upper speed in this roster, max engine is always 75mph
              gen_2_wagon_speeds = [75, None],
              ng_gen_1_wagon_speeds = [55, 55])

roster = Roster(id = 'antelope',
                numeric_id = 3,
                speeds = speeds,
                engines = [bigfoot,
                           smokey_mountain,
                           baby_boat,
                           big_boat,
                           antlion,
                           savannah_slammer])
