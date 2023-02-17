class SFZRegion():
    def __init__(self, sample_path: str, lokey=None, hikey=None, keycenter=60, keytrack=1, lovel=None, hivel=None,
                 loop=None):
        self._lokey = lokey
        self._hikey = hikey
        self._pitch_keycenter = keycenter
        self._pitch_keytrack = keytrack

        self._lovel = lovel
        self._hivel = hivel

        self._ampeg_release = None
        self._loop_mode = loop
        self._amp_velcurve_127 = None
        self._ampeg_attack = None
        self._sample = sample_path

    def __repr__(self):
        _content = f"<region>"
        params = {key[1:]: value for key, value in self.__dict__.items() if value is not None}
        _params = " ".join([f"{key}={params[key]}" for key in params])
        return f"    <region> {_params}"

    def set_param(self, param_name, param_value):
        self.params[param_name] = param_value
