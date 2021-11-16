from sforzando import *
import os.path

"""

"""

def scan_dir_for_samples(scan_path:str) -> Soundfont:
    """Generates a sforzando soundfont from a directory"""
    sf = Soundfont()

    ct = Control()
    ct.set_param("default_path", scan_path)
    sf.add_control(ct)

    gp = Group()
    reg = Region()
    reg.set_param("sample", "sample_path.wav")
    reg.set_param("lokey", "60")
    reg.set_param("hikey", "60")
    reg.set_param("pitch_keycenter", "60")
    reg.set_param("lovel", 0)
    reg.set_param("hivel", 127)
    gp.add_region(reg)

    sf.set_param("volume", "0")
    sf.add_group(gp)
    return sf


if __name__ == '__main__':

    scan_path = "chemin_de_recherche"
    sf = scan_dir_for_samples(scan_path)

    #if not os.path.exists(f"{scan_path}.sfz"):
    with open(f"{scan_path}.sfz", "w") as sfz:
        sfz.write(f"{sf}")

    print(sf)

