index_tasks = {
    "tasks": [
        {"task": "Задание 1",
         "description": """Создать базу данных для хранения информации о студентах университета.
База данных должна содержать две таблицы: "Студенты" и "Факультеты".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
В таблице "Факультеты" должны быть следующие поля: id и название факультета.
Необходимо создать связь между таблицами "Студенты" и "Факультеты".
Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.""",
         "link": "/all-students/"},
        {"task": "Задание 2",
         "description": """Создать базу данных для хранения информации о книгах в библиотеке.
База данных должна содержать две таблицы: "Книги" и "Авторы".
В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора.
В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
Необходимо создать связь между таблицами "Книги" и "Авторы".
Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов.""",
         "link": "/all-books/"},
        {"task": "Задание 3",
         "description": """Доработаем задача про студентов.
Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
База данных должна содержать две таблицы: "Студенты" и "Оценки".
В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
Необходимо создать связь между таблицами "Студенты" и "Оценки".
Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.""",
         "link": "/new-students/"},
        {"task": "Задание 4",
         "description": """Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
содержать следующие поля:
<ul>
    <li>Имя пользователя (обязательное поле)</li>
    <li>Электронная почта (обязательное поле, с валидацией на корректность ввода email)</li>
    <li>Пароль (обязательное поле, с валидацией на минимальную длину пароля)</li>
    <li>Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)</li>
</ul>
После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite) и выводиться сообщение об успешной регистрации. 
Если какое-то из обязательных полей не заполнено или данные не прошли валидацию, то должно выводиться соответствующее сообщение об ошибке.

Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в базе данных. 
Если такой пользователь уже зарегистрирован, то должно выводиться сообщение об ошибке.
""",
         "link": "/register/"},
        {"task": "Задание 5",
         "description": """Создать форму регистрации для пользователя.
Форма должна содержать поля: имя, электронная почта, пароль (с подтверждением), дата рождения, согласие на обработку персональных данных.
Валидация должна проверять, что все поля заполнены корректно (например, дата рождения должна быть в формате дд.мм.гггг).
При успешной регистрации пользователь должен быть перенаправлен на страницу подтверждения регистрации.""",
         "link": "/flash_task/"},
        {"task": "Задание 6",
         "description": """Дополняем прошлую задачу.
Создайте форму для регистрации пользователей в вашем веб-приложении.
Форма должна содержать следующие поля: имя пользователя, электронная почта, пароль и подтверждение пароля.
Все поля обязательны для заполнения, и электронная почта должна быть валидным адресом.
После отправки формы, выведите успешное сообщение об успешной регистрации.""",
         "link": "/flash_task/"},
        {"task": "Задание 7",
         "description": """Создайте форму регистрации пользователей в приложении Flask. 
Форма должна содержать поля: имя, фамилия, email, пароль и подтверждение пароля. 
При отправке формы данные должны валидироваться на следующие условия:
<ul>
    <li>Все поля обязательны для заполнения.</li>
    <li>Поле email должно быть валидным email адресом.</li>
    <li>Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и одну цифру.</li>
    <li>Поле подтверждения пароля должно совпадать с полем пароля.</li>
    <li>Если данные формы не прошли валидацию, на странице должна быть выведена соответствующая ошибка.</li>
    <li>Если данные формы прошли валидацию, на странице должно быть выведено сообщение об успешной регистрации.</li>
</ul>""",
         "link": "/flash_task/"},
        {"task": "Задание 8",
         "description": """Создать форму для регистрации пользователей на сайте.
Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.""",
         "link": "/flash_task/"},
    ],
}

faculties = ['Frontend', 'Backend']
students = [
    ['Ivan', 'Ivanov', 30, 'M', 101, 1],
    ['Maria', 'Andreeva', 25, 'F', 102, 1],
    ['Maksim', 'Maksimov', 22, 'M', 201, 2],
    ['Evgenii', 'Evgenev', 31, 'M', 203, 2],
    ['Olga', 'Olegovna', 34, 'F', 101, 1],
]

authors = [
    ['Terry', 'Pratchett'],
    ['Stephen', 'King']
]
books = [
    ['The Colour of Magic', 1983, 2, 1],
    ['Guards! Guards!', 1989, 1, 1],
    ['Pet Sematary', 1983, 6, 2],
    ['Hogfather', 1996, 3, 1],
    ['11/22/63', 2011, 5, 2],
]

new_students = [
    ['Ivan', 'Ivanov', 101, 'test@mail.ru'],
    ['Maria', 'Andreeva', 102, 'test1@mail.ru'],
    ['Maksim', 'Maksimov', 201, 'test2@mail.ru'],
    ['Evgenii', 'Evgenev', 203, 'test3@mail.ru'],
    ['Olga', 'Olegovna', 101, 'test4@mail.ru'],
]
scores = [
    [1, 'Python', 4],
    [1, 'Java', 3],
    [2, 'Python', 3],
    [3, 'HTML', 5],
    [1, 'Python', 4],
    [5, 'HTML', 4],
    [5, 'Java', 5],
]