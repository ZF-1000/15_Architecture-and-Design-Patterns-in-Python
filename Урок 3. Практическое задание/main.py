from my_framework import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/about/': views.about_view,
    '/contact/': views.contact_view,
    '/create-course/': views.create_course,
    '/create-category/': views.create_category,
    '/category-list/': views.category_list,
    '/course-list/': views.course_list,
}


def secret_controller(request):
    # пример Front Controller
    request['secret_key'] = 'SECRET'


front_controllers = [
    secret_controller
]

application = Application(urlpatterns, front_controllers)

# Запуск:
# gunicorn main:application

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/about/
# http://127.0.0.1:8000/contact/
# http://127.0.0.1:8000/create-course/
# http://127.0.0.1:8000/create-category/
# http://127.0.0.1:8000/category-list/
# http://127.0.0.1:8000/course-list/
