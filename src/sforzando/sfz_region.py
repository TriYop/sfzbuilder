class SFZRegion():
    def __init__(self, sample_path: str, lokey=None, hikey=None, keycenter=-1, keytrack=None, lovel=-1, hivel=None,
                 loop=None, seq_position=None):

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

        self._seq_position = seq_position

        self._ampeg_release = None
        self._loop_mode = loop
        self._amp_velcurve_127 = None
        self._ampeg_attack = None
        self._sample = sample_path.replace('/','\\')
        self._trigger = None

    def __repr__(self):
        _content = f"<region>"
        params = {key[1:]: value for key, value in self.__dict__.items() if value is not None and value != -1}
        _params = " ".join([f"{key}={params[key]}" for key in params])
        return f"    <region> {_params}"

    def set_param(self, param_name, param_value):
        self.params[param_name] = param_value
