def sourcetemplate(url):
    def get_parameters(**kwargs):
        nonlocal url
        if kwargs:
            url = url + '?'
            for key, value in kwargs.items():
                url += f'{key}={value}&'
        return url.strip('&')

    return get_parameters


url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load(name='timur'))
