def is_iterator(obj):
    if '__next__' in dir(obj):
        return True
    return False
