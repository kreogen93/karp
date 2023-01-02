# Используя миксины из прошлого пункта, напишите класс SecureTextHandler, который будет наследоваться
# от классов ParsesBody, ParsesHeaders и ParsesCookies , иметь метод process() и конструктор, принимающий
# один аргумент и сохраняющий его в нужное поле класса.
# Метод process() должен работать следующим образом:
# Если is_authed() дает False, то возвращать None.
# Иначе получать тело через body() и возвращать его длину.
import json


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


class JsonHandler(ParsesBody, ParsesHeaders):
    def __init__(self, request):
        self.request = request

    def process(self):
        if not self.need_json():
            return None
        try:
            return len(json.loads(self.body()))
        except:  # стоит указать конкретный Exception
            return None


class SecureTextHandler(ParsesBody, ParsesCookies):
    def __init__(self, request):
        self.request = request

    def process(self):
        if not self.is_authed():
            return None
        return len(self.body())

