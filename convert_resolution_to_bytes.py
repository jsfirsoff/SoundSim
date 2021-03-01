# convert sample buffer to new resolution; convert to bytes
# for now fixed to 16-bit

import numpy as np

max_16bit_value = 32767 
conversion_type = 'int16'


def convert_to_16bit_bytes(samples, val=max_16bit_value, conv=conversion_type):
    data = np.array(samples*val, conv)
    return data.tobytes()
