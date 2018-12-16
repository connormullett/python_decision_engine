
from decision_engine_util import DecisionEngine as Engine

count = 4
values = [ -9, -9, -9, -9, -9, -9]

engine = Engine()

heavy_apples = engine.track_decision(values, count)

for y in range(count):
    for x in range(count):
        print((heavy_apples[x, y]), -20)

total = heavy_apples[4, 0] + heavy_apples[4, 1] + heavy_apples[4, 2] + heavy_apples[4, 3]

