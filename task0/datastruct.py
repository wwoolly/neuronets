from enum import Enum

SUN, OVERCAST, RAIN = 0, 1, 2
COLD, SWEET, HOT = 0, 1, 2
HIGH, NORMAL, LOW = 0, 1, 2

OUTLOOK, TEMPERATURE, HUMIDITY, WIND, PLAY = \
    'outlook', 'temperature', 'humidity', 'wind', 'play'

class Attribute(Enum):
    OUTLOOK = 0
    TEMPERATURE = 1
    HUMIDITY = 2
    WIND = 3

    def get_attrs_count(self):
        attrs_number = {
            Attribute.OUTLOOK: 3,
            Attribute.TEMPERATURE: 3,
            Attribute.HUMIDITY: 2,
            Attribute.WIND: 2
        }
        return attrs_number[self]


class Weather:
    outlook: int
    temperature: int
    humidity: int
    wind: int
    play: bool

    def __init__(self, o, t, h, w, b):
        self.outlook = o
        self.temperature = t
        self.humidity = h
        self.wind = w
        self.play = b

    def is_correct(self):
        o = (self.outlook >= 0 & self.outlook <= 2)
        t = (self.temperature >= 0 & self.temperature <= 2)
        h = (self.humidity >= 0 & self.humidity <= 2)
        w = (self.wind >= 0 & self.wind <= 2)

        return o & t & h & w


class TreeNode:
    attribute: Attribute
    value: int
    desc: list

    def __init__(self, attr, v, desc=None):
        if desc is None:
            desc = list()
        self.attribute = attr
        self.value = v
        self.desc = desc
