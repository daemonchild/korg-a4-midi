import mido
from datetime import datetime
import sys

#file_name = sys.argv[1]
file_name = "korg-a4-patches-20200506-1550.sysex"

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
print(" --[ KORG A4 MIDI Dump Decoder ] --\n")

if file_name:

    try:
        sysex_data = mido.read_syx_file(file_name)
        print (f"[SUCCESS] Data read OK")

        # To Do:
        # - Decode the data:
        # - Looks to be patches starting at hex group 8, 24 groups long

    except:
        print (f"[FAILED] Something went wrong reading {file_name}.")
else:
    print (f"[FAILED] Please provide a filename to decode.")