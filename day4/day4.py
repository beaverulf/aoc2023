import re
#Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
#Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
#Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
def task1(data):
    score = []
    for line in data:
        my_winning_numbers = get_winning_numbers_per_line(line)
        acc = 0
        for x in range(len(my_winning_numbers)):
            if x == 0: acc += 1
            else: acc *= 2
        score.append(acc)
    return score

def get_winning_numbers_per_line(line):
    winning_line, mine_line = line.split(':')[1].split('|')    
    winning_numbers = [int(x) for x in  winning_line.split() if x.isdigit()]
    my_numbers = [int(x) for x in mine_line.split() if x.isdigit()]
    return [i for i in my_numbers if i in winning_numbers]

def task2(data):
        winning_numbers_per_card = {}
        card_copies = {}
        for i, line in enumerate(data):
            card_copies[i] = 1
            winning_numbers_per_card[i] = len(get_winning_numbers_per_line(line))
            
        for card, winnings in winning_numbers_per_card.items():
            for x in range(winnings):
                key = card+x+1
                card_copies[key] += card_copies[card]
        total = sum([x for _,x in card_copies.items()])
        return total

def main():
    with open('./day4/data.txt', encoding="utf-8") as f:
        data = f.read().splitlines()
        task1_score = sum(task1(data))
        task2_score = task2(data)
        print("Task 1",task1_score)
        print("Task 2",task2_score)
main()
