import pygame
import os


class AudioManager:

    # Define static fields for paths
    IN_GAME_MUSIC_PATH = os.path.join("..", "sources", "Audio files", "in_game_music.mp3")
    START_PAGE_MUSIC_PATH = os.path.join("..", "sources", "Audio files", "start_page_music.mp3")
    STORY_MODE_MUSIC_PATH = os.path.join("..", "sources", "Audio files", "story_mode_music.mp3")
    VICTORY_MUSIC_PATH = os.path.join("..", "sources", "Audio files", "victory_music.mp3")
    SLEEP_TURTLE_MUSIC_PATH = os.path.join("..", "sources", "Audio files", "sleep_turtle_music.mp3")

    ITEM_CLICK_SOUND_PATH = os.path.join("..", "sources", "Audio files", "item_click_sound.wav")
    GOT_HIT_SOUND_PATH = os.path.join("..", "sources", "Audio files", "got_hit_sound.wav")
    PRIZE_PICKING_SOUND_PATH = os.path.join("..", "sources", "Audio files", "prize_picking_sound.wav")
    HIT_ENEMY_SOUND_PATH = os.path.join("..", "sources", "Audio files", "hit_enemy_sound.wav")
    BABY_COLLECTING_SOUND_PATH = os.path.join("..", "sources", "Audio files", "baby_collecting_sound.wav")

    # Define constants for dictionary keys
    IN_GAME = 'IN_GAME'
    START_PAGE = 'START_PAGE'
    STORY_MODE = 'STORY_MODE'
    VICTORY = 'VICTORY'
    SLEEP_TURTLE = 'SLEEP_TURTLE'
    
    ITEM_CLICK = 'ITEM_CLICK'
    GOT_HIT = 'GOT_HIT'
    PRIZE_PICKING = 'PRIZE_PICKING'
    HIT_ENEMY = 'HIT_ENEMY'
    BABY_COLLECTING = 'BABY_COLLECTING'

    def __init__(self):
        self.dict_music_type = {}
        self.dict_sound_type = {}
        self.is_sound_enable = True
        self.is_music_enable = True
        self.already_playing = False  # New field to track if music is playing
        pygame.mixer.init()
        
        self._load_resources()

    def _load_resources(self):
        # Load and store music
        self.dict_music_type = {
            AudioManager.IN_GAME: pygame.mixer.music.load(AudioManager.IN_GAME_MUSIC_PATH),
            AudioManager.START_PAGE: pygame.mixer.music.load(AudioManager.START_PAGE_MUSIC_PATH),
            AudioManager.STORY_MODE: pygame.mixer.music.load(AudioManager.STORY_MODE_MUSIC_PATH),
            AudioManager.VICTORY: pygame.mixer.music.load(AudioManager.VICTORY_MUSIC_PATH),
            AudioManager.SLEEP_TURTLE: pygame.mixer.music.load(AudioManager.SLEEP_TURTLE_MUSIC_PATH),
        }
        
        # Load and store sounds
        self.dict_sound_type = {
            AudioManager.ITEM_CLICK: pygame.mixer.Sound(AudioManager.ITEM_CLICK_SOUND_PATH),
            AudioManager.GOT_HIT: pygame.mixer.Sound(AudioManager.GOT_HIT_SOUND_PATH),
            AudioManager.PRIZE_PICKING: pygame.mixer.Sound(AudioManager.PRIZE_PICKING_SOUND_PATH),
            AudioManager.HIT_ENEMY: pygame.mixer.Sound(AudioManager.HIT_ENEMY_SOUND_PATH),
            AudioManager.BABY_COLLECTING: pygame.mixer.Sound(AudioManager.BABY_COLLECTING_SOUND_PATH),
        }

    def play_music(self, music_type):
        """Play a specific type of music."""
        if not self.is_music_enable:
            return
        if self.already_playing and music_type in self.dict_music_type:
            # If already playing the same music, do nothing
            return
        
        music_path = self.dict_music_type.get(music_type)
        if music_path:
            pygame.mixer.music.load(music_path)  # Load the music file
            pygame.mixer.music.play(-1)  # Loop indefinitely
            self.already_playing = True

    def play_sound(self, sound_type):
        """Play a specific sound effect."""
        if not self.is_sound_enable:
            return
        sound = self.dict_sound_type.get(sound_type)
        if sound:
            sound.play()

    def stop_music(self):
        """Stop the currently playing music."""
        pygame.mixer.music.stop()
        self.already_playing = False

    def mute_unmute_music(self):
        """Mute or unmute the music."""
        if self.is_music_enable:
            pygame.mixer.music.pause()
            self.is_music_enable = False
        else:
            pygame.mixer.music.unpause()
            self.is_music_enable = True

    def mute_unmute_sound(self):
        """Mute or unmute the sound effects."""
        self.is_sound_enable = not self.is_sound_enable
