def wav_length(arg):
    
    try:
        
        wav_length = float(arg)
        return wav_length
        
    except TypeError as e:
        
        print(e)

def sample_rate(arg):
    
    try:
        
        sample_rate = int(arg)
        return sample_rate
        
    except TypeError as e:
        
        print(e)

def amplitude(arg):
    
    try:    

        amplitude = float(arg)
        return amplitude

    except TypeError as e:

        print(e)