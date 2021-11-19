"""SFZBuilder
---
Sforzando Control
"""
class Control():
    """Control associated to a sound bank"""

    def __init__(self):
        """Initialize a control"""
        self.params = dict()

    def __repr__(self):
        """Represents a Control as a String"""
        _content = f"<control>"
        _params = "\n".join([f"{key}={self.params[key]}" for key in self.params])
        return f"{_content}\n{_params}"

    def set_param(self, param_name, param_value):
        """Adds or replaces a parameter for the region.
          :param param_name parameter name
          :param param_value parameter value
        """
        self.params[param_name] = param_value
