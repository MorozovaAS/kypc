import telebot
from token_1 import t
from bs4 import BeautifulSoup
import requests
from telebot import types


bot = telebot.TeleBot(t)

@bot.message_handler(commands=["start"])
def buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Доллар США")
    btn2 = types.KeyboardButton("Евро")
    btn3 = types.KeyboardButton("Китайский юань")
    btn4 = types.KeyboardButton("Валюты стран СНГ") 
    btn5 = types.KeyboardButton("Валюты стран ЕC")  
    btn6 = types.KeyboardButton("Прочие валюты") 
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Тут ты можешь узнать курс иностранных валют к рублю по ЦБ на сегодня".format(message.from_user), reply_markup=markup)

def Exchange_Rates():
    url = 'https://www.cbr.ru/currency_base/daily/'
    page = requests.get(url)
    
    selected_data = []
    all_currencies = []
    soup = BeautifulSoup(page.text, "html.parser")
    all_currencies = soup.findAll(class_='table-wrapper')

    for data in all_currencies:
        if data.find(class_='table') is not None:
            selected_data.append(data.text)
    result = ' '.join(selected_data[0].split('\n'))

    return result

@bot.message_handler(content_types=['text'])
def func(message):
    
    currency = Exchange_Rates()
    
    if(message.text == "Доллар США"):
        bot.send_message(message.chat.id, text=f"1 Доллар США (USD) *{currency[currency.find('Доллар США')+10:currency.find('978 EUR')-4:]}* руб.", parse_mode="Markdown")
    
    if(message.text == "Евро"):  
        bot.send_message(message.chat.id, text=f"1 Евро (EUR) *{currency[currency.find('Евро')+4:currency.find('356 INR')-4:]}* руб.", parse_mode="Markdown")
    
    if(message.text == "Китайский юань"):        
        bot.send_message(message.chat.id, text=f"10 Китайских юаней (CNY) *{currency[currency.find('Китайских юаней')+15:currency.find('498 MDL')-4:]}* руб.", parse_mode="Markdown")
    
    if(message.text == "Прочие валюты"):
        bot.send_message(message.chat.id, text=f"1 Бразильский реал (BRL) *{currency[currency.find('Бразильский реал')+16:currency.find('348 HUF')-4:]}* руб.\n\
1 Австралийский доллар (AUD) *{currency[currency.find('Австралийский доллар')+20:currency.find('944 AZN')-4:]}* руб.\n\
1000 Вон Республики Корея (KRW) *{currency[currency.find('Вон Республики Корея')+20:currency.find('344 HKD')-4:]}* руб.\n\
10 Гонконгских долларов (HKD) *{currency[currency.find('Гонконгских долларов')+20:currency.find('208 DKK')-4:]}* руб.\n\
1 Канадский доллар (CAD) *{currency[currency.find('Канадский доллар')+16:currency.find('417 KGS')-4:]}* руб.\n\
10 Норвежских крон (NOK) *{currency[currency.find('Норвежских крон')+15:currency.find('985 PLN')-4:]}* руб.\n\
1 Сингапурский доллар (SGD) *{currency[currency.find('Сингапурский доллар')+19:currency.find('972 TJS')-4:]}* руб.\n\
10 Турецких лир (TRY) *{currency[currency.find('Турецких лир')+12:currency.find('860 UZS')-4:]}* руб.\n\
1 Фунт стерлингов Соединенного королевства (GBP) *{currency[currency.find('Фунт стерлингов Соединенного королевства')+40:currency.find('203 CZK')-4:]}* руб.\n\
1 Швейцарский франк (CHF) *{currency[currency.find('Швейцарский франк')+17:currency.find('710 ZAR')-4:]}* руб.\n\
10 Южноафриканских рэндов (ZAR) *{currency[currency.find('Южноафриканских рэндов')+22:currency.find('392 JPY')-4:]}* руб.\n\
100 Индийских рупий (INR) *{currency[currency.find('Индийских рупий')+15:currency.find('398 KZT')-4:]}* руб.\n\
100 Японских иен (JPY) *{currency[currency.find('Японских иен')+12:-5]}* руб.", parse_mode="Markdown")
    
    if(message.text == "Валюты стран СНГ"):
        bot.send_message(message.chat.id, text=f"1 Азербайджанский манат (AZN) *{currency[currency.find('Азербайджанский манат')+21:currency.find('051 AMD')-4:]}* руб.\n\
100 Армянских драмов (AMD) *{currency[currency.find('Армянских драмов')+16:currency.find('933 BYN')-4:]}* руб.\n\
100 Казахстанских тенге (KZT) *{currency[currency.find('Казахстанских тенге')+19:currency.find('124 CAD')-4:]}* руб.\n\
100 Киргизских сомов (KGS) *{currency[currency.find('Киргизских сомов')+16:currency.find('156 CNY')-4:]}* руб.\n\
10 Молдавских леев (MDL) *{currency[currency.find('Молдавских леев')+15:currency.find('934 TMT')-4:]}* руб.\n\
1 Новый туркменский манат (TMT) *{currency[currency.find('Новый туркменский манат')+23:currency.find('578 NOK')-4:]}* руб.\n\
10 Таджикских сомони (TJS) *{currency[currency.find('Таджикских сомони')+17:currency.find('949 TRY')-4:]}* руб.\n\
10000 Узбекских сумов (UZS) *{currency[currency.find('Узбекских сумов')+15:currency.find('980 UAH')-4:]}* руб.\n\
10 Украинских гривен (UAH) *{currency[currency.find('Украинских гривен')+17:currency.find('826 GBP')-4:]}* руб.", parse_mode="Markdown")
            
    if(message.text == "Валюты стран ЕC"):
        bot.send_message(message.chat.id, text=f"1 Болгарский лев (BGN) *{currency[currency.find('Болгарский лев')+14:currency.find('986 BRL')-4:]}* руб.\n\
100 Венгерских форинтов (HUF) *{currency[currency.find('Венгерских форинтов')+19:currency.find('410 KRW')-4:]}* руб.\n\
10 Датских крон (DKK) *{currency[currency.find('Датских крон')+12:currency.find('840 USD')-4:]}* руб.\n\
1 Польский злотый (PLN) *{currency[currency.find('Польский злотый')+15:currency.find('946 RON')-4:]}* руб.\n\
1 Румынский лей (RON) *{currency[currency.find('Румынский лей')+13:currency.find('960 XDR')-4:]}* руб.\n\
10 Чешских крон (CZK) *{currency[currency.find('Чешских крон')+12:currency.find('752 SEK')-4:]}* руб.\n\
10 Шведских крон (SEK) *{currency[currency.find('Шведских крон')+13:currency.find('756 CHF')-4:]}* руб.", parse_mode="Markdown")
            
            
  
bot.infinity_polling()

    
