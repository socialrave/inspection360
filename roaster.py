from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start_keyboard():
    keyboard = [
        [InlineKeyboardButton("Список проектов", callback_data='projects_list')],
        [InlineKeyboardButton("Расписание", callback_data='timetable')],
        [InlineKeyboardButton("Контакты", callback_data='contacts')]
    ]
    return InlineKeyboardMarkup(keyboard)

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("Список проектов", callback_data='projects_list')],
        [InlineKeyboardButton("Расписание", callback_data='timetable')],
        [InlineKeyboardButton("Контакты", callback_data='contacts')]
    ]
    return InlineKeyboardMarkup(keyboard)
#сюда надо дописать listobjects_keyboard и вписать все объекты 
def contacts_keyboard():
    keyboard = [
        [InlineKeyboardButton("Главное меню", callback_data='main_menu')] 
    ]
    return InlineKeyboardMarkup(keyboard)