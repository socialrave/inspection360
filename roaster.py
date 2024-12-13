from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start_keyboard():
    keyboard = [
        [InlineKeyboardButton("Список проектов", callback_data='projects_list')],
        [InlineKeyboardButton("Журнал посещений", callback_data='log_file')],
        [InlineKeyboardButton("Расписание", callback_data='google_sheets')],
        [InlineKeyboardButton("Контакты", callback_data='contacts')]
    ]
    return InlineKeyboardMarkup(keyboard)

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("Список проектов", callback_data='projects_list')],
        [InlineKeyboardButton("Журнал посещений", callback_data='log_file')],
        [InlineKeyboardButton("Расписание", callback_data='google_sheets')],
        [InlineKeyboardButton("Контакты", callback_data='contacts')]
    ]
    return InlineKeyboardMarkup(keyboard)

def back_step():
    keyboard = [
        [InlineKeyboardButton("Главное меню", callback_data='main_menu')] 
    ]
    return InlineKeyboardMarkup(keyboard)

def actual_objects_keyboard():
    keyboard = [
        [InlineKeyboardButton("Симфония", callback_data='symphony')],
        [InlineKeyboardButton("Селигер 4", callback_data='seliger')],
        [InlineKeyboardButton("Сити Бэй 3 очередь", callback_data='city_​​bay3')],
        [InlineKeyboardButton("Сити Бэй 5 очередь", callback_data='city_​​bay5')],
        [InlineKeyboardButton("Преображенская площадь", callback_data='preob_square')],
        [InlineKeyboardButton("Форивер", callback_data='foriver')],
        [InlineKeyboardButton("Раздоры", callback_data='razdory')],
        [InlineKeyboardButton("Сторис", callback_data='stories')],
        [InlineKeyboardButton("ЦОД", callback_data='COD')],
        [InlineKeyboardButton("ТПУ Сити", callback_data='tpu_city')],
        [InlineKeyboardButton("Полковая", callback_data='polkovaya')],
        [InlineKeyboardButton("ТПУ Рязанская", callback_data='tpu_ryazanskaya')],
        [InlineKeyboardButton("Тушино", callback_data='tushino')],
        [InlineKeyboardButton("Мосфильмовская", callback_data='mosfilmovskaya')],
        [InlineKeyboardButton("Шишкин лес", callback_data='shishkin_forest')],
        [InlineKeyboardButton("Верейская", callback_data='vereiskaya')],
        [InlineKeyboardButton("Нагатинская", callback_data='nagatinskaya')],
        [InlineKeyboardButton("Главное меню", callback_data='main_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)

def projects_nextstep_keyboard():
    keyboard = [
        [InlineKeyboardButton("Отметиться", callback_data='check_in')],
        [InlineKeyboardButton("Информация об объекте", callback_data='info_about_project')],
        [InlineKeyboardButton("Уведомление фотомейкеру", callback_data='notification_photomaker')],
        [InlineKeyboardButton("Главное меню", callback_data='main_menu')]
    ]
    return InlineKeyboardMarkup(keyboard)

def photo_allorno_menu():
    keyboard = [
        [InlineKeyboardButton("Да", callback_data='yesyes')],
        [InlineKeyboardButton("Нет", callback_data='ohno')]
    ]
    return InlineKeyboardMarkup(keyboard)