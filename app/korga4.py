class KorgA4Patch:
    """
        Korg A4 Patch
        Based on Korg A4 Manual, page 23. See 'documents' folder in project.
    """

    # Patch
    name = "Unnamed"

    # Effect Active Status
    comp_active = 0
    dist_active = 0
    eq_active = 0
    delay_active = 0        # aka Pitch / Delay
    chorus_active = 0       # aka Chorus / Flanger
    reverb_active = 0
    extctrl1_active = 0
    extctrl2_active = 0

    comp_sens = 0
    comp_level = 0
    comp_attack = 0
    dist_gain = 0
    dist_level = 0
    dist_mode = 0
    dist_tone = 0
    dist_eqlatch = 0
    eq_bass_gain = 0
    eq_mid_gain = 0
    eq_high_gain = 0
    eq_mid_freq = 0
    eq_high_freq = 0
    eq_trim = 0

    def printout (self):

        print (f"""

Patch Name: {self.name}

    Compressor: {self.comp_active}
    Distortion: {self.dist_active}
    Equaliser: {self.eq_active}
    Delay/Pitch: {self.delay_active}
    Chorus/Flange: {self.chorus_active}
    Reverb: {self.reverb_active}
    ExtCtrl 1: {self.extctrl1_active}
    ExtCtrl 2: {self.extctrl2_active}
""")

logo = """
 &&&&&  &&&&&&   &&&&&&&&&&&   &&&&&&&&&&&&    &&&&&&&&&&&&
 &&&&&  &&&&&&  &&&&&& &&&&&&  &&&&&  &&&&&   &&&&&&
 &&&&&  &&&&&   &&&&&  &&&&&&  &&&&&  &&&&&   &&&&&& ,&&&&&
 &&&&&&&&&      &&&&&  &&&&&&  &&&&&&&&&&     &&&&&& ,&&&&&
 &&&&&  &&&&&   &&&&&  &&&&&&  &&&&&  &&&&&   &&&&&& ,&&&&&
 &&&&&  &&&&&&  &&&&&. &&&&&&  &&&&&  &&&&&&  &&&&&& #&&&&&
 &&&&&  %&&&&&   &&&&&&&&&&&   &&&&&   &&&&&/  &&&&&&&&&&&&
"""

FC_ALLPROGDUMP = "0x50"
FC_PROGDUMP = "0x40"

A4ID = "0x31"

PATCHSIZE = 24

default_patches = [
    {
        'name': 'Thrash Man',
        'bank': 1,
        'pedal': 1
    },
    {
        'name': 'Valve Screamer',
        'bank': 1,
        'pedal': 2
    }
]

