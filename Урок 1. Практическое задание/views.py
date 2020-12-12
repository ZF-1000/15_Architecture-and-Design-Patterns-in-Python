from wavy import render


def main_view(request):
    secret = request.get('secret_key', None)
    # Используем шаблонизатор
    # Пробросс данных в контекст шаблона (secret=secret)
    return '200 OK', render('index.html', secret=secret)


def about_view(request):
    # Просто возвращаем текст
    return '200 OK', "About"
