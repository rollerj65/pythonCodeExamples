
#draw.py
#Module initialization. First time a module is loaded into code, it is run once (initialized).

def draw_game():
     # when clearing the screen we can use the main screen object initialized in this module
     clear_screen(main_screen)

def clear_screen(screen):
    ...

class Screen():
    ...

#initialize main_screen as a singleton
main_screen = Screen()

#extending module load path
#PYTHONPATH=/foo python game.py
#allows the code to retrieve modules from the foo directory as well.

#using sys.path.append
sys.path.append("/foo")
#adds foo directory to the list of paths to look for modules in as well.

#Exploring built-in modules
# important functions: dir and help
#urllib, read data from URLS
import urllib

#use it
urllib.urlopen(...)
dir(urllib)

#help function
help(urllib.urlopen)