"""
Для передачи данных на страницу используется шаблонизатор.
Один из популярных шаблонизаторов — Jinja2
"""
from jinja2 import Template
import os


def render(template_name, folder='templates', **kwargs):
    """
    :param template_name: имя шаблона
    :param folder: папка в которой ищем шаблон
    :param kwargs: параметры для передачи в шаблон
    :return:
    """
    # Совместили путь каталога и файла вместе, для получения рабочего пути
    file_path = os.path.join(folder, template_name)
    # Открываем шаблон по имени
    with open(file_path, encoding='utf-8') as f:
        # Читаем
        template = Template(f.read())
    # рендерим шаблон с параметрами
    return template.render(**kwargs)
