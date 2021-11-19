# implementation of the Karplus-Strong algorithm
# draws waveform if display flag is set

from collections import deque
import random
import numpy as np
import convert_resolution_to_bytes as convert


# generate note of given frequency
def generate_note(frequency, display_flag, plot):
    num_samples = 44100
    sample_rate = 44100
    reduction_factor = 0.996
    ring_buffer_length = int(sample_rate/frequency)
    # initialize ring buffer with random numbers between [-0.5, 0.5]
    ring_buffer = deque([random.random() - 0.5 for i in range(ring_buffer_length)])
    
    # plot if flag set
    if display_flag:
        axline, = plot.plot(ring_buffer)
        
    # initialize samples buffer
    samples_buffer = np.array([0]*num_samples, 'float32')
    
    # first element in ring buffer is copied to samples buffer
    # low-pass filter: average is calculated of first two elements in ring buffer
    # attenuation: use reduction value to reduce value in order to simulate loss of energy
    for i in range(num_samples):
        samples_buffer[i] = ring_buffer[0]
        average = reduction_factor*0.5*(ring_buffer[0] + ring_buffer[1])
        ring_buffer.append(average)
        ring_buffer.popleft()
        
        # plot if flag set
        if display_flag:
            if i % 1000 == 0:
                axline.set_ydata(ring_buffer)
                plot.draw()
    print(samples_buffer)
    # convert samples to 16-bit values; then to bytes
    return convert.convert_to_16bit_bytes(samples_buffer)
