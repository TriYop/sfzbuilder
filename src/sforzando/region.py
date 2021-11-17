
class Region():
    def __init__(self):
        self.params = dict()

    def __repr__(self):
        _content = f"<region>"
        _params = "\n".join([f"{key}={self.params[key]}" for key in self.params])
        return f"\n{_content}\n{_params}\n"

    def set_param(self, param_name, param_value):
        self.params[param_name] = param_value

