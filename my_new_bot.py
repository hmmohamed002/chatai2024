import logging
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# إعداد السجل
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# تعريف التوكن ومفاتيح الاستضافة
TOKEN = '7600581966:AAHJMKucIxZjPXVQnjb1HEabj6A0jHyomo8'  # أدخل توكن البوت هنا
API_KEY = '83fae0405eabb4ee8'  # أدخل مفتاح محرك البحث الخاص بك هنا
HOSTING_KEY = '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'  # أدخل مفتاح الاستضافة هنا

# تعريف الدالة التي ستتعامل مع الأمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your bot!')

# الدالة الرئيسية
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # إضافة معالج الأمر /start
    app.add_handler(CommandHandler("start", start))

    # بدء عملية الاستجابة
    await app.run_polling()

# تشغيل التطبيق
if __name__ == '__main__':
    nest_asyncio.apply()  # استخدام nest_asyncio
    import asyncio

    asyncio.run(main())
