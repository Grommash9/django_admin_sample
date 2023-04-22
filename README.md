Шаблон сайту Django містить важливі змінні в файлах .env. При Debug=False одноразовий код відключений, що полегшує розробку на локальному сервері.
<br><br>
Параметри SESSION_EXPIRE_AT_BROWSER_CLOSE та SESSION_COOKIE_AGE слід використовувати на сайтах з критичною інформацією у панелі адміністратора. Ці параметри автоматично виводять користувача з системи після заданого часу.
<br><br>
Для створення одноразового пароля на продакшені використовується команда:
<br><br>
python manage.py addstatictoken root
<br><br>
Також в налаштуваннях сайту є параметри, які не дозволяють запускати та працювати з ним в режимі HTTP. Шаблон передбачає використання з'єднання HTTPS.
<br><br>
Крім того, реалізовано базову сторінку та до неї підключено стиль для загального розуміння структури проекту.
<br><br>
<br><br>
The Django website template contains important variables in the .env files. When Debug=False, the one-time code is disabled, which makes it easier to develop on the local server.
<br><br>
The SESSION_EXPIRE_AT_BROWSER_CLOSE and SESSION_COOKIE_AGE parameters should be used on sites with critical information in the administrator panel. These parameters automatically log the user out of the system after a set amount of time.
<br><br>
The command used to create a one-time password on production is:
<br><br>
python manage.py addstatictoken root
<br><br>
In addition, the website's settings have parameters that do not allow it to be run or work in HTTP mode. The template expects the use of HTTPS connections.
<br><br>
Furthermore, a basic page has been implemented and a style has been linked to it for a general understanding of the project's structure.
