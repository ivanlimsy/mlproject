from mlproject.distance import haversine
import math


def test_haversine():
    assert math.floor(haversine(1,2,3,4)) == 314
