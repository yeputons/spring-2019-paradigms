import requests

# Упс, ключ лежит в репозитории и попал на видео.
# Если бы я его не отозвал, то им бы кто угодно мог воспользоваться от моего имени.
r = requests.get('https://search-maps.yandex.ru/v1/?apikey=cb5577ed-9d07-4154-9aad-68659d17d3ad&text=%D0%BC%D1%83%D0%B7%D0%B5%D0%B9&lang=ru_RU')
with open('result.py', 'w', encoding='utf-8') as f:
    f.write(str(r.json()))
