def is_iterable(obj):
    if '__iter__' in dir(obj):
        return True
    return False
