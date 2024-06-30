from datetime import date

d = {
    'ru': '%d.%m.%Y',
    'us': '%m-%d-%Y',
    'ca': '%Y-%m-%d',
    'br': '%d/%m/%Y',
    'fr': '%d.%m.%Y',
    'pt': '%d-%m-%Y'
}


def date_formatter(country_code):
    def format_date(date):
        return date.strftime(format=d[country_code])

    return format_date


date_ru = date_formatter('us')
today = date(2025, 1, 5)
print(date_ru(today))
