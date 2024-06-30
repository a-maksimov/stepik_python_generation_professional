def custom_isinstance(objects, typeinfo):
    return sum(map(lambda o: isinstance(o, typeinfo), objects))