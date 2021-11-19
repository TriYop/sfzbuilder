from . import Group, Region, Control

class Soundfont():
    """A whole soundbank"""

    def __init__(self):
        """Initialize the Soundbank"""
        self.params = dict()
        self.params["volume"] = 0
        self.controls = list()
        self.groups = list()


    def __str__(self):
        """Render SFZ file content"""
        global_content = f"<global>"
        _params = "\n".join([f"{key}={self.params[key]}" for key in self.params])
        _groups = "\n".join([f"{group}" for group in self.groups])
        _controls= "\n".join([f"{group}" for group in self.controls])
        return f"{_controls}\n\n{global_content}\n\n{_params}\n\n{_groups}"

    def set_param(self, param_name, param_value):
        """Adds or replaces a parameter for the soundbank.
          :param param_name parameter name
          :param param_value parameter value
        """
        self.params[param_name] = param_value

    def add_group(self, group:Group):
        """Add a group for the soundbank
          :param group the group object to be added
        """
        self.groups.append(group)

    def add_control(self, control:Control):
        """Add a control for the soundbank.
          :param control the control object to be added
        """
        self.controls.append(control)