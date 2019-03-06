#!/usr/bin/env python3

# Java-style, на питоне так делать не надо:
# это можно распилить в обычную функцию и константы


class YandexTranslateApi:
    YANDEX_API_TRANSLATE_URL = '...'
    YANDEX_API_GET_LANGUAGES_URL = '...'

    @staticmethod
    def get_languages():
        return ['ru', 'en']


print(YandexTranslateApi.get_languages())

x = YandexTranslateApi()
print(x.get_languages())
