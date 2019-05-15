# Обзор
* Дикий запад: много браузеров
  * А в email ещё и почтовые клиенты вроде Outlook (когда-то использовал Word)
* Есть HTML, CSS, JavaScript

# Front-end
## HTML
* Пишем Hello World
* Документ — дерево из элементов
  * https://www.w3schools.com/tags/ref_byfunc.asp
  * Семантические: `<h1>`, `<p>`
  * Стилистические (сейчас плохой тон): `<i>`, `<b>`, `<center>` 
  * Прочее: `<img>`, `<button>`, `<input>`, `<form>`...
* Есть тэги, похож на XML, но не такой строгий, браузер всегда отобразить хоть что-то
  * Поэтому руками разбирать HTML не рекомендуется: лучше Beautiful Soup
    * Сайты бывают динамически: www.meteor.com
  * Браузер внутри себя строит DOM (Document Object Model), открыть консоль разработчика и показать DOM
* Есть таблицы, в 2000 всё версталось таблицами (`<table>`, `<tr>`, `<td>`, `<th>`, `<thread>`, `<tbody>`), так надёжнее и проще
* Комментарии: `<!-- -->`, но обычно всё минифицируется
* Можно использовать без веб-сервера, открывать локально, так можно генерировать отчёты (например, протоколы на всеросе)
* Показать консоль разработчика:
  * Исходный код страницы

## CSS
* Идея: отделить данные от представления. Например, тогда лучше с accessibility.
* Селекторы: по тэгу `p`, по классу `.class`, по идентификатору `#id`, вложенности `.header p`.
* Свойства: `border: 1px solid red;`, `font-size: 200%`, `background-color: red`, `min-width: 100px`.
  * Показать вычисления в инспекторе элементов
* Можно прямо в элементе, но принято делать через `class`
* Block и inline: `<div>`, `<span>`
* Вёрстка: `float`, а вообще сложно.
  * В разных браузерах немного разное поведение, постоянно обновляется
  * CSS is awesome: https://css-tricks.com/css-is-awesome/
  * Недавно появился Flex
* Бывают ещё SASS, LESS: https://sass-lang.com/guide
* Twitter Bootstrap: https://getbootstrap.com/docs/4.3/examples/
  * Показать "исследовать элемент"

## JavaScript
https://www.w3schools.com/js/default.asp

* Единственный язык в браузере
  * Открываем консоль и пишем `alert`, `console.log()`
* Типы данных
  * У всего есть методы (`.toString()`)
  * Числа, строчки, объекты (ключ всегда строчка)
  * Функции: `function xxx() {}` и анонимные функции
  * `[]` и доступ по точке
  * Массивы - просто объекты (но оптимизируются)
  * `null`, `undefined`, разница философская
  * Можно проверить, есть ли свойство у объекта: `hasOwnProperty` (без наследования) и `in` (с наследованием)
  * Можно перечислить свойства: `Object.keys()` (перечисляемые свойства без наследования) и `for (x in obj)` (с наследованием)
    * Цикл по массиву `for (i in arr)` не работает: https://habr.com/ru/post/247857/
* Слабая динамическая типизация
  * Есть `undefined` для неопределённых элементов массива и ещё куча всего
  * Очень слабая: https://www.destroyallsoftware.com/talks/wat
  * `==` и `===` (лучше второе)
* Скрипт выполняется сразу в `<script>`, ещё до подгрузки
  * `alert` в середине
  * `document.write`
  * Поэтому надо либо ставить в конце, либо `defer`, либо `document.addEventListener("DOMContentLoaded", ready);`
  * Можно установить события у кнопок или кого-то ещё (сейчас принято делать в скрипте, а не в HTML)
* Нет потоков, всё в UI thread, блокирует браузер
  * Есть Web Workers
  * `setTimeout()`
* "Исходный код страницы" против "исследовать элемент"
* Модификация страницы:
  * `document.getElementById`
* Много ограничений "к чему можно получить доступ" (например, нельзя прочитать случайный файл с диска)

### Сам язык
* Версии: бывают ECMAScript 6, 8, 2015...
  * Например, в старых версиях был только `var` с hoisting (https://www.w3schools.com/js/js_hoisting.asp), теперь есть `let` и `const`
  * Раньше не было `() => {}` (arrow function)
* `this`
  * Классов исходно нет, есть сахар `new`: https://www.w3schools.com/js/js_object_constructors.asp
  * `this` внутри функции зависит от того, как функцию вызвать, что вызывает проблемы в callback'ах: https://stackoverflow.com/a/20279485/767632
* Прототипное ООП
  * Чтобы не объявлять методы в конструкторе, пишем `Person.prototype.getName = function() {}`: https://www.w3schools.com/js/js_object_prototypes.asp
  * Ещё есть наследование, но мы не будем
  * Но классы появились: https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Classes

### Фреймворвки
* jQuery: https://jquery.com/
  * Есть куча плагинов
* underscore, lodash: https://lodash.com/

# Back-end
## HTTP и формы
* Формы: `action=""`, GET, POST
* Привет из 2000: веб-сервер (Apache, Lighttpd, Nginx) и CGI
  * Можно без библиотеки, можно с библиотекой: https://docs.python.org/3/library/cgi.html
* Стандартный (но немодный) стэк: LAMP (см. gitexercises)
  * В сервер подключается модуль, который трактует `.php`-файлы как скрипты.
  * Но там можно mod_rewrite, см. http://paradigms-spring2019.yeputons.net/
  * Примеры древних фреймворков: WordPress и Drupal
* Утилита ngrok

## Cookies
https://developer.mozilla.org/ru/docs/Web/HTTP/%D0%9A%D1%83%D0%BA%D0%B8

* Просим браузер сохранить данные и каждый раз нам присылать
* Хранить там логин/пароль — плохая идея, лучше "сессию"
  * Срок годности
  * Привязка к IP
* Можно использовать для отслеживания
* Так как на сайте могут быть картинки с других сайтов, то они получают запросы и куки:
  tracking pixel (Google, Facebook, кто угодно)

// TODO

## AJAX
https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data
Same-origin policy и CORS (чтобы нельзя было воспользоваться чужими cookie): https://developer.mozilla.org/ru/docs/Web/HTTP/CORS

## Другое
* Flask
* Django, Ruby on Rails и MVC
* Webhooks
* Longpoll

# Байки
## Accessibility
## Часовые пояса
## Даты
## I18n, l10n
* Минификация, time-to-first-byte
## Отслеживание пользователей
Кэширование HTTP
Минификация
Скорость загрузки страницы (pagespeed)
Скорость отрисовки

# Full stack
## Node.js, Express
## Angular, React, Vua
## Meteor
## TypeScript, CoffeeScript
## Electron

# Безопасность
https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Website_security
https://google-gruyere.appspot.com/
google.com/../../../../passwd

## HTTPS
* Сертификаты
## Аутентификация
## OAuth
Токены рандомны, но не стоит хранить в репозитории
## Уязвимости и атаки
* SQL/HTML инъекции
* XSS
* CSRF
  * Инъекция картинки на страницу
* открытая переадресация
* Утечка информации
  * Через Canvas (уже нельзя)
  * Через определение размеров встроенных элементов с других сайтов
* Хранение паролей в открытом виде, хранение не-bcrypt хэшей
