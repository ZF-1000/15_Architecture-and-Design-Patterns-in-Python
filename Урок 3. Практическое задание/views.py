from my_framework import render


def main_view(request):
    secret = request.get('secret_key', None)
    # Используем шаблонизатор
    # Пробросс данных в контекст шаблона (secret=secret)
    return '200 OK', render('index.html', secret=secret)


def about_view(request):
    # Просто возвращаем текст
    return '200 OK', "About"


def contact_view(request):
    # Проверка метода запроса
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        print(f'Нам пришло сообщение от {email} с темой {title} и текстом {text}')
        return '200 OK', render('contact.html')
    else:
        return '200 OK', render('contact.html')


def create_course(request):
    secret = request.get('secret_key', None)
    return '200 OK', render('create_course.html', secret=secret)


def create_category(request):
    secret = request.get('secret_key', None)
    return '200 OK', render('create_category.html', secret=secret)


def category_list(request):
    secret = request.get('secret_key', None)
    return '200 OK', render('category_list.html', secret=secret)

def course_list(request):
    secret = request.get('secret_key', None)
    return '200 OK', render('course_list.html', secret=secret)