import mido
from datetime import datetime

LOGO = """
 &&&&&  &&&&&&   &&&&&&&&&&&   &&&&&&&&&&&&    &&&&&&&&&&&&
 &&&&&  &&&&&&  &&&&&& &&&&&&  &&&&&  &&&&&   &&&&&&
 &&&&&  &&&&&   &&&&&  &&&&&&  &&&&&  &&&&&   &&&&&& ,&&&&&
 &&&&&&&&&      &&&&&  &&&&&&  &&&&&&&&&&     &&&&&& ,&&&&&
 &&&&&  &&&&&   &&&&&  &&&&&&  &&&&&  &&&&&   &&&&&& ,&&&&&
 &&&&&  &&&&&&  &&&&&. &&&&&&  &&&&&  &&&&&&  &&&&&& #&&&&&
 &&&&&  %&&&&&   &&&&&&&&&&&   &&&&&   &&&&&/  &&&&&&&&&&&&
"""

TIMESTAMP = datetime.now().strftime('%Y%m%d-%H%M')
A4_DATA_SIZE = 725

print (LOGO)
print(" --[ KORG A4 MIDI Dump ] --\n")


midi_in_port = mido.open_input('Studio 1810c')
print("[READY] Waiting for MIDI data from A4]")
midi_msg = midi_in_port.receive()
sysex_data = midi_msg.data

if len(sysex_data) == A4_DATA_SIZE:
    print("[SUCCESS] Data Read Successful")

    patch_data = [mido.Message('sysex', data=sysex_data)]
    file_name_text = f"korg-a4-patches-{TIMESTAMP}.txt"
    file_name_raw = f"korg-a4-patches-{TIMESTAMP}.sysex"

    try:
        mido.write_syx_file(file_name_text, patch_data, plaintext=True)
        mido.write_syx_file(file_name_raw, patch_data, plaintext=False)
        print (f"[SUCCESS] Data written to {file_name_text}, {file_name_raw}")
    except:
        print (f"[FAILED] Something went wrong writing files.")

else:
    print(f"[Failed] Wrong MIDI Data size: {len(sysex_data)}")