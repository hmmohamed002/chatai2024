import asyncio
import requests
from transformers import AutoTokenizer
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackContext
import nest_asyncio

# تفعيل النست آسيكيو
nest_asyncio.apply()

# تحميل التوكن
MODEL_NAME = "aubmindlab/bert-base-arabertv02"
API_KEY = "AIzaSyCjqW6tpW2eeA0eQFGExjmFkE1lxdub9Qo"
SEARCH_ENGINE_ID = "83fae0405eabb4ee8"
BOT_TOKEN = "7600581966:AAHJMKucIxZjPXVQnjb1HEabj6A0jHyomo8"

# تحميل المحول
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# دالة لإجراء البحث في Google
def google_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
    response = requests.get(url)
    results = response.json()
    
    if "items" in results:
        return results["items"][0]["snippet"]
    
    return "لا توجد نتائج."

# دالة لمعالجة الرسائل
async def reply_message(update: Update, context: CallbackContext):
    user_message = update.message.text

    # استخدام التوكنايزر لتقطيع النص
    tokens = tokenizer.tokenize(user_message)
    
    # إجراء البحث وإرسال النتائج
    search_result = google_search(user_message)

    # إعداد الرسالة
    message = f"تم تقطيع النص إلى: {tokens}\n\nنتيجة البحث: {search_result}"
    max_length = 4096  # الطول الأقصى المسموح به للرسالة
    if len(message) > max_length:
        message = message[:max_length - 3] + '...'  # إضافة ثلاث نقاط للإشارة إلى أن الرسالة قد قُصت

    await update.message.reply_text(message)

# إعداد البوت
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # إضافة معالج الرسائل
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

    # بدء البوت
    await app.run_polling()

# تشغيل البرنامج
if __name__ == '__main__':
    asyncio.run(main())
