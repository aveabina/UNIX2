В рабочую директорию были добавлены файлы форматов .png, .jpeg, .gif, а также index.html и er403.html, er404.html.

settings.py - файл настроек веб-сервера, в котором указаны порты, рабочая директория, максимальный объем запроса в байтах

![pp6 12](https://user-images.githubusercontent.com/91433112/144756898-8fbfa470-c9e5-4efd-8e07-7e506a332c3a.png)


Реализована поддержка постоянного соединения с несколькими запросами:

![pp6 7](https://user-images.githubusercontent.com/91433112/144756911-44271f07-80a0-4a42-83e4-df06cc6284cc.png)

Запрос index.html :

![pp6 1](https://user-images.githubusercontent.com/91433112/144756904-b0e4344d-40c7-4527-9f11-dd3c0f9b9534.png)

ДОП.ЗАДАНИЯ:

При неправильном типе файла происходит переход на файл er403.html с ошибкой:

![pp6 2](https://user-images.githubusercontent.com/91433112/144756905-c3c2e12b-e6d9-4141-8cda-bb6afef6d9b9.png)

При запросе несуществующего файла происходит переход на файл er404.html с ошибкой:

![pp6 6](https://user-images.githubusercontent.com/91433112/144756908-3261c9a3-470b-4ca5-b7d8-0642c487f4f0.png)


Запрос png картинки:

![pp6 3](https://user-images.githubusercontent.com/91433112/144756906-9e0a6ad6-054f-4265-bd82-7f5329556aa9.png)

Запрос jpeg картинки:

![pp6 4](https://user-images.githubusercontent.com/91433112/144756902-981c4736-b1ee-40e3-986b-7228b2354dd5.png)


Запрос gif файла: 

![pp6 5](https://user-images.githubusercontent.com/91433112/144756907-52031805-e3d0-455f-802c-87689e448476.png)

Логи сохраняются в файл logs.txt:

![pp6 11](https://user-images.githubusercontent.com/91433112/144756892-981e592b-4513-44c7-a65a-c9410937f9aa.png)
