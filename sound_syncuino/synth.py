from scipy.io import wavfile
from scipy import stats
import numpy as np

def write_noise_wav(length, sample_rate, amplitude):
    
    log = 'Creating {} sec noise wav (sample rate: {}, amplitude: {})'.format(length, sample_rate, amplitude)
    print(log)
    
    length_str = '{:.1f}'.format(length).replace('.', 'p')
    amp_str = '{:.1f}'.format(amplitude).replace('.', 'p')
    file_name = 'wav_files/noise_{}sec_{}_{}.wav'.format(length_str, sample_rate, amp_str)
    noise = stats.truncnorm(-1, 1, scale=min(2**16, 2**amplitude)).rvs(int(round(sample_rate * length)))
    wavfile.write(file_name, sample_rate, noise.astype(np.int16))