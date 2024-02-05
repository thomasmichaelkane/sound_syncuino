"""Create noise wav sound files.

This script allows noise wav files to be instantly written with various
parameters. These parameters are currently limited to length, sample 
rate, and amplitude.

Example
-------
Below is an example of a command line use of create_noise.py. There are
three arguments that can be used, one is required (length), the other 
two are optional::

    $ python create_noise.py 1
    $ python create_noise.py 3 44100 11

Attributes
----------
length : float
    Length of the sound in seconds.
    
sample_rate : int
    {optional} Sample rate. Default is 44100.
    
amplitude : float
    {optional} Amplitude of the sound. Default is 11, recommended not
    to deviate from the default signifciantly.

"""

import sys
from sound_syncuino import parse, synth

def run():
    
    WAV_LENGTH, SAMPLE_RATE, AMPLITUDE = parse_args()
    
    synth.write_noise_wav(WAV_LENGTH, SAMPLE_RATE, AMPLITUDE)
    
    
def parse_args():

    if len(sys.argv) == 1:
        
        raise KeyError("No wav length specified")
        
    elif len(sys.argv) == 2:
        
        wav_length = parse.wav_length(sys.argv[1])
        sample_rate = 44100
        amplitude = 11.0
        
    elif len(sys.argv) == 3:
        
        wav_length = parse.wav_length(sys.argv[1])
        sample_rate = parse.sample_rate(sys.argv[2])
        amplitude = 11.0
        
    elif len(sys.argv) == 4:
        
        wav_length = parse.wav_length(sys.argv[1])
        sample_rate = parse.sample_rate(sys.argv[2])
        amplitude = parse.amplitude(sys.argv[3])
        
    else:
        
        raise KeyError("Too many input arguments")
    
    return wav_length, sample_rate, amplitude

if __name__ == "__main__":
    run()