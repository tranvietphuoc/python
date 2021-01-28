from dataclasses import dataclass
from dataclasses import make_dataclass
from typing import Any, List
from math import asin, cos, radians, sin, sqrt


@dataclass
class Transaction:
    sender: Any
    amount: Any
    reciever: Any


# now instantiate
trans = Transaction("Phuoc", 3000000, "Tuyen")
print(trans.sender, trans.amount, trans.reciever)
print(trans)
print(trans == Transaction("Phuoc", 3000000, "Tuyen"))

# Position = make_dataclass("Position", ["name", "lat", "lon"])
# print(Position)


@dataclass
class Position:
    name: Any
    lon: Any = 0.0
    lat: Any = 0.0

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lamb_1, lamb_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (
            sin((phi_2 - phi_1) / 2) ** 2
            + cos(phi_1) * cos(phi_2) * sin((lamb_2 - lamb_1) / 2) ** 2
        )
        return 2 * r * asin(sqrt(h))


oslo = Position("Oslo", 10.8, 59.9)
vancouver = Position("Vancouver", -123.1, 49.3)
print(oslo.distance_to(vancouver))

# more flexible data classes
@dataclass
class PlayingCard:
    rank: Any
    suit: Any


@dataclass
class Deck:
    cards: List[PlayingCard]


queen_of_hearts = PlayingCard("Q", "Hearts")
ace_of_spades = PlayingCard("A", "Spades")
two_cards = Deck([queen_of_hearts, ace_of_spades])
print(two_cards)

# Advanced default
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "♣ ♢ ♡ ♠".split()


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


print(make_french_deck())
