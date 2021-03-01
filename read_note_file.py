# reads in a .txt file of notes to create and play. returns a dictionary of notes, frequencies, and rest intervals

# open a given file and read in values. create and return a dictionary
def process_file(filename):
    file = open(filename)
    notes = {}
    for line in file:
        note, rest = line.split()
        length = len(note)-1
        octave = int(line[length])
        name = line[:length]
        freq = calculate_frequency(name, octave)
        notes[note] = [freq, int(rest)]
    file.close()
    return notes


# calculate the frequency of a note given its name and octave
def calculate_frequency(name, octave):
    middle_c = 261.63
    note_difference = calculate_note_distance(name, octave)
    return round(middle_c * pow(2, (note_difference/12)), 2)


# calculate the number of semitones from middle C (C4) to a given note
def calculate_note_distance(name, octave):
    # assign each note a position
    note_positions = {'A': 1, 'Bb': 2, 'A#': 2, 'B': 3, 'C': 4,
                      'C#': 5, 'Db': 5, 'D': 6, 'D#': 7, 'Eb': 7,
                      'E': 8, 'F': 9, 'F#': 10, 'Gb': 10, 'G': 11,
                      'Ab': 12, 'G#': 12}
    middle_c_position = 4
    middle_c_octave = 4
    # factor needed to correct the direction of the note relative to middle C
    relative_position_factor = -1
    # the number of notes in an octave
    octave_length = 12

    note_position = note_positions[name]

    note_difference = middle_c_position - note_position
    octave_difference = (middle_c_octave - octave) * octave_length
    note_difference = (octave_difference + note_difference) * relative_position_factor

    # if the note comes before middle C, add another octave
    if middle_c_position > note_position:
        return note_difference + octave_length
    else:
        return note_difference
