from wavy import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/about/': views.about_view,
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
