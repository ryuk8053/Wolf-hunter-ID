# Wolf STEAM Hunter ID

Этот скрипт на Python позволяет конвертировать ссылки на профили Steam в формат Steam ID `STEAM_X:Y:Z`. Скрипт поддерживает как ссылки с 64-битным Steam ID, так и ссылки с пользовательскими именами. Вы можете конвертировать одну или несколько ссылок на каждую строку за раз. Все конвертируемые ссылки сохраняются в файле `output.txt`. 

## !!! Внимание !!!
Для работы скрипта необходимо наличие API ключа Steam. Без него скрипт не сможет выполнять запросы к API и преобразовывать пользовательские имена в Steam ID. Убедитесь, что вы получили свой API ключ, следуя инструкциям на [странице Steam API](https://steamcommunity.com/dev/apikey). Затем измените в файле скрипта строку `'STEAM_API_KEY'` на `'ВАШ КЛЮЧ'`. Помните, никому не передавайте свой api ключ и переодически меняйте его.


### Установка и использование
1. Убедитесь, что у вас установлен Python 3. Вы можете скачать его с [официального сайта Python](https://www.python.org/downloads/).

2. Установите VSCode [с официального сайта](https://code.visualstudio.com) и запустите его в папке со скриптом.

3. Установите библиотеку `requests`, если она еще не установлена. Откройте терминал и выполните следующую команду:

   ```bash
   pip install requests

4. Поместите ваши ссылки на каждую строку в файл `profiles.txt`. Они должны выглядеть примерно так:

   ```bash
   https://steamcommunity.com/id/пример1
   https://steamcommunity.com/id/пример2
   https://steamcommunity.com/id/пример3

5. Запустите скрипт `wolf_hunter_id.py`