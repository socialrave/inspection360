from telegram import Update
from telegram.ext import CallbackContext
from roaster import main_menu_keyboard, start_keyboard, contacts_keyboard
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

async def start(update: Update, context: CallbackContext) -> None:
    reply_markup = start_keyboard()
    await update.message.reply_text("Добрый день!", reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'projects_list': #нажал на кнопочку список проектов
        keyboard = [
            [InlineKeyboardButton("Главное меню", callback_data='main_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard) #создаю новую? клавиатуру с нужными кнопками 
        await query.edit_message_text(text="Вот список проектов: \n1. Проект 1\n2. Проект 2\n3. Проект 3", reply_markup=reply_markup)
        
    elif query.data == 'timetable': #нажал на кнопочку расписание
        keyboard = [
            [InlineKeyboardButton("Главное меню", callback_data='main_menu')] #сразу получил кнопочку главное меню
        ]
        reply_markup = InlineKeyboardMarkup(keyboard) #создаю новую клавиатуру? с нужными кнопками? не понимаю)
        await query.edit_message_text(text="Малеванный - пн, вт, ср \nЛангаев - пн, вт, ср, чт, пт", reply_markup=reply_markup) 
    
    elif query.data == 'contacts': 
        keyboard= [
            [InlineKeyboardButton("Главное меню", callback_data='main_menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Малеванный Владимир, +7 (977) 267-17-38. \nСсылка на телеграмм: @gtoooe\n\nЛангаев Артем, +7 (926) 708-18-27. \nСсылка на телеграмм: @ww5575262337\n\nВинокуров Дмитрий, +7 (968) 470-51-71.\nСсылка на телеграмм: @vindim_a\n\nКрадинов Борис, +7 (926) 187-98-88, \nСсылка на телеграмм: @Boris6", reply_markup=reply_markup)
        
    elif query.data == 'main_menu':  #возвращаюсь в главное меню
        reply_markup = main_menu_keyboard()
        await query.edit_message_text(text="Вы вернулись в главное меню. Нажмите кнопку:", reply_markup=reply_markup)
