def get_attributes(instance):
    """
    Get an OrderedDict of attributes (name: value) from a model instance
    :param instance: model instance
    :return: OrderedDict
    """
    try:
        attrs = instance.attrs
    except AttributeError:
        attrs = {}
    try:
        attrs_to_add = instance.get_attributes()
    except AttributeError:
        pass
    else:
        for attribute in attrs_to_add:
            key = attribute.pk
            if key not in attrs:
                attrs[key] = None
    return attrs
