# Разным классам в приложении потребуется разная функциональность: кому-то потребуется проверять,
# есть ли в headers ключ "Accept", кому-то потребуется читать body, а кому-то понадобится проверять пустоту cookies.
# Будут и классы, которым потребуется несколько возможностей сразу.
# Напишите классы ParsesCookies, ParsesBody, ParsesHeaders по условиям:
# Класс ParsesCookies имеет метод cookies(), возвращающий все по ключу cookies из словаря self.request.
# Класс ParsesCookies имеет метод is_authed(), который будет проверять, что в словаре cookies будет ключ
# auth_key (ни в коем случае не используйте такую авторизацию в реальных проектах).
# Класс ParsesBody имеет метод body(), возвращающий текст по ключу body в self.request.
# Класс ParsesHeaders имеет метод headers(), возвращающий все по ключу headers из словаря self.request.
# Класс ParsesHeaders имеет метод need_json(), который возвращает True, если в headers по ключу
# "content-type" лежит значение "application/json", иначе False.


class ParsesCookies:
    def cookies(self):
        # вытаскивает куки из запроса
        return self.request['cookies']

    def is_authed(self):
        # проверяет наличие ключа 'auth-key' в cookies
        # обратите внимание, как вместо дублирования кода self.request['cookies']
        # мы переиспользуем функцию
        return 'auth_key' in self.cookies()


class ParsesBody:
    def body(self):
        # аналогично cookies()
        return self.request['body']


class ParsesHeaders:
    def headers(self):
        # аналогично cookies()
        return self.request['headers']

    def need_json(self):
        # проверяем, лежит ли в headers по ключу 'content-type' интересующее значение
        return self.headers().get('content-type') == 'application/json'