from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
from insp360 import start, button

def main() -> None:
    TOKEN = "7760617545:AAFAeBG8CDipHTEYRSW5Dt0sKWM56dFeON0"
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))  #обработка нажатия кнопки

    application.run_polling()

if __name__ == "__main__":
    main()