# HH_click
    3. Автокликер вакансий на HH
    Используемые библиотеки: selenium
1.	Делаем авторизацию на НН.
2.	Нам нужно закрепить вкладку с НН и передать сохраненные параметры браузера в наш код. Для этого используем метод .add_argument() и передаем ему путь до нашей паки User_data( где хранятся настройки браузера).
3.	Далее находим все нужные нам поля используя метод find_element(), и с помощью команды click и send_keys кликаем или передаем нужные нам значения.
4.	Все оборачиваем в цикл for 
5.	Были не большие сложности с поиском некоторых элементов на странице пришлось использовать разные методы поиска (BY.CLASS_NAME, BY.AG_NAME, BY.XPATH, BY.CSS
