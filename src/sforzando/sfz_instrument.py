from . import SFZGroup, SFZRegion, SFZControl

class SFZInstrument():
    def __init__(self):
        self.params = dict()
        self.params["volume"] = 0
        self.controls:[SFZControl] = []
        self.groups:[SFZGroup] = []
        self.meta = []


    def __repr__(self):
        _metas = "\n".join([f"// {value}" for value in self.meta])
        _params = " ".join([f"{key}={self.params[key]}" for key in self.params])
        _groups = "\n".join([f"{group}" for group in self.groups])
        _controls= "\n".join([f"{control}" for control in self.controls])
        return f"{_metas}\n\n{_controls}\n\n<global> {_params}\n\n{_groups}"

    def set_param(self, param_name, param_value):
        self.params[param_name] = param_value

    def set_meta(self, meta_value):
        self.meta.append( meta_value )

    def add_group(self, group):
        self.groups.append(group)

    def add_control(self, control):
        self.controls.append(control)