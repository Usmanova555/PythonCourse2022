""" Файлы __init__.py необходимы, чтобы Python рассматривал каталоги как содержащие пакеты

Это делается для того, чтобы предотвратить каталоги с общим именем, например string, от непреднамеренного скрытия 
допустимых модулей, которые происходят позже (глубже) на пути поиска модуля. В простейшем случае __init__.py может 
быть просто пустым файлом, но он также может выполнять код инициализации для пакета или устанавливать переменную 
__all__ """