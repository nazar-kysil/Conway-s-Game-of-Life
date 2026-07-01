from game_rules import *
from animation import *

while True:
    question = input(f"Do you want to create your own template or look at basic ones? m/b\n"
                     f"'m' - own, 'b' - basic ones\n")
    if question not in ["m", "b"]:
        print("Please enter either 'b' or 'm': ")
    else:
        break
if question == 'm':
    while True:
        try:
            x, y = map(int, input("Please define the size of field 'x y': ").split())
            if x <= 0 or y <= 0:
                print("Please enter only positive integers ")
            else:
                break
        except ValueError:
            print("Please enter two integers separated by a space")
    game = GameOfLife(x, y)
    display = Display(game)
    display.run()
else:
    while True:
        question2 = input("Do you want to look at glider, gosper glider gun or pulsar?\n"
                          "g - glider, ggg - gosper glider gun, p - pulsar\n")
        if question2 not in ["g", "ggg", "p"]:
            print("Please enter either 'g' or 'ggg' or 'p': ")
        else:
            break
    if question2 == 'g':
        file = FileGameOfLife("glider")
        display = Display(file, start_paused=False)
        display.run()
    elif question2 == 'ggg':
        file = FileGameOfLife("gosper-glider-gun")
        display = Display(file, start_paused=False)
        display.run()
    else:
        file = FileGameOfLife("pulsar")
        display = Display(file, start_paused=False)
        display.run()



