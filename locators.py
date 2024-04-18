class BurgersLocators:

    #Главная страница:
    LK_BUTTON = ".//p[text()='Личный Кабинет']"  # кнопка Личный кабинет
    ENTER_BUTTON = ".//button[text()='Войти в аккаунт']"  # кнопка Войти в аккаунт
    ORDER_BUTTON = ".//button[text()='Оформить заказ']"  # кнопка Оформить заказ

    #Форма регистрации

    REGISTRATION_NAME = ".//label[text()='Имя']/parent::div/input"  # поле Имя в форме регистрации
    REGISTRATION_EMAIL = ".//label[text()='Email']/parent::div/input"  # поле Email в форме регистрации
    REGISTRATION_PASSWORD = ".//input[@name='Пароль']"  # поле Пароль в форме регистрации
    REGISTRATION_BUTTON = ".//button[text()='Зарегистрироваться']"  # кнопка Зарегистрироваться в форме регистрации

    LINK_ENTER = ".//a[text()='Войти']"  # ссылка Войти в форме регистрации

    #Форма авторизации:
    LOGIN_TITLE = ".//h2[text()='Вход']"  # заголовок Вход формы авторизации
    LOGIN_EMAIL = ".//input[@name='name']"  # поле Email в форме авторизации
    LOGIN_PASSWORD = ".//input[@name='Пароль']"  # поле Пароль в форме авторизации
    LOGIN_BUTTON = ".//Button[text()='Войти']"  # кнопка Войти в форме авторизации

    LINK_REGISTRATION = ".//a[text()='Зарегистрироваться']"  # ссылка Зарегистрироваться
    LINK_RECOVERY = ".//a[text()='Восстановить пароль']"  # ссылка Восстановить пароль

    PASSWORD_ERROR = ".//p[text()='Некорректный пароль']"  # Ошибка Некорректный пароль в форме авторизации


    #Форма восстановления пароля
    ENTER_LINK = ".//a[text()='Войти']"  # ссылка Войти в форме восстановления пароля
    PROFILE_NAME = "//h1[@class='profile__title']"

    #Личный кабинет
    LK_NAME = ".//input[@name='Name']"  # поле Имя в Личном кабинете
    SAVE_BUTTON = ".//button[text()='Сохранить']"  # кнопка Сохранить в личном кабинете
    CONSTRUCT_BUTTON = ".//p[text()='Конструктор']" # кнопка Конструктор в личном кабинете
    LOGO = ".//header//div/a"  # Логотип Stellar Burgers
    LOGOUT_BUTTON = ".//button[text()='Выход']"  # кнопка Выход в личном кабинете

    #Конструктор
    ROLLS = ".//span[text()='Булки']"  # заголовок раздела Булки
    SAUCES = ".//span[text()='Соусы']"  # заголовок раздела Соусы
    FILLINGS = ".//span[text()='Начинки']"  # заголовок раздела Начинки
    ROLLS_SECTION = ".//span[text()='Булки']/parent::div"  # раздел Булки
    SAUSES_SECTION = ".//span[text()='Соусы']/parent::div"  # раздел Соусы
    FILLINGS_SECTION = ".//span[text()='Начинки']/parent::div"  # раздел Начинки
