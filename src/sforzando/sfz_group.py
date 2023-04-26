from sforzando.sfz_region import SFZRegion


class SFZGroup():
    def __init__(self, lokey=None, hikey=None, keycenter=None, keytrack=None, lovel=None, hivel=None, loop=None, seq_length=None):

        if lokey == hikey and hikey == keycenter:
            self._lokey = None
            self._hikey = None
            self._pitch_keycenter = None
            self._key = lokey
        else:
            self._key = None
            self._lokey = lokey
            self._hikey = hikey
            self._pitch_keycenter = keycenter

        self._pitch_keytrack = keytrack

        self._lovel = lovel
        self._hivel = hivel

        self._seq_length = seq_length

        self._ampeg_release = None
        self._loop_mode = loop
        self._amp_velcurve_127 = None
        self._ampeg_attack = None
        self.regions: [SFZRegion] = []

    def __repr__(self):
        params = {key[1:]: value for key, value in self.__dict__.items() if value is not None and key.startswith('_')}
        _params = " ".join([f"{key}={params[key]}" for key in params])
        _regions = "\n".join([str(region) for region in sorted(self.regions,key=lambda x : f'{x._pitch_keycenter:x}:{x._lovel:x}:{x._sample}' )])
        return f"  <group> {_params}\n{_regions}\n"

    # def set_param(self, param_name, param_value):
    #     self.params[param_name] = param_value

    def add_region(self, region):
        self.regions.append(region)
