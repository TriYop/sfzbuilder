from . import Group, Region, Control

class Soundfont():
    def __init__(self):
        self.params = dict()
        self.params["volume"] = 0
        self.controls = list()
        self.groups = list()


    def __str__(self):
        # TODO: render as sfz file content
        global_content = f"<global>"
        _params = "\n".join([f"{key}={self.params[key]}" for key in self.params])
        _groups = "\n".join([f"{group}" for group in self.groups])
        _controls= "\n".join([f"{group}" for group in self.controls])
        return f"{_controls}\n\n{global_content}\n\n{_params}\n\n{_groups}"

    def set_param(self, param_name, param_value):
        self.params[param_name] = param_value

    def add_group(self, group):
        self.groups.append(group)

    def add_control(self, control):
        self.controls.append(control)