import os
import soundfile as sf

from playsound import playsound

def get_sound_file(loc='./sound/'):
    
    sound_folder = os.path.abspath(loc)
    sound_files = os.listdir(sound_folder)
    sound_filename = os.path.join(sound_folder, sound_files[0])
 
    return sound_filename

def play_sound(sound_filename):
    
    try:
        playsound(sound_filename)
    except:
        raise("Playback error")

def get_wav_length(sound_filename):

    f = sf.SoundFile(sound_filename)
    ms = str(int(round(f.frames * 1000 / f.samplerate)))
    new_ms = ms.zfill(5)
    
    return new_ms
    
if __name__ == '__main__':
    
    sound_filename = get_sound_file(loc='../sound/')
    
    get_wav_length(sound_filename)