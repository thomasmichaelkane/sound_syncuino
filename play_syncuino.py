from sound_syncuino.arduino import setup_serial
from sound_syncuino.sound import * 

def run():

    serial_inst = setup_serial()

    serial_inst.open()

    sound_file = get_sound_file()
    sound_duration = get_wav_length(sound_file)

    print("---------------------------")

    while True:
        command = input("Sound control (type 'help' for options) > ")
        
        if command == "help":
            
            print("-- Sound control options --")
            print("Play sound - type '' > (Press enter with no command)")
            print("Exit program - type 'exit'")
            print("See help - type 'help'")
            print("---------------------------")
            
        
        elif command == "exit":
            exit()
            
        elif command == "":
            command = sound_duration + "\n"
            serial_inst.write(command.encode("utf-8"))
            play_sound(sound_file)
        
        else:
            
            print("Error: Unknown command")
            
if __name__ == "__main__":
    run()