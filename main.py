from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, CallbackQueryHandler, CallbackContext, filters
from insp360 import check_in, button, save_check_in, cancel, INPUT_DATA, handle_input, PHOTO_CHECK, photo_check, start, handle_no_input, send_google_sheets_data, AWAITING_NOTE#, notification_photomaker_button, button_handler,  handle_note_input,send_message_photomaker, 

def main() -> None:
    TOKEN = "7760617545:AAFAeBG8CDipHTEYRSW5Dt0sKWM56dFeON0"
    application = Application.builder().token(TOKEN).build()
    
    conv_handler = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(check_in, pattern="^check_in$"),
            ],
        states={
            INPUT_DATA: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_input)],
            PHOTO_CHECK: [CallbackQueryHandler(photo_check, pattern='^(yesyes|ohno)$')],
            "INPUT_DATA2": [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_no_input)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CallbackQueryHandler(send_google_sheets_data, pattern="^google_sheets$"))
    application.run_polling()

if __name__ == "__main__":
    main()