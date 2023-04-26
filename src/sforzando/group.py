"""SFZBuilder
---
Sforzando Group
"""
class Group():
    """A SFZ Group entry"""

    def __init__(self):
        """Initialize a Group"""
        self.params = dict()
        self.regions= list()

    def __repr__(self):
        """Represent a Group as String"""
        _content = f"<group>"
        _params = "\n".join([f"{key}={self.params[key]}" for key in self.params])
        _regions = "\n".join([f"{region}" for region in self.regions])
        return f"{_content}\n{_params}\n{_regions}"

    def set_param(self, param_name, param_value):
        """Adds or replaces a parameter for the group.
          :param param_name parameter name
          :param param_value parameter value
        """
        self.params[param_name] = param_value

    def add_region(self, region):
        """Append a region to the group
          :param region the region to be added to group
        """
        self.regions.append( region )
