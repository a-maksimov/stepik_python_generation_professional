def get_genre(string):
    string_list = string.split(',')
    genres_order = ['Animation', 'Documentary', 'Musical', 'Comedy', 'Horror', 'Action', 'Adventure',
                    'Thriller', 'Crime', 'Drama']
    if len(string_list) == 1:
        if string_list[0] in genres_order:
            return string_list[0]
        else:
            return 'Other'
    for genre in genres_order:
        if genre in string_list:
            return genre
    return 'Other'


print(get_genre('Animation'))
