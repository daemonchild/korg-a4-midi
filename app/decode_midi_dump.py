import mido
from datetime import datetime
import korga4
import sys

#file_name = sys.argv[1]
file_name = "korg-a4-patches-20200506-1550.sysex"

def ByteToBin (data_byte):

    return (bin(data_byte)[2:].zfill(8))



def Sysex2Patch (patch_name, data):

    if len(data) == 24:

        effects_active_byte = ByteToBin(data[0])
        byte1 = ByteToBin(data[1])
        byte2 = ByteToBin(data[2])
        byte3 = ByteToBin(data[3])
        byte4 = ByteToBin(data[4])
        byte5 = ByteToBin(data[5])
        byte6 = ByteToBin(data[6])
        byte7 = ByteToBin(data[7])
        byte8 = ByteToBin(data[8])
        byte9 = ByteToBin(data[9])
        byte10 = ByteToBin(data[10])
        byte11 = ByteToBin(data[11])
        byte12 = ByteToBin(data[12])
        byte13 = ByteToBin(data[13])
        byte14 = ByteToBin(data[14])
        byte15 = ByteToBin(data[15])
        byte16 = ByteToBin(data[16])
        byte17 = ByteToBin(data[17])
        byte18 = ByteToBin(data[18])
        byte19 = ByteToBin(data[19])


        # Effects: Active or Not

        patch = korga4.KorgA4Patch()

        patch.name = patch_name

        patch.comp_active = effects_active_byte[0]
        patch.dist_active = effects_active_byte[1]
        patch.eq_active = effects_active_byte[2]
        patch.delay_active = effects_active_byte[3]
        patch.chorus_active = effects_active_byte[4]
        patch.reverb_active = effects_active_byte[5]
        patch.extctrl1_active = effects_active_byte[6]
        patch.extctrl2_active = effects_active_byte[7]

        # Effects: Compressor (3 settings)

        print (f"patch.comp_sens = {int(byte1[0:3])}")
        print (f"patch.comp_level = {int(byte1[4:7])}")
        print (f"patch.comp_attack = {int(byte10[5:7])}")

        # Effects: Distortion (5 settings)

        print (f"patch.dist_gain = {int(byte2[0:3])}")
        print (f"patch.dist_level = {int(byte2[4:7])%15}")
        print (f"patch.dist_mode = {int(byte11[5:7])}")
        print (f"patch.dist_tone = {int(byte12[5:7])}")
        print (f"patch.dist_eqlatch = {int(byte14[5])}")

        # Effects: Equaliser (6 settings)

        print (f"patch.eq_bass_gain = {int(byte3[0:3])}")
        print (f"patch.eq_mid_gain = {int(byte4[0:3])}")
        print (f"patch.eq_high_gain = {int(byte5[0:3])}")
        print (f"patch.eq_mid_freq = {int(byte3[4:7])}")
        print (f"patch.eq_high_freq = {int(byte4[4:7])}")
        print (f"patch.eq_trim = {int(byte5[4:7])%15}")

        # Effects: Delay / Pitch (11 settings)

        print (f"patch.delay_mode = {}")
        # Delay
        print (f"patch.delay_delay_time_100ms = {int(byte6[0:3])}")
        print (f"patch.delay_delay_time_10ms = {int(byte6[4:7])}")
        print (f"patch.delay_delay_time_1ms = {int(byte7[0:3])}")
        print (f"patch.delay_delay_feedback = {}")
        print (f"patch.delay_delay_hi_damp = {}")
        print (f"patch.delay_delay_mix = {}")
        # Pitch
        print (f"patch.delay_pitch_pitch = {}")
        print (f"patch.delay_pitch_fine = {}")
        print (f"patch.delay_pitch_hicut = {}")
        print (f"patch.delay_pitch_mix = {}")


        return (patch)
    else:
        print ("[FAILED] Data Broken")


TIMESTAMP = datetime.now().strftime('%Y%m%d-%H%M')
A4_DATA_SIZE = 725

print (korga4.logo)
print(" --[ KORG A4 MIDI Dump Decoder ] --\n")

if file_name:

    try:
        sysex_data = mido.read_syx_file(file_name)
        print (sysex_data)
        data = sysex_data[0].data
        print (f"[SUCCESS] Data read OK")

        # To Do:§
        # - Decode the data:
        # - Looks to be patches starting at hex group 8, 24 groups long

    except:
        print (f"[FAILED] Something went wrong reading {file_name}.")

    # Sysex header bytes 0-6

    header_id = hex(data[0])
    header_format_id = hex(data[1])
    header_a4id = hex(data[2])
    header_function_code = hex(data[3])

    print (f"{header_id}, {header_format_id}, {header_a4id}, {header_function_code}")

    if header_a4id != korga4.A4ID:

        print(f"[FAILED] This does not look like Korg A4 Data. :(")
        exit (1)

    if header_function_code == korga4.FC_ALLPROGDUMP:

        print(f"[FOUND] Received 'All Program Dump'")

        patches = data[6:]
        patch_size = korga4.PATCHSIZE

        patch_count = 0
        for p in range (0,int(len(patches)/patch_size)):

            block = []
            offset = patch_count * patch_size
            block.append(patches[offset:offset+patch_size])

            patch_name = f"User Patch {patch_count + 11}"

            patch = korga4.KorgA4Patch()
            patch = Sysex2Patch (patch_name, block[0])

            patch_count += 1

            patch.printout()




else:
    print (f"[FAILED] Please provide a filename to decode.")
    exit(1)