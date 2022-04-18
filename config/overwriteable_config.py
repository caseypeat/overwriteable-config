import yaml

def is_scientific(x):
    if not isinstance(x, str):
        return False

    xs = x.lower().split('e')
    if len(xs) != 2:
        return False

    a_str, b_str = xs[0].strip('+-'), xs[1].strip('+-')
    if not a_str.isnumeric() or not b_str.isnumeric():
        return False

    return True

def from_dict(dict_obj):
    config_obj = OverwriteableConfig()
    for key in dict_obj.keys():
        if isinstance(dict_obj[key], dict):
            config_obj[key] = from_dict(dict_obj[key])
        else:
            config_obj[key] = dict_obj[key]
    return config_obj

def to_dict(config_obj):
    dict_obj = {}
    for key in config_obj.keys():
        if isinstance(config_obj[key], OverwriteableConfig):
            dict_obj[key] = to_dict(config_obj[key])
        else:
            dict_obj[key] = config_obj[key]
    return dict_obj


class OverwriteableConfig(dict):
    def __init__(self, *args):
        super().__init__()
        """
        Load and merge all mapping objects from left to right.
        Takes YAML filepaths, or dict and OverwriteableConfig objects as arguments
        """
        for arg in args:
            if isinstance(arg, str):
                self.load_yaml(arg)
            elif isinstance(arg, dict) or isinstance(arg, OverwriteableConfig):
                self.merge(arg)
            else:
                raise TypeError('Must be YAML file path, or dictionary object')

    def __getattr__(self, key):
        if key in self.keys():
            # convert scientific notation from string to float
            if is_scientific(self[key]):
                return float(self[key])
            else:
                return self[key]
        else:
            raise KeyError

    def __setattr__(self, key, value):
        self[key] = value

    def merge(self, other):
        """
        Merge with other mapping object, note that "other" object will overwrite "self" when conflicts occur.
        Takes dict or OverwriteableConfig objects as arguments
        """
        if isinstance(other, dict):
            other = from_dict(other)

        for key in other.keys():
            if key in self.keys():
                if isinstance(self[key], OverwriteableConfig) and isinstance(other[key], OverwriteableConfig):
                    self[key].merge(other[key])
                else:
                    self[key] = other[key]
            else:
                self[key] = other[key]

    def as_dict(self):
        return to_dict(self)

    def load_yaml(self, yaml_path):
        """ Load and merge YAML file"""
        with open(yaml_path, 'r') as file:
            config_dict = yaml.safe_load(file)
        self.merge(config_dict)

    def save_yaml(self, yaml_path):
        """ Save YAML file retaining insertion order"""
        with open(yaml_path, 'w') as file:
            yaml.safe_dump(self.as_dict(), file, default_flow_style=False, sort_keys=False)
