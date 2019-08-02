
#game.py
#import the draw module

#game imports draw module, and retrieves it from the local folder. the play_game() function is local. to retrieve the draw_game function from draw, first draw must be imported.
#then you can call draw_game through draw.draw_game(result)
import draw
#import package foo, module bar
import foo.bar
# using from
from foo import bar


#import only one function. This allows you to ignore declaring draw.draw_game, but will be overwritten if two functions of the same name exist.
from draw import draw_game

#import all functions from draw. This is risky, and can affect the module you import from.
from draw import *

#custom import name
if visualMode:
    #in visual mode, we draw using graphics
    import draw_visual as draw
else:
    #in textual mode, we print out text
    import draw_textual as draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

#if this script is executed, then main() will be executed
if _name_ == '_main_':
    main()


