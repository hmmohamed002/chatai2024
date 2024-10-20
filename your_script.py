import requests
from random import choice, randrange
import re
import time
import os
import webbrowser

# استبدل هذه القيم بالقيم الصحيحة الخاصة بك
BOT_TOKEN = '7813807932:AAFL2zGkGbaSCYLIPQ7fwf4Np5FJymr269k'
CHAT_ID = '7456101114'

# دالة للتحقق من توفر الإيميل في Gmail
def check_gmail(email):
    # هنا يجب إضافة المنطق للتحقق من Gmail، مثل استخدام واجهة برمجة التطبيقات لـ Google.
    # سأستخدم placeholder هنا. استبدلها بالتحقق الفعلي.
    return True  # يجب استبداله بتحقق حقيقي

# دالة للتحقق مما إذا كان الإيميل مستخدمًا في إنستغرام
def check_instagram(email):
    # هنا يجب إضافة المنطق للتحقق من إنستغرام.
    # سأستخدم placeholder هنا. استبدلها بالتحقق الفعلي.
    return True  # يجب استبداله بتحقق حقيقي

# دالة لإرسال الإيميل إلى البوت
def send_to_bot(email):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': f'Email found: {email}'
    }
    requests.post(url, data=payload)

# توليد الإيميلات وفحصها
def generate_and_check_emails():
    yy = 'qwertyuiopasdfghjklzxcvbnm'
    while True:
        # توليد إيميل عشوائي
        email = ''.join(choice(yy) for _ in range(randrange(6, 9))) + '@gmail.com'
        
        # تحقق من Gmail
        if check_gmail(email):
            # تحقق من إنستغرام
            if check_instagram(email):
                send_to_bot(email)
                print(f'Email sent to bot: {email}')
        
        time.sleep(1)  # تأخير لتفادي الحظر أو التحميل الزائد

# بدء العملية
generate_and_check_emails()
