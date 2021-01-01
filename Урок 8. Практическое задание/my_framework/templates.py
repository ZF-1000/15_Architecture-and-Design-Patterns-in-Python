"""
Для передачи данных на страницу используется шаблонизатор.
Один из популярных шаблонизаторов — Jinja2
"""
from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment
# import os


def render(template_name, folder='templates', **kwargs):
    """
    :param template_name: имя шаблона
    :param folder: папка в которой ищем шаблон
    :param kwargs: параметры для передачи в шаблон
    :return:
    """
    # Совместили путь каталога и файла вместе, для получения рабочего пути
    # file_path = os.path.join(folder, template_name)
    # Открываем шаблон по имени
    # with open(file_path, encoding='utf-8') as f:
        # Читаем
        # template = Template(f.read())
    # рендерим шаблон с параметрами
    # return template.render(**kwargs)

    env = Environment()
    # print(env)      # -> <jinja2.environment.Environment object at 0x7ff09a1eff70>
    # print(dir(env))
    # указываем папку для поиска шаблонов
    env.loader = FileSystemLoader(folder)
    # находим шаблон в окружении
    template = env.get_template(template_name)
    return template.render(**kwargs)

# print(dir(env))
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
 '_compile', '_generate', '_load_template', '_parse', '_tokenize', 'add_extension', 'auto_reload', 'autoescape',
 'block_end_string', 'block_start_string', 'bytecode_cache', 'cache', 'call_filter', 'call_test',
 'code_generator_class', 'comment_end_string', 'comment_start_string', 'compile', 'compile_expression',
 'compile_templates', 'context_class', 'enable_async', 'exception_formatter', 'exception_handler', 'extend',
 'extensions', 'filters', 'finalize', 'from_string', 'get_or_select_template',
 'get_template',
 'getattr', 'getitem', 'globals', 'handle_exception', 'is_async', 'iter_extensions', 'join_path',
 'keep_trailing_newline',
 'lex', 'lexer', 'line_comment_prefix', 'line_statement_prefix', 'linked_to', 'list_templates',
 'loader',
 'lstrip_blocks', 'make_globals', 'newline_sequence', 'optimized', 'overlay', 'overlayed', 'parse', 'policies',
 'preprocess', 'sandboxed', 'select_template', 'shared', 'template_class', 'tests', 'trim_blocks', 'undefined',
 'variable_end_string', 'variable_start_string']
"""