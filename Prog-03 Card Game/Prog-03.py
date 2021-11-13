# Prog-03: Card Game

import time
import random

def generate_deck(n_cards, n_shuffles):
    print('Shuffle', end='')
    deck = ''
    for suit in 'CDHS':
        for face in 'A23456789TJQK':
            deck += '|' + face + suit + '|'
    for i in range(n_shuffles):
        deck = cut(deck, random.randint(0,n_cards))
        deck = shuffle(deck)
        time.sleep(0.1)
        print('.', end='')
    print()
    return deck[:4*n_cards]

def play(n_cards):
    print('Start a card game.')
    deck = generate_deck(n_cards, 20)

    p1, deck = deal_n_cards(deck, 5)
    p2, deck = deal_n_cards(deck, 5)
    players = [p1, p2]
    
    table_cards, deck = deal_n_cards(deck, 1)
    fail = False
    turn = 0
    
    while True:
        show_table_cards(table_cards, 10)
        show_player_cards(players[turn], turn+1)
        k = select_card_number(players[turn])
        valid = (k != 0)
        if valid:
            cards = players[turn]
            card = peek_kth_card(cards, k)
            valid = eq_suit_or_value(card, table_cards[-4:])
            if valid:
                table_cards += card
                players[turn] = remove_kth_card(cards, k)
                fail = False
        if not valid:
            print('  ** Invalid **')
            if len(deck) == 0:
                if fail: break
                fail = True
            if len(deck) > 0:
                print('  >> get a new card')
                card, deck = deal_n_cards(deck, 1) 
                players[turn] = card + players[turn]
                
        show_player_cards(players[turn], turn+1)
        if len(players[turn]) == 0: break
        turn = (turn + 1) % len(players)

    if len(deck) == 0:
        print('\n** No more cards **')
    print('*****************')
    if len(deck) == 0 and \
         len(players[0]) == len(players[1]):
            print('Draw!!!')
    elif len(players[0]) < len(players[1]):
        print('Player # 1 win!!!')
    else:
        print('Player # 2 win!!!')        

def eq_suit_or_value(card1, card2):
    return card1[1] == card2[1] or \
                 card1[2] == card2[2]

def show_player_cards(cards, k):
    print('  Player #', k, ':', cards)

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            pass

def select_card_number(cards):
    n = len(cards)//4
    k = input_int('  Select card # (1-'+ str(n)+') : ')
    if not(1 <= k <= n): k = 0
    return k

#---------------------------------------
def peek_kth_card(cards, k):
    
    cards = cards[1:-1].split('||')
    the_kth_card = '|'+cards[k-1]+'|'

    return the_kth_card
#---------------------------------------
def remove_kth_card(cards, k):

    cards = cards.split('|')
    new_cards = cards[:2*k-1]+ cards[2*k+1:]
    new_cards = '|'.join(new_cards)
    
    return new_cards
#---------------------------------------
def deal_n_cards(deck, n):

    deck = deck.split('|')
    cards = deck[:(2*n)+1]
    cards = ('|').join(cards)
    new_deck = deck[(2*n):]
    new_deck = ('|').join(new_deck)

    return cards, new_deck
#---------------------------------------
def cut(deck, m):
    
    deck = deck[1:-1].split('||')
    new_deck = deck[m:]+deck[:m]
    new_deck = '|'+(('||').join(new_deck)) + '|'

    return new_deck
#---------------------------------------
def shuffle(deck):

    deck = deck[1:-1].split('||')
    x = int((len(deck)+1)//2)
    y = deck[:x]
    z  = deck[x:]
    a = ['']*(len(y+z))
    a[::2] = y[::1]
    a[1::2] = z[::1]
    b = (len(a)*2)*['']+['']
    b[1::2] = a[::1]
    new_deck = ('|').join(b)

    return new_deck
#---------------------------------------
def show_table_cards(cards, m):

    y = cards[1:-1].split('||')
    cards = y[-m:]
    x = ('||').join(cards)
    z = 'Table: '+(min(max((len(y)-m),0),1)*'....')+'|'+x+'|'
    print('-'*len(z))
    print(z)
    print('-'*len(z))
    
#-----------------------------------------    
play(51)