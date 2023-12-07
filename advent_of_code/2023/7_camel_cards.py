## 7th task of advent of code

task_file = "advent_of_code/2023/inputs/7_task.txt"

class CardHand:
    def __init__(self, hand, bid, is_j_joker=False):
        if not is_j_joker:
            self.rank_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
                            '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
        else:
            self.rank_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10,
                            '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    

        if len(hand) != 5 or any(card not in self.rank_map for card in hand):
            raise ValueError("Invalid hand")

        self.rank_order = [self.rank_map[card] for card in hand]
        
        if not is_j_joker:
            self.card_counts = sorted([hand.count(card) for card in set(hand)])[::-1]
        else:
            self.card_counts = sorted([hand.count(card) for card in set(hand) if card!="J"])[::-1]
            self.joker_count = hand.count("J")
            if self.joker_count == 5:
                self.card_counts = [5]
            else:
                for i in range(self.joker_count):
                    for n in range(len(self.card_counts)):
                        if self.card_counts[n]<5:
                            self.card_counts[n]+=1
                            break


        self.set = self.evaluate_set()

        self.hand = hand

        self.bid = bid

    def evaluate_set(self):
        if 5 in self.card_counts:
            return 6
        elif 4 in self.card_counts:
            return 5
        elif 3 in self.card_counts and 2 in self.card_counts:
            return 4
        elif 3 in self.card_counts:
            return 3
        elif 2 in self.card_counts:
            if self.card_counts.count(2) == 2:
                return 2
            else:
                return 1
        else:
            return 0


    def __str__(self):
        return f"Card:{self.hand}\nRank Order: {self.rank_order}\nCard Counts: {self.card_counts}\nSet value:{self.set}"

    def __gt__(self, other):
        if self.set > other.set:
            return True
        elif self.set < other.set:
            return False
        else:
            for i in range(len(self.rank_order)):
                if self.rank_order[i] > other.rank_order[i]:
                    return True
                elif self.rank_order[i] < other.rank_order[i]:
                    return False
            return False
## Part one
with open(task_file) as f:
    lines = [line.replace("\n","") for line in f]
    cards = [CardHand(line.split(" ")[0], line.split(" ")[1]) for line in lines]

print(sum([int(cards_set.bid)*(n+1) for n, cards_set in enumerate(sorted(cards))]))

# Part two 

with open(task_file) as f:
    lines = [line.replace("\n","") for line in f]
    cards = [CardHand(line.split(" ")[0], line.split(" ")[1], is_j_joker=True) for line in lines]

print(sum([int(cards_set.bid)*(n+1) for n, cards_set in enumerate(sorted(cards))]))
