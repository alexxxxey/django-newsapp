import importlib

def class_for_name(path):
    module_name, class_name = path.rsplit('.', 1)

    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module(module_name)

    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)

    return c