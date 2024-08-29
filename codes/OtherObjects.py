from abc import ABC
from typing import abstractmethod
import os
import pygame


class OtherObject(ABC):
    def __init__(self, pos_x, pos_y, row_num, col_num):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.row_num = row_num
        self.col_num = col_num

    @abstractmethod
    def render(self):
        # Render the object
        pass



class PortableBlock(OtherObject):

    NUM_OF_IMAGES = 3  #########

    @staticmethod
    def process_images() -> list:
        list_of_images = list()
        for i in range(1, PortableBlock.NUM_OF_IMAGES):
            image_path = os.path.join(PortableBlock.FOLDER_PATH, "img" + str(i) + ".png")
            image = pygame.image.load(image_path)
            list_of_images.append(image)
        return list_of_images
            

    images = process_images()  # List of images

    FOLDER_PATH = os.path.join("sources", "sprite", "portable")

    def __init__(self, pos_x, pos_y, row_num, col_num):
        super().__init__(pos_x, pos_y, row_num, col_num)

    def render(self):
        pass


class Thorn(OtherObject):

    @staticmethod
    def process_images() -> list:
        pass ###############

    images = process_images()  # List of images

    DAMAGE = 0 ###############

    def __init__(self, pos_x, pos_y, row_num, col_num, image):
        super().__init__(pos_x, pos_y, row_num, col_num, image)
        self.damage = Thorn.DAMAGE

    def hit(self):
        """Handle what happens when the player touches the thorn."""
        print(f"Player hit the thorn! Damage: {self.damage}")

    def get_damage(self):
        return self.damage
    
    def render(self):
        pass


class BubbleTurtle(OtherObject):

    @staticmethod
    def process_images() -> list:
        pass ###############

    images = process_images()  # List of images

    def __init__(self, pos_x, pos_y, row_num, col_num):
        super().__init__(pos_x, pos_y, row_num, col_num)

    def got_hit(self):
        """Handle what happens when the bubble turtle is hit."""
        print("BubbleTurtle got hit!")

    def render(self):
        pass

class Ladder(OtherObject):

    @staticmethod
    def process_images() -> list:
        pass ###############

    images = process_images()  # List of images

    def __init__(self, pos_x, pos_y, row_num, col_num):
        super().__init__(pos_x, pos_y, row_num, col_num)

    def render(self):
        pass

class Rope(OtherObject):

    @staticmethod
    def process_images() -> list:
        pass ###############

    images = process_images()  # List of images


    def __init__(self, pos_x, pos_y, row_num, col_num):
        super().__init__(pos_x, pos_y, row_num, col_num)

    def render(self):
        pass


class VerticalBlock(OtherObject):

    @staticmethod
    def process_images() -> list:
        pass ###############

    images = process_images()  # List of images

    def __init__(self, pos_x, pos_y, row_num, col_num):
        super().__init__(pos_x, pos_y, row_num, col_num)
        self.activation = False
        self.pointer_image = 0

    def get_activation(self):
        return self.activation

    def render(self):
        image = self.images[self.pointer_image]  # Update the image based on pointer



class Portal(OtherObject):

    @staticmethod
    def process_images() -> list:
        pass ###############

    images = process_images()  # List of images 

    def __init__(self, pos_x, pos_y, row_num, col_num):
        super().__init__(pos_x, pos_y, row_num, col_num)

    def render(self):
        pass
