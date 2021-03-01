# use given data to write to a WAV file
# single-channel (mono), 16-bit, and uncompressed format

import wave

mode = 'wb'
num_channels = 1
sample_width = 2
frame_rate = 44100  # sampling rate
num_frames = 44100  # number of samples


def write_wav(filename, data):
    file = wave.open(filename, mode)
    file.setparams((num_channels, sample_width, frame_rate, num_frames, 
                    'NONE', 'uncompressed'))
    file.writeframes(data)
    file.close()
