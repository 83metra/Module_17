# Не забудьте об импорте одного класса модели в модуль с другим, чтобы таблицы были видны друг другу.
# Для более удобного импорта необходимо дополнить __init__.py в пакете models следующими строками:

from models.user import User
from models.task import Task