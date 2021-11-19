"""SFZBuilder
---
Sforzando region
"""
class Region():
    def __init__(self):
        """Create a new region with its own parameters"""
        self.params = dict()

    def __repr__(self):
        """Render a region representation"""
        _content = f"<region>"
        _params = "\n".join([f"{key}={self.params[key]}" for key in self.params])
        return f"\n{_content}\n{_params}\n"

    def set_param(self, param_name, param_value):
        """Adds or replaces a parameter for the region.
          :param param_name parameter name
          :param param_value parameter value
        """
        self.params[param_name] = param_value

