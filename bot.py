from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import requests

# وظيفة للرد على الرسائل باستخدام API خارجي
async def respond(update: Update, context: CallbackContext):
    user_message = update.message.text
    # الاتصال بواجهة برمجة التطبيقات (API) للحصول على رد
    response = requests.get(f"https://api.example.com/ai?query={user_message}")
    bot_response = response.json().get('response', 'Sorry, I did not understand that.')
    await update.message.reply_text(bot_response)

# وظيفة لبدء البوت
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Hello! I am your AI bot. How can I assist you?')

if __name__ == '__main__':
    # ضع توكن بوت تلغرام الخاص بك هنا
    TOKEN = "7600581966:AAHJMKucIxZjPXVQnjb1HEabj6A0jHyomo8"
    
    # إنشاء تطبيق
    application = Application.builder().token(TOKEN).build()

    # إضافة معالجات الأوامر
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))

    # بدء البوت
    application.run_polling()
