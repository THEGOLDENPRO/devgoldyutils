import random
from ..colours import Colours

class LegacyColours:
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
        return Colours.GREEN.apply(text)

    def BLUE(self, text:str):
        return Colours.BLUE.apply(text)

    def CLAY(self, text:str):
        return Colours.CLAY.apply(text)

    def PURPLE(self, text:str):
        return Colours.PURPLE.apply(text)

    def RED(self, text:str):
        return Colours.RED.apply(text)