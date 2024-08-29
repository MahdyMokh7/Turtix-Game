from abc import ABC



class Enemy(ABC):
    def __init__(self, pos_x, pos_y, row_num, col_num, health):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.row_num = row_num
        self.col_num = col_num
        self.health = health

    def move(self):
        # Move the enemy
        pass

    def got_hit(self):
        # Handle being hit
        pass

    def got_kick(self):
        # Handle being kicked
        pass

    def hit_turtle(self):
        # Hit the turtle
        pass

    def render(self):
        # Render the enemy
        pass

    def get_reward(self):
        # Reward for killing the enemy
        pass



class EnemyType1(Enemy):

    @staticmethod
    def process_images() -> list:
        pass ###############

    images = process_images()  # List of images

    HEALTH = 2

    def __init__(self, pos_x, pos_y, row_num, col_num):
        super().__init__(pos_x, pos_y, row_num, col_num, EnemyType1.HEALTH)
        self.images = []  # List of images
        self.pointer_of_image = 0

    def move(self):
        # Move the enemy
        pass


class EnemyType2:

    @staticmethod
    def process_images() -> list:
        pass ###############

    images = process_images()  # List of images

    HEALTH = 2

    def __init__(self, pos_x, pos_y, row_num, col_num):
        super().__init__(pos_x, pos_y, row_num, col_num, EnemyType1.HEALTH)
        self.images = []  # List of images
        self.pointer_of_image = 0

    def move(self):
        pass
        # Move the enemy
