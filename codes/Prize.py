class Prize:
    def __init__(self, pos_x, pos_y, row_num, col_num, prize_amount):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.row_num = row_num
        self.col_num = col_num
        self.prize_amount = prize_amount

    def got_hit(self):
        # Handle being hit
        pass

    def render(self):
        # Render the prize
        pass


class Diamond:

    @staticmethod
    def process_images() -> list:
        pass ###############

    PRIZE_AMOUNT = 10
    images = process_images()  # List of images
    
    def __init__(self, pos_x, pos_y, row_num, col_num):
        super().__init__(pos_x, pos_y, row_num, col_num, Diamond.PRIZE_AMOUNT)
        self.pointer_of_image = 0

    def got_hit(self):
        # Handle when the diamond is hit
        pass

    def render(self, screen):
        # Render the diamond on the screen
        current_image = self.images[self.pointer_of_image]
        screen.blit(current_image, (self.pos_x, self.pos_y))


class Star:

    @staticmethod
    def process_images() -> list:
        pass ###############

    PRIZE_AMOUNT = 5
    images = process_images()  # List of images


    def __init__(self, pos_x, pos_y, row_num, col_num):
        super().__init__(pos_x, pos_y, row_num, col_num, Star.PRIZE_AMOUNT)
        self.pointer_of_image = 0

    def got_hit(self):
        # Handle when the star is hit
        pass

    def render(self, screen):
        # Render the star on the screen
        current_image = self.images[self.pointer_of_image]
        screen.blit(current_image, (self.pos_x, self.pos_y))


