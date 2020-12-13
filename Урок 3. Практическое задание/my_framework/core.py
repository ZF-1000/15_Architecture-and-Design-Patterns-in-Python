class Application:

    def parse_input_data(self, data: str):
        result = {}
        if data:
            # делим параметры через &
            params = data.split('&')
            for item in params:
                # делим ключ и значение через =
                k, v = item.split('=')
                result[k] = v
        return result

    # -> используется для указания типа, который возвращает функция
    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            # декодируем данные
            data_str = data.decode(encoding='utf-8')
            # собираем их в словарь
            result = self.parse_input_data(data_str)
        return result

    def get_wsgi_input_data(self, env) -> bytes:
        # получаем длину тела
        content_length_data = env.get('CONTENT_LENGTH')
        # print(dir(env))
        # приводим к int
        content_length = int(content_length_data) if content_length_data else 0
        # считываем данные если они есть
        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def __init__(self, urlpatterns: dict, front_controllers: list):
        """
        :param urlpatterns: словарь связок url: view
        :param front_controllers: список front controllers
        """
        self.urlpatterns = urlpatterns
        self.front_controllers = front_controllers

    def __call__(self, environ, start_response):
        # environ - словарь с данными запроса от пользователя, в нём мы можем получить все
        # необходимые данные для обработки запроса
        # start_response — функция для отправки кода ответа и заголовков, нужна для передачи заголовков ответа
        # текущий url
        path = environ['PATH_INFO']
        # print(environ)
        # добавление закрывающего слеша
        if not path.endswith('/'):
            path = f'{path}/'

        # Получаем все данные запроса
        method = environ['REQUEST_METHOD']
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)

        query_string = environ['QUERY_STRING']
        request_params = self.parse_input_data(query_string)

        if path in self.urlpatterns:
            # получаем view по url
            view = self.urlpatterns[path]
            request = {}
            # добавляем параметры запросов
            request['method'] = method
            request['data'] = data
            request['request_params'] = request_params
            print(request)      # -> {'method': 'GET', 'data': {}, 'request_params': {}}
            # {'method': 'POST', 'data': {'title': 'qwe', 'text': 'qwe', 'email': 'gb%40local.ru'}, 'request_params': {}}
            # добавляем в запрос данные из front controllers
            for controller in self.front_controllers:
                controller(request)
            # вызываем view, получаем результат
            code, text = view(request)
            # возвращаем заголовки
            start_response(code, [('Content-Type', 'text/html')])
            # возвращаем тело ответа
            return [text.encode('utf-8')]
        else:
            # Если url нет в urlpatterns - то страница не найдена
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b"Not Found"]


# print(environ)
"""
{'wsgi.errors': <gunicorn.http.wsgi.WSGIErrorsWrapper object at 0x7f96f7272160>, 
'wsgi.version': (1, 0), 
'wsgi.multithread': False, 
'wsgi.multiprocess': False, 
'wsgi.run_once': False, 
'wsgi.file_wrapper': <class 'gunicorn.http.wsgi.FileWrapper'>, 
'wsgi.input_terminated': True, 
'SERVER_SOFTWARE': 'gunicorn/20.0.4', 
'wsgi.input': <gunicorn.http.body.Body object at 0x7f96f72727c0>, 
'gunicorn.socket': <socket.socket fd=9, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 54572)>, 
'REQUEST_METHOD': 'GET', 
'QUERY_STRING': '',
'RAW_URI': '/',
'SERVER_PROTOCOL': 'HTTP/1.1', 
'HTTP_HOST': '127.0.0.1:8000', 
'HTTP_CONNECTION': 'keep-alive', 
'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 
'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', 
'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
'HTTP_SEC_FETCH_SITE': 'none', 
'HTTP_SEC_FETCH_MODE': 'navigate', 
'HTTP_SEC_FETCH_USER': '?1', 
'HTTP_SEC_FETCH_DEST': 'document', 
'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 
'HTTP_ACCEPT_LANGUAGE': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 
'wsgi.url_scheme': 'http', 
'REMOTE_ADDR': '127.0.0.1', 
'REMOTE_PORT': '54572', 
'SERVER_NAME': '127.0.0.1', 
'SERVER_PORT': '8000', 
'PATH_INFO': '/', 
'SCRIPT_NAME': ''}
"""

# print(dir(env))
"""
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', 
'__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
'__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 
'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
"""

