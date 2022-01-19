def inserction(cards,cards_order,cards_pre):
    for i in range(1, len(cards)):
        key = cards[i]
        j = i - 1
        while j >= 0 and (cards_order[key[0]] < cards_order[cards[j][0]] or (cards_order[key[0]] == cards_order[cards[j][0]]
                and cards_pre[key[1:]] < cards_pre[cards[j][1:]])):
            cards[j + 1] = cards[j]
            j = j - 1
        cards[j + 1] = key
    return cards
cards_pre = {"A": 1,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 
                    7,"8": 8,"9": 9,"10": 10,"J": 11,"Q": 12,"K": 13,}
cards_order = {"S": 1, "H": 2, "D": 3, "C": 4}
cards = []
n = int(input("Enter size of the array:"))
print("Enter card name first letter followed by card number:")
print("Example:S10(S-Spade,10-card number")
for i in range(n):
    cards.append(input("Enter card:"))
print("Sorted cards:",inserction(cards,cards_order,cards_pre))
