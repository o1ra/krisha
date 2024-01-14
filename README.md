## Автоматизация тестирования  веб-сайта объявлений о продаже, покупке, аренде недвижимости в Казахстане [Krisha.kz](https://krisha.kz/)

![main_page.png](resources%2Fimg%2Fmain_page.png)

----

### Инструменты и технологии, используемые в проекте
<p>
<a href="https://www.python.org/"><img src="resources/img/python.png" width="40" height="40"  alt="PYTHON"/></a>
<a href="https://docs.pytest.org/en/"><img src="resources/img/pytest.png" width="40" height="40"  alt="PYTEST"/></a>
<a href="https://www.jetbrains.com/pycharm/"><img src="resources/img/pycharm.png" width="40" height="40"  alt="PYCHARM"/></a>
<a href="https://www.selenium.dev/"><img src="resources/img/selenium.png" width="40" height="40"  alt="SELENIUM"/></a>
<a href="https://github.com/yashaka/selene/"><img src="resources/img/selene.png" width="40" height="40"  alt="SELENE"/></a>
<a href="https://python-poetry.org/"><img src="resources/img/poetry.png" width="40" height="40"  alt="POETRY"/></a>
<a href="https://docs.pydantic.dev/latest/"><img src="resources/img/pydantic.png" width="40" height="40"  alt="PYDANTIC"/></a>
<a href="https://www.jenkins.io/"><img src="resources/img/jenkins.png" width="40" height="40"  alt="JENKINS"/></a>
<a href="https://allurereport.org/"><img src="resources/img/allure_report.png" width="40" height="40"  alt="ALLUREREPORT"/></a>
<a href="https://qameta.io/"><img src="resources/img/allure_testops.png" width="40" height="40"  alt="ALLURETESTOPS"/></a>
<a href="https://aerokube.com/selenoid/"><img src="resources/img/selenoid.png" width="40" height="40"  alt="SELENOID"/></a>
<a href="https://www.atlassian.com/software/jira"><img src="resources/img/jira.png" width="40" height="40"  alt="JIRA"/></a>
</p>

### Особенности проекта

* Оповещения о тестовых прогонах в Telegram
* Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Автоматизация отчетности о тестовых прогонах и тест-кейсах в Jira
* Запуск web/UI автотестов в Selenoid


### Покрываемый функционал
- Выполнение поиска без авторизации по умолчанию
- Выполнение поиска покупки/аренды квартиры
- Главное меню:
  - Открывается страница "Продажа", отображается верный заголовок
  - Открывается страница "Аренда", отображается верный заголовок
  - Открывается страница "Оценка", отображается верный заголовок
  - Открывается страница "Новостройки", отображается верный заголовок, выбран параметр поиска по ЖК в продаже
  - Открывается страница "Новости", отображается верный заголовок
  - Открывается страница "Крыша Гид", отображается верный заголовок

----    

### Запуск тестов
#### По умолчанию производится запуск всех тестов *локально*
Для управления параметрами локального запуска необходимо создать файл .env.local
В проекте есть пример файла `.env.local.example`


### Для локального запуска
1. Склонируйте репозиторий
2. Откройте проект в PyCharm
3. Введите в терминале команду

``` 
python -m venv .venv
source .venv/bin/activate
pip install poetry
pytest --context=local
```
для удаленного запуска тестов через Selenoid необходимо создать файл `.env.test` или `.env.prod` и передать параметр:

```
--context={env_context} 
```
где `{env_context}`  - выбранное окружение, на котором запускаются тесты

В проекте есть примеры файлов `.env.test.example`, `.env.prod.example`



### Для запуска тестов в [Jenkins](https://jenkins.autotests.cloud/job/008-o11ra-diplom/)

1. Открыть проект по [ссылке](https://jenkins.autotests.cloud/job/008-o11ra-diplom/)
2. Нажать `Build with Parameters`
3. Установить параметры или оставить по-умолчнанию 
4. В поле "COMMENT" ввести комментарий
5. Нажать `Build`

![jenkins_build](resources/jenkins_choice_param.png)
6. Дождаться прохождения тестов

![jenkins_build](resources/tests_are_running.png)

#### По итогу будет сформированно 2 отчета : в [Allure Report](https://jenkins.autotests.cloud/job/008-o11ra-diplom/52/allure/) и [Allure TestOps](https://allure.autotests.cloud/project/3915/dashboards)

----

### Allure-отчет

Для перехода к отчету, нужно выбрать соответствующую иконку отчета:

<img alt="This is an image" height="300" src="resources/allure_report.png"/>

#### Пример отчета 

![This is an image](resources/allure_rep.png)

Во вклвдке `Behaviors` есть более подробная информация о этапах прохождения каждого теста, а так же прикрепленные видео, логи, скриншоты, разметка страницы

![This is an image](resources/attachments.png)

----

### Allure TestOps

#### Общий список всех кейсов, имеющихся в системе
![This is an image](resources/test_cases.png)

#### Пример dashboard с общими результатами тестирования
![This is an image](resources/dashboard.png)

----
### Интеграция с Jira

[//]: # (<img alt="This is an image" height="300" src="resources/jira.png"/>)

![This is an image](resources/jira.png)

----
### Оповещение о результатах прохождения тестов в Telegram

<img alt="This is an image" height="300" src="resources/telegram_tests.png"/>

----
### Пример видео прохождения автотеста
Тест-кейс "Регистрация без ввода пароля"

![Регистрация без ввода пароля](resources/test_rent.gif)