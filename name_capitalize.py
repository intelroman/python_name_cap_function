def name_cap(value):
    list = []
    for i in value.split():
        list.append(i.capitalize())
    return (' '.join(list))
