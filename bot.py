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

def kyps():
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
    
    
    if(message.text == "Доллар США"):
        bot.send_message(message.chat.id, text=f"1 Доллар США (USD) *{kyps()[kyps().find('Доллар США')+10:kyps().find('978 EUR')-4:]}* руб.", parse_mode="Markdown")
    
    if(message.text == "Евро"):  
        bot.send_message(message.chat.id, text=f"1 Евро (EUR) *{kyps()[kyps().find('Евро')+4:kyps().find('356 INR')-4:]}* руб.", parse_mode="Markdown")
    
    if(message.text == "Китайский юань"):        
        bot.send_message(message.chat.id, text=f"10 Китайских юаней (CNY) *{kyps()[kyps().find('Китайских юаней')+15:kyps().find('498 MDL')-4:]}* руб.", parse_mode="Markdown")
    
    if(message.text == "Прочие валюты"):
        bot.send_message(message.chat.id, text=f"1 Бразильский реал (BRL) *{kyps()[kyps().find('Бразильский реал')+16:kyps().find('348 HUF')-4:]}* руб.\n\
1 Австралийский доллар (AUD) *{kyps()[kyps().find('Австралийский доллар')+20:kyps().find('944 AZN')-4:]}* руб.\n\
1000 Вон Республики Корея (KRW) *{kyps()[kyps().find('Вон Республики Корея')+20:kyps().find('344 HKD')-4:]}* руб.\n\
10 Гонконгских долларов (HKD) *{kyps()[kyps().find('Гонконгских долларов')+20:kyps().find('208 DKK')-4:]}* руб.\n\
1 Канадский доллар (CAD) *{kyps()[kyps().find('Канадский доллар')+16:kyps().find('417 KGS')-4:]}* руб.\n\
10 Норвежских крон (NOK) *{kyps()[kyps().find('Норвежских крон')+15:kyps().find('985 PLN')-4:]}* руб.\n\
1 Сингапурский доллар (SGD) *{kyps()[kyps().find('Сингапурский доллар')+19:kyps().find('972 TJS')-4:]}* руб.\n\
10 Турецких лир (TRY) *{kyps()[kyps().find('Турецких лир')+12:kyps().find('860 UZS')-4:]}* руб.\n\
1 Фунт стерлингов Соединенного королевства (GBP) *{kyps()[kyps().find('Фунт стерлингов Соединенного королевства')+40:kyps().find('203 CZK')-4:]}* руб.\n\
1 Швейцарский франк (CHF) *{kyps()[kyps().find('Швейцарский франк')+17:kyps().find('710 ZAR')-4:]}* руб.\n\
10 Южноафриканских рэндов (ZAR) *{kyps()[kyps().find('Южноафриканских рэндов')+22:kyps().find('392 JPY')-4:]}* руб.\n\
100 Индийских рупий (INR) *{kyps()[kyps().find('Индийских рупий')+15:kyps().find('398 KZT')-4:]}* руб.\n\
100 Японских иен (JPY) *{kyps()[kyps().find('Японских иен')+12:-5]}* руб.", parse_mode="Markdown")
    
    if(message.text == "Валюты стран СНГ"):
        bot.send_message(message.chat.id, text=f"1 Азербайджанский манат (AZN) *{kyps()[kyps().find('Азербайджанский манат')+21:kyps().find('051 AMD')-4:]}* руб.\n\
100 Армянских драмов (AMD) *{kyps()[kyps().find('Армянских драмов')+16:kyps().find('933 BYN')-4:]}* руб.\n\
100 Казахстанских тенге (KZT) *{kyps()[kyps().find('Казахстанских тенге')+19:kyps().find('124 CAD')-4:]}* руб.\n\
100 Киргизских сомов (KGS) *{kyps()[kyps().find('Киргизских сомов')+16:kyps().find('156 CNY')-4:]}* руб.\n\
10 Молдавских леев (MDL) *{kyps()[kyps().find('Молдавских леев')+15:kyps().find('934 TMT')-4:]}* руб.\n\
1 Новый туркменский манат (TMT) *{kyps()[kyps().find('Новый туркменский манат')+23:kyps().find('578 NOK')-4:]}* руб.\n\
10 Таджикских сомони (TJS) *{kyps()[kyps().find('Таджикских сомони')+17:kyps().find('949 TRY')-4:]}* руб.\n\
10000 Узбекских сумов (UZS) *{kyps()[kyps().find('Узбекских сумов')+15:kyps().find('980 UAH')-4:]}* руб.\n\
10 Украинских гривен (UAH) *{kyps()[kyps().find('Украинских гривен')+17:kyps().find('826 GBP')-4:]}* руб.", parse_mode="Markdown")
            
    if(message.text == "Валюты стран ЕC"):
        bot.send_message(message.chat.id, text=f"1 Болгарский лев (BGN) *{kyps()[kyps().find('Болгарский лев')+14:kyps().find('986 BRL')-4:]}* руб.\n\
100 Венгерских форинтов (HUF) *{kyps()[kyps().find('Венгерских форинтов')+19:kyps().find('410 KRW')-4:]}* руб.\n\
10 Датских крон (DKK) *{kyps()[kyps().find('Датских крон')+12:kyps().find('840 USD')-4:]}* руб.\n\
1 Польский злотый (PLN) *{kyps()[kyps().find('Польский злотый')+15:kyps().find('946 RON')-4:]}* руб.\n\
1 Румынский лей (RON) *{kyps()[kyps().find('Румынский лей')+13:kyps().find('960 XDR')-4:]}* руб.\n\
10 Чешских крон (CZK) *{kyps()[kyps().find('Чешских крон')+12:kyps().find('752 SEK')-4:]}* руб.\n\
10 Шведских крон (SEK) *{kyps()[kyps().find('Шведских крон')+13:kyps().find('756 CHF')-4:]}* руб.", parse_mode="Markdown")
            
            
  
bot.infinity_polling()

    
