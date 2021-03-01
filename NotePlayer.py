# play a WAV file

import pygame
import random


class NotePlayer:

    frequency = 44100  # sampling rate
    size = -16  # 16-bit signed values
    channels = 1
    buffer_size = 2048

    # constructor
    def __init__(self):
        pygame.mixer.pre_init(self.frequency, self.size, self.channels, self.buffer_size)
        pygame.init()
        # create dictionary of notes to store pygame sound objects and filenames
        self.notes = {}
    
    # create a sound file and add a note to dictionary
    def add_note(self, filename):
        self.notes[filename] = pygame.mixer.Sound(filename)
    
    # play a note from the dictionary, given the filename
    def play_note(self, filename):
        try:
            self.notes[filename].play()
        except:
            print(filename + ' not found ')
    
    # play a random note from the dictionary
    def play_random(self):
        index = random.randint(0, len(self.notes)-1)
        note = list(self.notes.values())[index]
        note.play()
