from transformers import AutoModelForMaskedLM, AutoTokenizer, pipeline
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# تحميل النموذج والتوكن
model_name = "aubmindlab/bert-base-arabertv02"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForMaskedLM.from_pretrained(model_name)

# إعداد pipeline لإكمال الجمل الناقصة
nlp = pipeline("fill-mask", model=model, tokenizer=tokenizer)

# دالة لمعالجة الرسائل الواردة من المستخدم
def reply_message(update: Update, context: CallbackContext):
    user_message = update.message.text

    # إذا كانت الجملة تحتوي على [MASK] يتم ملء القناع
    if "[MASK]" in user_message:
        response = nlp(user_message)
        completed_text = response[0]['sequence']
        update.message.reply_text(f"الإجابة: {completed_text}")
    else:
        update.message.reply_text("يرجى إرسال رسالة تتضمن [MASK] ليقوم النموذج بتعبئتها.")

# إعداد البوت
def main():
    token = "7600581966:AAHJMKucIxZjPXVQnjb1HEabj6A0jHyomo8"  # توكن البوت الخاص بك
    updater = Updater(token)
    dispatcher = updater.dispatcher

    # التعامل مع الرسائل النصية
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_message))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
