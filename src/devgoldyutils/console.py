import random
import os, sys

class ConsoleColours:
    """Class that contants methods for colouring the text printed to the console."""

    def RANDOM(self, text:str):
        random_num = random.randint(1, 4)

        if random_num == 1: return self.GREEN(text)
        if random_num == 2: return self.BLUE(text)
        if random_num == 3: return self.CLAY(text)
        if random_num == 4: return self.PURPLE(text)

    def PICK_COLOUR(self, colour_name:str, text:str):
        if not colour_name == None:
            if colour_name.lower() in ["green"]:
                return self.GREEN(text)

            if colour_name.lower() in ["blue"]:
                return self.BLUE(text)

            if colour_name.lower() in ["clay"]:
                return self.CLAY(text)

            if colour_name.lower() in ["purple"]:
                return self.PURPLE(text)
        else:
            return self.RANDOM(text)
    
    def GREEN(self, text:str):
        return "\u001b[32m" + str(text) + "\u001b[0m"

    def BLUE(self, text:str):
        return "\u001b[36m" + str(text) + "\u001b[0m"

    def CLAY(self, text:str):
        return "\u001b[38;5;51m" + str(text) + "\u001b[0m"

    def PURPLE(self, text:str):
        return "\u001b[38;5;200m" + str(text) + "\u001b[0m"

    def RED(self, text:str):
        return "\u001b[31m" + str(text) + "\u001b[0m"

class Console(ConsoleColours):
    def __init__(self):
        if sys.platform == "win32": os.system("color")