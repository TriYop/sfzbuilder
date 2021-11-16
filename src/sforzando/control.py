
class Control():
    def __init__(self):
        self.params = dict()

    def __repr__(self):
        _content = f"<control>"
        _params = "\n".join([f"{key}={self.params[key]}" for key in self.params])
        return f"{_content}\n{_params}"

    def set_param(self, param_name, param_value):
        self.params[param_name] = param_value