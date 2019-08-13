from random import choice
pics=['''
=========||
    |    ||
         ||
         ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
         ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
    |    ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|    ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
         ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
   /     ||
         ||
         || ''',
'''
=========||
    |    ||
    0    ||
   /|\   ||
   / \   ||
         ||
         ||'''
]
word_list = [ ' panamera', 'metindoiarena', 'macarena', 'onomatopee']

def extrage_cuv():
    return choice(word_list)
how_dead_am_i = 0

def play_game():
    cuv = extrage_cuv()
    litere_ghicite = []
    how_dead_am_i = 0
    castigat = True
    while how_dead_am_i < len (pics):
        print(pics[how_dead_am_i])
        castigat = True
        for ch in cuv:
            if ch in litere_ghicite:
                print('_' , end='')
            else:
                print('_', end='')
                castigat = False

        print()

        if castigat:
            print("Bravo!")
            break

        letter = input("Zi o litera?")
        if letter in cuv and letter not in letter_ghicite:
            litere_ghicite.append(letter)

        else:
            how_did_am_i +=1
        if not castigat :
            print (pics[how_did_am_i])
            print ("Ai murit !")

play_game()

