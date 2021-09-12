# API_polling_system
Polling system by DRF

## URIs:

Доступные всем:

- /api-auth/login/ - browsable authorization
- /active-pollings/ - список всех активных опросов

Доступные только администратору:

- /pollings/ - полный список опросов
- /polling/<int:pk>/ - детали опроса
- /questions/ - список вопросов
- /question/<int:pk>/ - детали вопроса
- /choices/ - список вариантов ответов
- /choice/<int:pk>/ - детали варианта ответа

## Архитектура БД

Главная таблца опрос (polling) может включать в себя вопросы (question). Вопросы (question) могут включать в себя варианты ответов (choice).

Таблица опрос (polling) состоит из таких полей как:
- id(int, pk);
- name(char);
- start_date(datetime, editable=False);
- finish_date(datetime);
- description(char).

Таблица вопросы (question) состоит из:
- id(int, pk);
- question(char);
- question_type(char);
- polling(many to one).

Таблица варианты (choices) состоит из:
- id(int, pk);
- choice_text(char);
- question(many to one).

P.S.

Не понял как сделать авторизацию без регистрации. Поэтому, нет таких URI как: прохождение опроса и показ пройдённых опросов.


