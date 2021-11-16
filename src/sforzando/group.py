class Group():
    def __init__(self):
        self.params = dict()
        self.regions= list()

    def __repr__(self):
        _content = f"<group>"
        _params = "\n".join([f"{key}={self.params[key]}" for key in self.params])
        _regions = "\n".join([f"{region}" for region in self.regions])
        return f"{_content}\n{_params}\n{_regions}"

    def set_param(self, param_name, param_value):
        self.params[param_name] = param_value

    def add_region(self, region):
        self.regions.append( region )