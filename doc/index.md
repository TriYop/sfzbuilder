# SFZBuilder documentation home

---
## Where is the sfz file generated ?

The sfz file is generated in the parent folder of the samples directory. 
It is named after the samples directory with appended `.sfz` suffix

    python3 SFZBuilder.py -i /home/user/samples/PIANO -o /home/user/PIANO.sfz

will scan `PIANO` folder in `/home/user/samples/` and generate 
`/home/user/PIANO.sfz` file

## How to name samples 

In order to be efficiently processed, samples must follow the following naming rule :

    [sample_group_name]_[sample_key]_[sample_velocity].[extension]
    
where 
- `sample_group_name` is in almost free form even if ascii alphanum is strongly encouraged 
- `sample_key` is in the form of Note (A to G with accidental *b* or #) followed by
an octave number from -1 (minus one) to 9 (nine).
-  `extension` is one of wav, aif, flac, mp3, ogg (to match sfz players supported formats)

valid sample names would be:

    piano_C3_ff.wav
    piano_Db3_mf.aif
    piano_D3_pp.mp3
    piano_D#3.ogg

As an enhancement (to be able to import GrandOrgue samplesets https://github.com/GrandOrgue/grandorgue), another common syntax is also allowed:

    [key_number]-[sample_name].[extension]

where 
- `key_number` is the MIDI key number from 0 to 127 and may be formatted on two or three digits.
- `sample_name` follows `sample_group_name` naming convention
-  `extension` is one of wav, aif, flac, mp3, ogg (to match sfz players supported formats)

## Limits and future evolutions

As of now, samples are bound to only a single keyboard note. So if you want to sample less notes to keep your sampleset light, you will still have to manually fix mapping
