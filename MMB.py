"""
MIT License

Copyright (c) 2024 KeyisB

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
__version__ = '0.0.1.0.4'

import typing as _typing
import types as _types


try:
    from PyQt6.QtWidgets import QWidget
except ImportError:
    pass



class __LocalVault:
    """
    Well-protected local storage for storing data
    """
    def _get_caller_filename(self) -> str:
        ...
    @_typing.overload
    def add(self, key: str, model: tuple): ...
    @_typing.overload
    def add(self, key: str, data: _typing.Any = None, access_level: str = '', allowed_files: _typing.Union[str, _typing.List[str]] = None, denied_files: _typing.Union[str, _typing.List[str]] = None): ... # type: ignore

    def add(self, key: str, data: _typing.Any = None, access_level: str = '', allowed_files: _typing.Union[str, _typing.List[str]] = None, denied_files: _typing.Union[str, _typing.List[str]] = None, model: tuple = None): ... # type: ignore

    @_typing.overload
    def get(self, key: str) -> _typing.Any: ...
    @_typing.overload
    def get(self, model: tuple, default: _typing.Any) -> _typing.Any: ... # type: ignore

    def get(self, key: _typing.Optional[str] = None, model: _typing.Optional[tuple] = None, default: _typing.Optional[_typing.Any] = None) -> _typing.Any: # type: ignore
        ...
    def remove(self, key: str):
        ...
LocalVault = __LocalVault()



class Url:
    def __init__(self, url_str: _typing.Optional[str] = None):
        self.scheme: str
        self.hostname: str
        self.path: str
        self.query: str
        self.fragment: str
        self.params: dict

    def setUrl(self, url_str: str):
        """
        установка URL из строки
        """
        ...
    

    def getUrl(self, parts: _typing.List[_typing.Literal['scheme', 'hostname', 'path', 'params', 'fragment']] = ['scheme', 'hostname', 'path', 'params', 'fragment']) -> str:
        """
        Формирует и возвращает URL на основе указанных частей.

        Этот метод собирает URL из его составных частей, таких как схема, имя хоста, путь,
        параметры и фрагмент. Части, которые должны быть включены в конечный URL, передаются
        в виде списка. Если часть не указана в списке, она будет исключена из конечного результата.

        По умолчанию собираются все части: схема, имя хоста, путь, параметры и фрагмент.

        Пример использования:

            url = my_url.getUrl(parts=['scheme', 'hostname', 'path'])
            # Вернет URL, состоящий только из схемы, имени хоста и пути.

        :param parts List[Literal['scheme', 'hostname', 'path', 'params', 'fragment']]: 
            Список частей URL, которые должны быть включены в конечный результат. 
            Возможные значения:
            - 'scheme': Схема (например, 'https', 'http')
            - 'hostname': Имя хоста (например, 'example.com')
            - 'path': Путь (например, '/some/path')
            - 'params': Параметры запроса (например, '?param1=value1&param2=value2')
            - 'fragment': Фрагмент URL (например, '#section1')
        
        :return str: Полностью сформированный URL, включающий только указанные части.
        """
        ...


class __PyEngine_async:
    """
    Класс PyEngineAsync

    Асинхронный класс, содержащий методы для управления окнами и специфическими для языка Python функциями
    в контексте веб-страницы. Этот класс предназначен для интеграции с браузером и управления
    отображением пользовательского интерфейса в асинхронном контексте.
    """
PyEngine_async = __PyEngine_async()
class __PyEngine:
    """
    Класс PyEngine

    Класс, содержащий методы для управления окнами и специфическими для языка Python функциями
    в контексте веб-страницы. Этот класс предназначен для интеграции с браузером и управления
    отображением пользовательского интерфейса.
    """
    
    def setWidget(self, widget: 'QWidget') -> None: # type: ignore
        """
        Установка виджета страницы в окно браузера.

        Этот метод устанавливает указанный виджет в окно браузера, позволяя отображать
        интерфейс страницы в браузере. Виджет должен быть объектом типа QWidget и будет
        использоваться для представления интерфейса веб-страницы.

        :param widget QWidget: Виджет, представляющий интерфейс страницы.
        """
        ...
    def event(self, name: str):
        """
        Вызывается при событии.

        Usage:
        
            @PyEngine.event('tab-closed')
            def close(code: int) -> None:
                pass
        """
        def wrapper(func): # пример
            return func
        return wrapper
PyEngine = __PyEngine()







class __document_async:
    """
    Класс DocumentAsync

    Асинхронный класс, содержащий методы для управления заголовком и описанием страницы
    в контексте веб-страницы. Этот класс предназначен для интеграции с браузером
    и управления метаданными страницы в асинхронном контексте.
    """

    async def setTitle(self, title: str) -> None:
        """
        Асинхронная установка заголовка страницы.

        Этот метод асинхронно устанавливает указанный заголовок для веб-страницы.

        :param title str: Заголовок страницы.
        """
        ...

    async def setDescription(self, description: str) -> None:
        """
        Асинхронная установка описания страницы.

        Этот метод асинхронно устанавливает указанное описание для веб-страницы, которое
        может быть использовано для отображения в результатах поиска и для других
        мета-целей.

        :param description str: Описание страницы.
        """
        ...
document_async = __document_async()
class __document:
    """
    Класс Document

    Класс, содержащий методы для управления заголовком и описанием страницы
    в контексте веб-страницы. Этот класс предназначен для интеграции с браузером
    и управления метаданными страницы.
    """

    def setTitle(self, title: str) -> None:
        """
        Установка заголовка страницы.

        Этот метод устанавливает указанный заголовок для веб-страницы.

        :param title str: Заголовок страницы.
        """
        ...

    def setDescription(self, description: str) -> None:
        """
        Установка описания страницы.

        Этот метод устанавливает указанное описание для веб-страницы, которое
        может быть использовано для отображения в результатах поиска и для других
        мета-целей.

        :param description str: Описание страницы.
        """
        ...
document = __document()

class __Console:
    """
    Класс Console

    Класс, предоставляющий методы для вывода логов и сообщений в консоль.
    Этот класс предназначен для интеграции с браузером и работы с выводом
    сообщений в консоль, аналогично объекту console в JavaScript.
    """

    def log(self, message: _typing.Any) -> None:
        """
        Выводит информационное сообщение в консоль.

        :param message Any: Сообщение, которое будет выведено в консоль.
        """
        ...

    def warn(self, message: _typing.Any) -> None:
        """
        Выводит предупреждающее сообщение в консоль.

        :param message Any: Сообщение, которое будет выведено в консоль.
        """
        ...

    def error(self, message: _typing.Any) -> None:
        """
        Выводит сообщение об ошибке в консоль.

        :param message Any: Сообщение, которое будет выведено в консоль.
        """
        ...

    def info(self, message: _typing.Any) -> None:
        """
        Выводит информационное сообщение в консоль.

        :param message Any: Сообщение, которое будет выведено в консоль.
        """
        ...
console = __Console()
class __Console_async:
    """
    Класс ConsoleAsync

    Асинхронный класс, предоставляющий методы для вывода логов и сообщений в консоль.
    Этот класс предназначен для интеграции с браузером и работы с выводом
    сообщений в консоль в асинхронном контексте, аналогично объекту console в JavaScript.
    """

    async def log(self, message: _typing.Any) -> None:
        """
        Асинхронно выводит информационное сообщение в консоль.

        :param message Any: Сообщение, которое будет выведено в консоль.
        """
        ...

    async def warn(self, message: _typing.Any) -> None:
        """
        Асинхронно выводит предупреждающее сообщение в консоль.

        :param message Any: Сообщение, которое будет выведено в консоль.
        """
        ...

    async def error(self, message: _typing.Any) -> None:
        """
        Асинхронно выводит сообщение об ошибке в консоль.

        :param message Any: Сообщение, которое будет выведено в консоль.
        """
        ...

    async def info(self, message: _typing.Any) -> None:
        """
        Асинхронно выводит информационное сообщение в консоль.

        :param message Any: Сообщение, которое будет выведено в консоль.
        """
        ...
console_async = __Console_async()

class __window_async:
    """
    Класс WindowAsync

    Асинхронный класс, представляющий собой интерфейс для управления событиями и историей навигации
    в веб-странице. Этот класс предоставляет методы для асинхронной регистрации обработчиков событий,
    управления состоянием истории и имитации навигации назад и вперед в браузере.

    Класс WindowAsync работает аналогично объекту window в JavaScript, обеспечивая
    взаимодействие с ключевыми аспектами работы с окном браузера и историей навигации в асинхронном контексте.
    """
    def __init__(self) -> None:
        self.history = self.__history()
        self.location = self.__location()

    async def addEventListener(self, event: str, handler: _typing.Callable) -> None:
        """
        Асинхронно регистрирует обработчик для указанного события.

        Этот метод добавляет слушателя события для отслеживания определенного события,
        происходящего в окне браузера. Например, вы можете добавить обработчик для
        события "popstate", чтобы реагировать на изменения в истории навигации.

        :param event str: Название события, на которое регистрируется обработчик (например, "popstate").
        :param handler Callable: Функция-обработчик, которая будет вызвана при наступлении события.
        """
        ...

    class __history:
        """
        Вложенный класс HistoryAsync

        Асинхронный класс HistoryAsync предоставляет интерфейс для управления состояниями истории
        навигации в веб-странице. Он позволяет добавлять новые состояния, заменять
        текущие, а также имитировать переходы назад и вперед в истории браузера в асинхронном контексте.
        """

        async def pushState(self, state, title, url: str) -> None:
            """
            Асинхронно добавляет новое состояние в историю и изменяет URL.

            Этот метод позволяет асинхронно добавить новое состояние в стек истории браузера
            без перезагрузки страницы, а также изменить текущий URL. Он часто используется
            в одностраничных приложениях (SPA) для изменения состояния интерфейса
            без полной перезагрузки страницы.

            :param state: Объект состояния, который будет связан с новым элементом истории.
            :param title str: Заголовок страницы для нового состояния (может быть пустым).
            :param url str: Новый URL, который будет отображаться в адресной строке браузера.
            """
            ...

        async def replaceState(self, state, title, url: str) -> None:
            """
            Асинхронно заменяет текущее состояние в истории и изменяет URL.

            Этот метод асинхронно заменяет текущий элемент в истории браузера новым состоянием,
            сохраняя при этом позицию в истории. Это полезно, когда нужно обновить
            состояние или URL без добавления нового элемента в историю.

            :param state: Объект состояния, который заменит текущее состояние в истории.
            :param title str: Новый заголовок страницы для состояния (может быть пустым).
            :param url str: Новый URL, который будет отображаться в адресной строке браузера.
            """
            ...

        async def goBack(self) -> None:
            """
            Асинхронно имитирует нажатие кнопки "Назад" в браузере.

            Этот метод выполняет асинхронный переход на одну страницу назад в истории браузера,
            аналогично нажатию кнопки "Назад" пользователем. Полезно для программной
            навигации в веб-приложениях.
            """
            ...

        async def goForward(self) -> None:
            """
            Асинхронно имитирует нажатие кнопки "Вперед" в браузере.

            Этот метод выполняет асинхронный переход на одну страницу вперед в истории браузера,
            аналогично нажатию кнопки "Вперед" пользователем. Используется для
            программного управления навигацией, когда необходимо восстановить
            следующее состояние после перехода назад.
            """
            ...
    class __location:
        """
        Вложенный класс LocationAsync

        Асинхронный класс LocationAsync предоставляет методы для работы с URL страницы, включая получение текущего
        URL и другие операции, связанные с навигацией, в асинхронном контексте.
        """
window_async = __window_async()
class __window:
    """
    Класс Window

    Класс представляет собой интерфейс для управления событиями и историей навигации
    в веб-странице. Этот класс предоставляет методы для регистрации обработчиков событий,
    управления состоянием истории и имитации навигации назад и вперед в браузере.

    Класс Window работает аналогично объекту window в JavaScript, обеспечивая
    взаимодействие с ключевыми аспектами работы с окном браузера и историей навигации.
    """
    def __init__(self) -> None:
        self.history = self.__history()
        self.location = self.__location()

    def addEventListener(self, event: str, handler: _typing.Callable) -> None:
        """
        Регистрирует обработчик для указанного события.

        Этот метод добавляет слушателя события для отслеживания определенного события,
        происходящего в окне браузера. Например, вы можете добавить обработчик для
        события "popstate", чтобы реагировать на изменения в истории навигации.

        :param event str: Название события, на которое регистрируется обработчик (например, "popstate").
        :param handler Callable: Функция-обработчик, которая будет вызвана при наступлении события.
        """
        ...

    class __history:
        """
        Вложенный класс History

        Класс History предоставляет интерфейс для управления состояниями истории
        навигации в веб-странице. Он позволяет добавлять новые состояния, заменять
        текущие, а также имитировать переходы назад и вперед в истории браузера.
        """

        def pushState(self, state, title, url: str) -> None:
            """
            Добавляет новое состояние в историю и изменяет URL.

            Этот метод позволяет добавить новое состояние в стек истории браузера
            без перезагрузки страницы, а также изменить текущий URL. Он часто используется
            в одностраничных приложениях (SPA) для изменения состояния интерфейса
            без полной перезагрузки страницы.

            :param state: Объект состояния, который будет связан с новым элементом истории.
            :param title str: Заголовок страницы для нового состояния (может быть пустым).
            :param url str: Новый URL, который будет отображаться в адресной строке браузера.
            """
            ...

        def replaceState(self, state, title, url: str) -> None:
            """
            Заменяет текущее состояние в истории и изменяет URL.

            Этот метод заменяет текущий элемент в истории браузера новым состоянием,
            сохраняя при этом позицию в истории. Это полезно, когда нужно обновить
            состояние или URL без добавления нового элемента в историю.

            :param state: Объект состояния, который заменит текущее состояние в истории.
            :param title str: Новый заголовок страницы для состояния (может быть пустым).
            :param url str: Новый URL, который будет отображаться в адресной строке браузера.
            """
            ...

        def goBack(self) -> None:
            """
            Имитирует нажатие кнопки "Назад" в браузере.

            Этот метод выполняет переход на одну страницу назад в истории браузера,
            аналогично нажатию кнопки "Назад" пользователем. Полезно для программной
            навигации в веб-приложениях.
            """
            ...

        def goForward(self) -> None:
            """
            Имитирует нажатие кнопки "Вперед" в браузере.

            Этот метод выполняет переход на одну страницу вперед в истории браузера,
            аналогично нажатию кнопки "Вперед" пользователем. Используется для
            программного управления навигацией, когда необходимо восстановить
            следующее состояние после перехода назад.
            """
            ...
    class __location:
        """
        Вложенный класс Location

        Класс Location предоставляет методы для работы с URL страницы, включая получение текущего
        URL и другие операции, связанные с навигацией.
        """

        def href(self) -> Url:
            """
            Возвращает текущий URL.

            Этот метод возвращает обьект URL, представляющий текущий URL адресной строки.
            Это полезно для получения информации о том, на каком адресе в данный момент
            находится пользователь.

            :return Url: Текущий URL страницы.
            """
            ...
        def currentUrl(self) -> Url:
            """
            Возвращает URL страницы.

            Этот метод возвращает обьект URL, представляющий URL веб-страницы.
            Этот метод отличается от href() в том, он возвращает конкретный начальный url страницы, а не адресную строку.

            :return Url: Текущий URL страницы.
            """
            ...
        def reload(self) -> None:
            ...
window = __window()


class __files:
    """
    Класс Files

    Класс, содержащий методы для загрузки файлов с сайтов, а также для загрузки и управления
    библиотеками с сайтов. Класс предназначен для синхронной загрузки данных с удаленных источников.
    """
    def load(self, url: _typing.Union[Url, str], savePath: str = '/', fileName: _typing.Optional[str] = None, unpack: bool = False, version: str = '0.0.1') -> _typing.Optional[str]:
        """
        Загрузка файла с указанного URL.

        Этот метод загружает файл по указанному URL и возвращает путь к локально сохраненному файлу.

        Usage:

            path = files.load('https://example.com/file.txt')
            path = files.load('https://example.com/file.txt', '/site_name/images')

        :param url str: URL файла, который необходимо загрузить.
        :param savePath str: Необязательный путь для сохранения файла.
                             Если не указан, используется путь из `self.getCurrentFilePath()`.
        :return str: Путь к локально сохраненному файлу, или None, если файл не уладось загрузить.
        """
        ...
    def getCurrentPath(self) -> str:
            """
            Возвращает текущий путь для сохранения файлов.
            :return str: Текущий путь для сохранения файлов.
            """
            ...
files = __files()

class __libs:
        """
        Вложенный класс Libs

        Класс предоставляет методы для загрузки библиотек с сайтов или по имени. Предназначен
        для работы с внешними Python-библиотеками, загружаемыми с удаленных источников.
        """
        def get(self, name: str) -> _typing.Optional[_types.ModuleType]:
            """
            Загрузка библиотеки с указанного URL или по имени.

            Этот метод загружает библиотеку из lib.sourse.gw по имени и возвращает загруженный модуль,
            если он был найден и успешно загружен.

            Usage:

                module = files.libs.load('lib_name')

            :param name str: имя библиотеки для загрузки.
            :return typing.Optional[types.ModuleType]: Загруженная библиотека в виде модуля, или None, если библиотека не найдена.
            """
            ...
libs = __libs()




