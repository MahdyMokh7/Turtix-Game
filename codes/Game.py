import pygame
import sys
from GameManagerPage import GameManagerPage
from LoadingPage import LoadingPage
from StartPage import StartPage
from OptionsPage import OptionsPage
from StoryPage import StoryPage
from GuidePage import GuidePage
from PausePage import PausePage
from VictoryPage import VictoryPage
from GameOverPage import GameOverPage


class Game:

    WIDTH = 1200
    HEIGHT = 700

    def __init__(self):
        self.current_page = None  # Page object
        self.screen = None
        self.running = True
        self.clock = None
        self.fps = 60

        # Instantiate all page classes
        self.game_manager_page = GameManagerPage()
        self.loading_page = LoadingPage()
        self.start_page = StartPage()
        self.options_page = OptionsPage()
        self.story_page = StoryPage()
        self.guide_page = GuidePage()
        self.pause_page = PausePage()
        self.victory_page = VictoryPage()
        self.game_over_page = GameOverPage()

    def initialization(self):
        # Initialize the game
        pass

    def run(self):

        pygame.init()

        self.screen = pygame.display.set_mode((Game.WIDTH, Game.HEIGHT))
        pygame.display.set_caption("Turtix")
        self.clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Call the appropriate run_page method based on the current_page
                if self.current_page == LoadingPage.__name__:
                    self.loading_page.run_page()

                elif self.current_page == StartPage.__name__:
                    self.start_page.run_page()

                elif self.current_page == OptionsPage.__name__:
                    self.options_page.run_page()

                elif self.current_page == StoryPage.__name__:
                    self.story_page.run_page()

                elif self.current_page == GameManagerPage.__name__:
                    self.game_manager_page.run_page()

                elif self.current_page == GuidePage.__name__:
                    self.guide_page.run_page()

                elif self.current_page == PausePage.__name__:
                    self.pause_page.run_page()

                elif self.current_page == VictoryPage.__name__:
                    self.victory_page.run_page()

                elif self.current_page == GameOverPage.__name__:
                    self.game_over_page.run_page()
                    

            self.screen.fill((0, 0, 0))  # Black background

            pygame.display.flip()
            self.clock.flip(self.fps)



