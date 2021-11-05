import mido
import time

def main():
    port = midi_port()
    save_patch(port)

# Retrieves available midi devices, returns chosen device name
def midi_port():
    try:
        ports = mido.get_input_names()
        for x in ports:
            print(f'{ports.index(x)} {x}')
        select_port = input('Select midi port (#): ')
        return ports[int(select_port)]
    except:
        print('Midi port cannot be found. Please try again.')
        quit()

# Requests a voice bulk dump from the Reface DX, packs received sysex messages
# into a .syx file with user-specified filename
def save_patch(port):
    try:
        inport = mido.open_input(port)
        outport = mido.open_output(port)
        bulk_dump_request = mido.read_syx_file('bulk-dump-request.syx')
        for y in bulk_dump_request:
            outport.send(y)
        time.sleep(1) # time delay to account for speed of incoming messages
        bulk_dump = [z for z in inport.iter_pending()]
        if not bulk_dump:
            print('No data received. Please try again.')
        else:
            patch_name = input('Filename (must end in .syx): ')
            mido.write_syx_file(patch_name, bulk_dump)
    except:
        print('Data was not received in the correct format. Please try again.')
        quit()

if __name__ == '__main__':
    main()
