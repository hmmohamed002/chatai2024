from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# استبدل بـ توكن البوت الخاص بك
TOKEN = '7600581966:AAHJMKucIxZjPXVQnjb1HEabj6A0jHyomo8'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! أنا بوت ذكاء اصطناعي. كيف يمكنني مساعدتك اليوم؟')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('يمكنني مساعدتك في العديد من الأمور! فقط اسألني.')

def main() -> None:
    updater = Updater(TOKEN)

    # الحصول على الموزع
    dispatcher = updater.dispatcher

    # إضافة أوامر البوت
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
