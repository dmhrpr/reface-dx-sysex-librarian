import mido
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def main():
    Tk().withdraw()
    port = midi_port()
    send_patch(port)

# Retrieves available midi devices, returns chosen device name
def midi_port():
    try:
        ports = mido.get_output_names()
        for x in ports:
            print(f'{ports.index(x)} {x}')
        select_port = input('Select midi port (#): ')
        return ports[int(select_port)]
    except:
        print('Midi port cannot be found. Please try again.')
        quit()

# Opens GUI window to choose .syx file, sends file to chosen midi device
def send_patch(port):
    outport = mido.open_output(port)
    y = 0
    while y < 1:
        select_syx_file = askopenfilename()
        try:
            if select_syx_file.split('.')[1] != 'syx':
                print('Please choose a sysex file (.syx)')
            else:
                y = 1
        except:
            quit()
    sysex_messages = mido.read_syx_file(select_syx_file)
    for z in sysex_messages:
        outport.send(z)

if __name__ == '__main__':
    main()
