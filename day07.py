""" Day 07 setup """

import functools
from advent import Advent, Runner, file_to_string

class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.hand_type_jacks = self.get_type_jacks(hand)
        self.hand_type_jokers = self.get_type_jokers(hand)

    def get_type_jacks(self, hand):
        cards = {}
        for c in hand:
            if c in cards:
                cards[c] += 1
            else:
                cards[c] = 1
        
        if len(cards) == 1:
            return "five-of-a-kind",6
        elif len(cards) == 2:
            if max(cards.values()) == 4:
                return "four-of-a-kind",5
            else:
                return "full house",4
        elif len(cards) == 3:
            if max(cards.values()) == 3:
                return "three-of-a-kind",3
            else:
                return "two pair",2
        elif len(cards) == 4:
            return "one pair",1
        else:
            return "high card",0

    def get_type_jokers(self, hand):
        cards = {}
        for c in hand:
            if c in cards:
                cards[c] += 1
            else:
                cards[c] = 1

        t,r = self.get_type_jacks(hand)
        if 'J' not in hand:
            return t,r

        jokers = cards['J']
        best_count = 0
        if jokers < 5:
            best_count = max(cards[c] for c in cards if c != 'J')

        if best_count + jokers == 5:
            return "five-of-a-kind", 6
        elif best_count + jokers == 4:
            return "four-of-a-kind", 5
        elif best_count + jokers == 3 and len(cards) == 3:
            return "full house", 4
        elif len(cards) == 4:
            if best_count + jokers == 3:
                return "three-of-a-kind", 3
        elif jokers == 1:
            return "one pair", 1
        else:
            return "high card", 0


def compare_hand_jacks(first, second):
    card_order = '23456789TJQKA'
    _, my_type = first.hand_type_jacks
    _, other_type = second.hand_type_jacks
    if my_type == other_type:
        my_hand, other_hand = first.hand, second.hand
        card_number = 0
        while my_hand[card_number] == other_hand[card_number]:
            card_number += 1
        return card_order.find(my_hand[card_number]) - card_order.find(other_hand[card_number])
    else:
        return my_type - other_type

def compare_hand_jokers(first, second):
    card_order = 'J23456789TQKA'
    _, my_type = first.hand_type_jokers
    _, other_type = second.hand_type_jokers
    if my_type == other_type:
        my_hand, other_hand = first.hand, second.hand
        card_number = 0
        while my_hand[card_number] == other_hand[card_number]:
            card_number += 1
        return card_order.find(my_hand[card_number]) - card_order.find(other_hand[card_number])
    else:
        return my_type - other_type

def compare_hand_jokers(first, second):
    card_order = 'J23456789TQKA'
    _, my_type = first.hand_type_jokers
    _, other_type = second.hand_type_jokers
    if my_type == other_type:
        my_hand, other_hand = first.hand, second.hand
        card_number = 0
        while my_hand[card_number] == other_hand[card_number]:
            card_number += 1
        return card_order.find(my_hand[card_number]) - card_order.find(other_hand[card_number])
    else:
        return my_type - other_type


class Day07(Advent):
    """ Day 07 solution class """

    def __init__(self, input_text):
        super().__init__()
        self.input_lines = input_text
        self.name = "07"
        self.hands = []

    def parse(self):
        for line in self.input_lines:
            h, b = line.strip().split()
            hand = Hand(h, int(b))
            self.hands.append( hand )

    def part_one(self):
        self.hands.sort(key=functools.cmp_to_key(compare_hand_jacks))
        winnings = 0
        for i in range(len(self.hands)):
            hand = self.hands[i]
            winnings += (i+1) * hand.bid
        print(f"total winnings: {winnings}")
        return winnings

    def part_two(self):
        self.hands.sort(key=functools.cmp_to_key(compare_hand_jokers))
        winnings = 0
        for i in range(len(self.hands)):
            hand = self.hands[i]
            winnings += (i+1) * hand.bid
            # print(f"rank {i+1}  hand {hand.hand}  bid {hand.bid}  winnings {winnings}")
        print(f"total joker winnings: {winnings}")
        return winnings


def main():
    """ stub for main() """
    aoc07 = Day07(file_to_string("data\\day07.txt"))
    runner = Runner(aoc07)
    runner.run()


if __name__ == '__main__':
    main()
