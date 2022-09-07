import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup


bot = telebot.TeleBot('5698669177:AAH0OzcM0sLMuGsrRqrbEqPprxZuwcgnxk0')


#собщение пользователю, ответы на команды

@bot.message_handler(commands=['start'])
def start(message):
    msg = f'Приветствуем, <b>{message.from_user.username}!</b>'
    bot.send_message(message.chat.id, msg, parse_mode='html')
    bot.send_message(message.chat.id, 'Мы осуществляем обмен криптовалюты в Приморском крае по следующим направлениям: BTC, USDT, ETH, USDC, DAI. По обмену обращаться к менеджеру @Chinganch. Для более подробного ознакомления с курсом нажмите /keyboard.',parse_mode='html')


@bot.message_handler(commands=['keyboard'])
def button1(message):
    murkup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    actualexchangerate=types.KeyboardButton('Актуальный курс')
    works=types.KeyboardButton('Как мы работаем')
    murkup.add(actualexchangerate, works)
    bot.send_message(message.chat.id, 'Перейдите', reply_markup=murkup)

#кнопки


@bot.message_handler(commands=['currency'])
def button2(messag):
    murkp=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    one = types.KeyboardButton('BTC')
    two = types.KeyboardButton('USDT')
    three = types.KeyboardButton('ETH')
    four= types.KeyboardButton('USDС')
    five=types.KeyboardButton('DAI')
    murkp.add(one, two, three, four, five)
    bot.send_message(messag.chat.id,'Выберите одну из криптовалют', reply_markup=murkp)


#логика кнопок


@bot.message_handler()
def get_text(message):
    if message.text == 'Актуальный курс':
        bot.send_message(message.chat.id, 'Для просмотра криптовалюты нажмите /currency', parse_mode='html')
    elif message.text == "Как мы работаем":
        bot.send_message(message.chat.id, 'нужен текст', parse_mode='html')
    elif message.text == "BTC":
         Dollar_Rub = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82+btc&ei=26MQY9CJIPKQrgTA85PgCw&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82+%D0%B8%D0%B5%D1%81+&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIICAAQHhAPEBY6BAgAEEM6BQgAEIAEOgoIABCxAxCDARBDOggIABCABBDJAzoFCAAQkgM6BwgAELEDEEM6CAgAEB4QFhAKSgQIQRgASgQIRhgAUPwpWOsvYOs5aAJwAXgAgAGzAYgBywaSAQMwLjWYAQCgAQHAAQE&sclient=gws-wiz"
         headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
         full_page = requests.get(Dollar_Rub, headers=headers)
         soup = BeautifulSoup(full_page.content, 'html.parser')
         convert = soup.findAll("span", {"class": "pclqee"})
         bot.send_message(message.chat.id, convert)
    elif message.text == "USDT":
        Dollar_Rub = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82+usdt&ei=86QQY5maFpGMrwToopqoDg&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82+usdt&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQgAQyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjoHCAAQRxCwAzoKCAAQRxCwAxDJAzoICAAQgAQQyQM6BQgAEJIDOgsIABCABBCxAxCDAToICAAQsQMQgwE6CAgAEIAEELEDOgcIABCABBAKOgoIABCABBBGEIICSgQIQRgASgQIRhgAUMEGWI4bYOkpaAFwAXgAgAG9AYgBkwmSAQMwLjeYAQCgAQHIAQjAAQE&sclient=gws-wiz"
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
        full_page = requests.get(Dollar_Rub, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "pclqee"})
        bot.send_message(message.chat.id, convert)
    elif message.text == "ETH":
        Dollar_Rub = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82+ETH&ei=rKgQY82dD5Wj3QOT-oH4DA&ved=0ahUKEwjNo_mNz_P5AhWVUXcKHRN9AM8Q4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82+ETH&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWOgcIABBHELADSgQIQRgASgQIRhgAUMQHWMQHYIAXaAJwAXgAgAGeAYgBngGSAQMwLjGYAQCgAQKgAQHIAQjAAQE&sclient=gws-wiz"
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
        full_page = requests.get(Dollar_Rub, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "pclqee"})
        bot.send_message(message.chat.id, convert)
    elif message.text == "USDС":
        Dollar_Rub = "https://www.google.com/search?q=usd+coin+wtyf&ei=eq8QY5aCDN6PwPAP7PmHwA0&ved=0ahUKEwiWp8nM1fP5AhXeBxAIHez8AdgQ4dUDCA4&uact=5&oq=usd+coin+wtyf&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEA0yBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBY6BwgAEEcQsAM6BwgAELADEEM6BAgAEEM6BQgAEIAESgQIQRgASgQIRhgAUIgIWOQUYPUXaAFwAXgAgAGyAYgBwgaSAQMwLjWYAQCgAQHIAQnAAQE&sclient=gws-wiz"
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
        full_page = requests.get(Dollar_Rub, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("div", {"class": "IZ6rdc"})
        bot.send_message(message.chat.id, convert)
    elif message.text == "DAI":
        Dollar_Rub = "https://www.coinbase.com/ru/converter/dai/rub"
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
        full_page = requests.get(Dollar_Rub, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("div", {"class": "cds-typographyResets-t1xhpuq2 cds-body-bvviwwo cds-currentColor-cl6elq7 cds-transition-txjiwsi cds-start-s1muvu8a"})
        bot.send_message(message.chat.id, convert)


bot.polling(none_stop=True)