import nest_asyncio
nest_asyncio.apply()
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
import requests
import asyncio


logging.basicConfig(filename='bot_log.txt',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


BOT_TOKEN = '7600581966:AAHJMKucIxZjPXVQnjb1HEabj6A0jHyomo8'
# Google API
GOOGLE_API_KEY = 'AIzaSyCjqW6tpW2eeA0eQFGExjmFkE1lxdub9Qo'

SEARCH_ENGINE_ID = '83fae0405eabb4ee8'
# رمز API من Hugging Face
HUGGING_FACE_API_KEY = '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'


async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text.lower()

    # مجموعة من الأجوبة المتاحة
    responses = {
        "كيفك": "أنا بخير شكراً لسؤالك! كيف حالك أنت",
        "السلام عليكم": "وعليكم السلام والرحمة كيف يمكنني مساعدتك",
        "مرحبا": "مرحباً بك! كيف يمكنني مساعدتك؟🧠",
        "كيف حالك": "أنا بخير، شكراً لسؤالك!",
        "كيف حال الطقس": "الطقس جميل اليوم.",
        "ما وظيفتك": "وظيفتي مساعدتك.",
        "كيف تم تطويرك": "تم تطويري وتدريبي باستخدام مجموعة كبيرة ومتنوعة من البيانات، مما يساعدني في تقديم معلومات دقيقة ومفيدة في مجالات متعددة. يعتمد تعلمي على تقنيات التعلم الآلي.",
        "من أنت": "أنا بوت ذكاء اصطناعي تم تطويره بواسطة @QCM_7👨🏻‍💻 لمساعدتك.",
        "من قام بتطويرك": "أنا بوت ذكاء اصطناعي تم تطويره بواسطة @QCM_7👨🏻‍💻",
        "ما هي لغتك المفضلة": "أحب التواصل باللغة العربية.",
        "ما هو الذكاء الاصطناعي": "الذكاء الاصطناعي هو فرع من علوم الكمبيوتر يهدف إلى إنشاء أنظمة قادرة على القيام بمهام تتطلب ذكاء بشري.",
        "ما هي تطبيقات الذكاء الاصطناعي": "تتضمن التطبيقات الشائعة للذكاء الاصطناعي معالجة اللغة الطبيعية، التعلم الآلي، الرؤية الحاسوبية، والروبوتات.",
        "كيف تعمل محركات البحث": "تعمل محركات البحث عن طريق الزحف إلى صفحات الويب وفهرستها، ثم تستخدم خوارزميات لتقديم النتائج ذات الصلة عند البحث.",
        "ما هي أكبر شركات الذكاء الاصطناعي": "تشمل الشركات الكبرى في هذا المجال جوجل، أمازون، فيسبوك، وOpenAI.",
        "ما هي تقنية التعلم العميق": "التعلم العميق هو جزء من التعلم الآلي يستخدم الشبكات العصبية الاصطناعية لمحاكاة طريقة تفكير البشر.",
        "كيف يمكنني تحسين مهاراتي في البرمجة": "يمكنك تحسين مهاراتك من خلال ممارسة البرمجة بانتظام، المشاركة في المشاريع، وقراءة الكتب والمقالات في مجال البرمجة.",
        "ما هي فوائد الذكاء الاصطناعي": "تشمل الفوائد تحسين الكفاءة، تقليل الأخطاء، وزيادة السرعة في اتخاذ القرارات.",
        "كيف يمكنني البدء في تعلم الذكاء الاصطناعي": "يمكنك البدء من خلال دراسة الرياضيات، تعلم البرمجة، والالتحاق بالدورات التدريبية المتخصصة.",
        "ما هي أدوات تطوير الذكاء الاصطناعي": "تشمل أدوات تطوير الذكاء الاصطناعي بايثون، TensorFlow، Keras، وPyTorch.",
        "ما هو الفرق بين الذكاء الاصطناعي والتعلم الآلي": "الذكاء الاصطناعي هو المفهوم العام، بينما التعلم الآلي هو فرع ضمن الذكاء الاصطناعي يركز على تدريب النماذج.",
        "ما هي أخلاقيات الذكاء الاصطناعي": "تشمل أخلاقيات الذكاء الاصطناعي قضايا مثل الخصوصية، الشفافية، والتمييز.",
        "ما هو مستقبل الذكاء الاصطناعي": "من المتوقع أن يستمر الذكاء الاصطناعي في التطور وسيؤثر على العديد من جوانب حياتنا اليومية.",
        "ما هو مفهوم البيانات الكبيرة": "البيانات الكبيرة تشير إلى كميات ضخمة من البيانات التي تتطلب تقنيات متقدمة لمعالجتها وتحليلها.",
    }

    # الرد من الأجوبة المخزنة
    if user_message in responses:
        await update.message.reply_text(responses[user_message])
    else:
        # هنا نستخدم Hugging Face's Inference API
        url = "https://api-inference.huggingface.co/models/asafaya/bert-base-arabic"
        headers = {"Authorization": f"Bearer {HUGGING_FACE_API_KEY}"}
        payload = {
            "inputs": {
                "question": user_message,
                "context": " ".join(responses.values())
            }
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            answer = response.json()
            await update.message.reply_text(answer['answer'])
        else:
            await update.message.reply_text("حدث خطأ أثناء معالجة طلبك. حاول مرة أخرى.")

# دالة البدء
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("مرحبا أنا مساعد ذكاء اصطناعي 🤖 يمكنني الإجابة على أسئلتك حول مجموعة متنوعة من المواضيع. كيف يمكنني مساعدتك؟")

# إعداد التطبيق
if __name__ == "__main__":
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    
    application.run_polling()
