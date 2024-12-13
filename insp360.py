from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext, MessageHandler, filters, ConversationHandler, ContextTypes
from roaster import main_menu_keyboard, start_keyboard, actual_objects_keyboard, projects_nextstep_keyboard, back_step, photo_allorno_menu
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import json, os
import logging

JSON_FILE = 'visit_log.json'
AWAITING_NOTE = 1
INPUT_DATA, PHOTO_CHECK = range(2)
CREDENTIALS_FILE = "grand-mile_googlesheets.json" 
CREDENTIALS_FILE2 = "grand-mile-googledrive.json" 
SPREADSHEET_ID = "19UPUb5_UXcTG7eai6WkgtpKnog" 


async def start(update: Update, context: CallbackContext) -> None:
    reply_markup = start_keyboard()
    await update.message.reply_text("Добрый день!", reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    callback_data = query.data
    
    object_name = None 
    for row in actual_objects_keyboard().inline_keyboard:
        for button in row:
            if button.callback_data == callback_data:
                object_name = button.text
                
    context.user_data['selected_object'] = object_name or "Неизвестный объект"
    
    await query.answer()

    if query.data == 'projects_list': #кнопочка список проектов
        reply_markup = actual_objects_keyboard()
        await query.edit_message_text(text="Актуальный список проектов:", reply_markup=reply_markup)
    
    elif query.data == 'symphony':  
        reply_markup = projects_nextstep_keyboard()
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
     
    elif query.data == 'paveletckaya':  
        reply_markup = projects_nextstep_keyboard()
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
        
    elif query.data == 'seliger':  
        reply_markup = projects_nextstep_keyboard()
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
        
    elif query.data == 'city_​​bay3':  
        reply_markup = projects_nextstep_keyboard()
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
        
    elif query.data == 'city_​​bay5':  
        reply_markup = projects_nextstep_keyboard() 
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
    
    elif query.data == 'preob_square':  
        reply_markup = projects_nextstep_keyboard() 
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
    
    elif query.data == 'foriver':  
        reply_markup = projects_nextstep_keyboard() 
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
    
    elif query.data == 'razdory':  
        reply_markup = projects_nextstep_keyboard() 
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
        
    elif query.data == 'stories':  
        reply_markup = projects_nextstep_keyboard() 
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
        
    elif query.data == 'COD':  
        reply_markup = projects_nextstep_keyboard() 
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
    
    elif query.data == 'tpu_city':  
        reply_markup = projects_nextstep_keyboard() 
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
    
    elif query.data == 'polkovaya':  
        reply_markup = projects_nextstep_keyboard() 
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
    
    elif query.data == 'tpu_ryazanskaya':  
        reply_markup = projects_nextstep_keyboard() 
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
    
    elif query.data == 'tushino':  
        reply_markup = projects_nextstep_keyboard() 
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
    
    elif query.data == 'mosfilmovskaya':  
        reply_markup = projects_nextstep_keyboard() 
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
    
    elif query.data == 'shishkin_forest':   
        reply_markup = projects_nextstep_keyboard() 
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
    
    elif query.data == 'vereiskaya':   
        reply_markup = projects_nextstep_keyboard() 
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)
    
    elif query.data == 'nagatinskaya':   
        reply_markup = projects_nextstep_keyboard() 
        await query.edit_message_text(text="старт\уведомление\инфо", reply_markup=reply_markup)  
    
    elif query.data == 'contacts': 
        reply_markup = back_step()
        await query.edit_message_text(text="О_О", reply_markup=reply_markup)

    elif query.data == 'main_menu': 
        reply_markup = main_menu_keyboard()
        await query.edit_message_text(text="Вы вернулись в главное меню. Нажмите кнопку:", reply_markup=reply_markup)
    
    elif query.data == 'log_file':
        await send_log_file(update, context)    
        
    elif query.data == 'ohno':
        await query.edit_message_text(text="Опишите, что не выполнено?")
        context.user_data["awaiting_input"] = True
        return "INPUT_DATA2"

    elif query.data == 'notification_photomaker': 
        await query.edit_message_text("Пожалуйста, введите ваше замечание:") 
        return "AWAITING_NOTE"
    
    elif query.data == 'google_sheets':
        await send_google_sheets_data(query, context)    
        
async def check_in(update: Update, context: CallbackContext) -> int: 
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text="Введите информацию в формате: \nФамилия Имя, дата, время, объект")
    return INPUT_DATA

async def handle_input(update: Update, context: CallbackContext) -> int:
    user_dict = update.message.text.strip()
    context.user_data.pop("user_dict", None)
    context.user_data["user_dict"] = user_dict
    reply_markup = photo_allorno_menu()
    await update.message.reply_text("Фото выполнены на всех точках?", reply_markup=reply_markup)
    return PHOTO_CHECK

async def handle_no_input(update: Update, context: CallbackContext) -> int:
    reason = update.message.text.strip()
    user_dict = context.user_data.get("user_dict", "Неизвестные данные")
    full_data = f"{user_dict}, Причина: {reason}"
    await save_check_in(full_data, update.effective_user.username)
    reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton("Главное меню", callback_data="main_menu")]
            ])
    await update.message.reply_text("Данные с причиной успешно записаны.", reply_markup=reply_markup)
            
    return ConversationHandler.END
    
async def photo_check(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    await query.answer()

    if query.data == "yesyes":
        user_dict = context.user_data.get("user_dict")
        if user_dict:
            await save_check_in(user_dict, update.effective_user.username)
            reply_markup = InlineKeyboardMarkup([
                [InlineKeyboardButton("Главное меню", callback_data="main_menu")]
            ])
            await query.edit_message_text("Данные успешно сохранены.", reply_markup=reply_markup)
            return ConversationHandler.END
        else:
            await query.edit_message_text("Ошибка, данные отсутствуют. Попробуйте заново.")
            return INPUT_DATA

    elif query.data == "ohno":
        await query.edit_message_text("Опишите, что не выполнено?")
        context.user_data["awaiting_input"] = True
        return "INPUT_DATA2"

async def save_check_in(user_dict: str, username: str) -> None:
    visit_log = load_visit_log()
    full_entry = f"{user_dict} @{username}"
    visit_log.append(full_entry)
    save_visit_log(full_entry)

def load_visit_log():
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_visit_log(entry: str):
    with open(JSON_FILE, 'a', encoding='utf-8') as file:
        file.write(f"{entry}\n")

async def send_log_file(update: Update, context: CallbackContext) -> None:
    file_path = JSON_FILE
    if os.path.exists(file_path):
        await update.callback_query.answer()
        await update.callback_query.message.reply_document(
            document=open(file_path, 'rb'),
            filename="журнал посещений"
        )
    else:
        await update.callback_query.answer()
        await update.callback_query.message.reply_text("Файл журнала отсутствует.")

def read_google_sheets():
    try:
        credentials = Credentials.from_service_account_file(CREDENTIALS_FILE)
        service = build("sheets", "v4", credentials=credentials)

        RANGES = ["График 2024!K2:N2", "График 2024!K3:N3", "График 2024!K4:N100", "График 2024!C4:C100", "График 2024!A3:A100"]
        sheet = service.spreadsheets()

        #Запрос данных из всех диапазонов
        result = sheet.values().batchGet(spreadsheetId=SPREADSHEET_ID, ranges=RANGES).execute()
        value_ranges = result.get("valueRanges", [])

        if len(value_ranges) < 5:
            raise Exception("EEEEdata depletion")

        employees = value_ranges[0].get("values", [[]])[0] if value_ranges[0].get("values", []) else []
        dates = value_ranges[1].get("values", [[]])[0] if value_ranges[1].get("values", []) else []
        days_of_week = value_ranges[2].get("values", []) if len(value_ranges) > 2 else []
        objects = value_ranges[3].get("values", []) if len(value_ranges) > 3 else []
        especially_marks = value_ranges[4].get("values", []) if len(value_ranges) > 4 else []

        return employees, dates, days_of_week, objects, especially_marks

    except Exception as e:
        raise Exception(f"Ошибка при работе с sheets: {e}")

def timetable(employees, dates, days_of_week, objects, especially_marks):
    if not employees or not dates or not days_of_week or not objects or not especially_marks:
        return "Данных нет"

    days_order = {"Пн": 1, "Вт": 2, "Ср": 3, "Чт": 4, "Пт": 5}

    formatted_schedule = f"{dates[0]}\n\n"  # Добавляем дату
    for i, employee in enumerate(employees):
        formatted_schedule += f"<b>{employee}</b>:\n"
        days_dict = {}

        for row_index, row in enumerate(days_of_week):
            for index, mark_row in enumerate(especially_marks): 
                print(f"Row {index}: {mark_row}") 
            day = row[i] if len(row) > i else None
            if day:
                mark = (
                especially_marks[row_index][0].strip()
                if row_index < len(especially_marks) and especially_marks[row_index] and especially_marks[row_index][0]
                else None
            )
                obj = objects[row_index][0] if len(objects) > row_index and len(objects[row_index]) > 0 else "Нет объекта"
                mark = especially_marks[row_index][0] if len(especially_marks) > row_index and len(especially_marks[row_index]) > 0 else None
                obj_with_mark = f"{obj} ({mark})" if mark else obj
                day_key = day.strip()
                days_dict[day_key] = obj_with_mark

        sorted_days = sorted(
            days_dict.items(),
            key=lambda x: min(
                days_order.get(day.strip(), float('inf')) for day in x[0].split(",")
            )
        )
        for day, obj in sorted_days:
            formatted_schedule += f"{day} - {obj}\n"

    return formatted_schedule.strip()
    
async def send_google_sheets_data(query, context):
    try:
        employees, dates, days_of_week_data, objects, especially_marks = read_google_sheets()
        #employees2, dates2, days_of_week2, objects2 = read_google_sheets_twin()

        all_schedules = timetable(employees, dates, days_of_week_data, objects, especially_marks)
        #all_schedules2 = timetable_twin (employees2, dates2, days_of_week2, objects2)
        
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("Главное меню", callback_data="main_menu")]
        ])
        
        await query.message.reply_text(f"{all_schedules}", reply_markup=reply_markup, parse_mode="HTML")

    except Exception as e:
        error_message = f"Ошибка при работе с Google Sheets: {e}"
        await query.message.reply_text(error_message) 

async def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'notification_photomaker':
        await query.edit_message_text("Пожалуйста, введите ваше замечание:")
        context.user_data["aw_input"] = True

async def notification_photomaker_button(update: Update, context: CallbackContext) -> int:
    if context.user_data.get("aw_input"):
        notif_text = update.message.text.strip()
        
        context.user_data["notification"] = notif_text
        
        photomaker_chat_id = "-10024672734"  #чат ID
        await context.bot.send_message(chat_id=photomaker_chat_id, text=notif_text)

        await update.message.reply_text("Ваши данные успешно отправлены.")

        context.user_data["aw_input"] = False


async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text("Операция отменена.")
    return ConversationHandler.END
        
