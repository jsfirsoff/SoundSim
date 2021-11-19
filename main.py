# expanded upon from Mahesh Venkitachalam's 'Python Playground', chapter 4
#
# create and play notes
# arguments: --display          sets up matplotlib plot to show how
#                               the waveform evolves during the Karplus-Strong algorithm
#            --play             plays a note at random from the dictionary
#            --piano            plays a random note per key pressed; press 'q' to quit
#            --file [filepath]  takes a filepath as an input. file must include notes followed
#                               by a rest time on each line

import os
import time
import argparse
import keyboard
from matplotlib import pyplot as plt
import numpy as np
import write_WAV as wwav
import karplus_strong as ks
import NotePlayer
import read_note_file as rnf

# show plot of algorithm in action?
show_plot = False

# notes of Pentatonic Minor scale
# piano C4-E(b)-F-G-B(b)-C5
musical_notes = {'C4': [262.11, 0], 'Eb': [311.54, 0], 'F': [349.32, 0], 'G': [391.76, 0], 'Bb': [466.32, 0]}

path = "Notes\\"


def main():
    global show_plot
    # create parser
    parser = argparse.ArgumentParser(description
                                     ="Generating sounds with Karplus Strong Algorithm")
    # add command line arguments
    parser.add_argument('--display', action='store_true', required=False)
    parser.add_argument('--play', action='store_true', required=False)
    parser.add_argument('--piano', action='store_true', required=False)
    parser.add_argument('--file', help="Filepath with notes.", type=str)
    args = parser.parse_args()

    # show plot if flag set
    if args.display:
        show_plot = True
        plt.ion()

    if args.file:
        global musical_notes
        musical_notes = rnf.process_file(args.file)

    # create note player
    nplayer = NotePlayer.NotePlayer()

    print('creating notes...')
    for note, freq in list(musical_notes.items()):
        filename = path + note + '.wav'
        print(filename)
        if not os.path.exists(filename) or args.display:
            data = ks.generate_note(freq[0], show_plot, plt)
            print('creating ' + filename + '...')
            wwav.write_wav(filename, data)
        else:
            print('filename already exists. skipping...')

        # add note to player
        nplayer.add_note(filename)

        # play note if display flag is set
        if args.display:
            nplayer.play_note(filename)
            time.sleep(0.5)

    if args.display:
        plt.pause(100)

    # play a random tune
    if args.play:
        while True:
            try:
                nplayer.play_random()
                # rest - 1 to 8 beats with probabilities: 2 beat with highest and 8 beat lowest
                rest = np.random.choice([1, 2, 4, 8], 1, p=[0.15, 0.7, 0.1, 0.05])
                time.sleep(0.25 * rest[0])
            except KeyboardInterrupt:
                exit()

    # random piano mode
    if args.piano:
        while True:
            event = keyboard.read_event()
            if event.name == 'q':
                exit()
            print("key pressed")
            nplayer.play_random()
            time.sleep(0.1)

    if args.file:
        for note in nplayer.notes:
            nplayer.play_note(note)
            # slice off path from note
            # slice off '.wav' of the note name to get the dict key to retrieve the rest value
            path_len = len(path)
            time.sleep(0.25 * musical_notes[note[path_len:-4]][1])


if __name__ == '__main__':
    main()
