from dotenv import load_dotenv
import os
import requests
from telegram import Bot

load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY')
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=fa"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        return f"آب و هوای شهر {city}:\n{desc}\nدمای هوا: {temp}°C\nرطوبت: {humidity}%"
    else:
        return "خطا در دریافت اطلاعات هواشناسی."

def send_message(text):
    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHANNEL_ID, text=text)

if __name__ == "__main__":
    city_name = "Tehran"  # می‌تونی اینو به هر شهری تغییر بدی
    weather_report = get_weather(city_name)
    send_message(weather_report)
    print("پیام آب و هوا ارسال شد ✅")
