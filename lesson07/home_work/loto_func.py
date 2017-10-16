import random
def card_player():
    a = []
    while len(a) < 15:
        x = random.randint(1, 90)
        if x not in a:
            a.append(x)
    print(a)

def card_computer():
    b = []
    while len(b) < 15:
        x = random.randint(1, 90)
        if x not in b:
            b.append(x)
    print(b)