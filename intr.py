def introspection_info(obj):
    info_dict = {
        "Type": type(obj).__name__,
        "Attributes": [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        "Methods": [method for method in dir(obj) if callable(getattr(obj, method))],
        "Module": obj.__class__.__module__
    }

    return info_dict

number_info = introspection_info(25)
print(number_info)