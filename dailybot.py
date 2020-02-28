import time

import telepot
from telepot.loop import MessageLoop
from khayyam import JalaliDate
from config import TOKEN, PROXY, channel_id
from khayyam import JalaliDatetime
from num2fawords import words


def dayrep(day):
    if day == 1:
        return 'یکم'
    if day == 2:
        return 'دوم'
    if day == 3:
        return 'سوم'
    if day == 4:
        return 'چهارم'
    if day == 5:
        return 'پنجم'
    if day == 6:
        return 'ششم'
    if day == 7:
        return 'هفتم'
    if day == 8:
        return 'هشتم'
    if day == 9:
        return 'نهم'
    if day == 10:
        return 'دهم'
    if day == 11:
        return 'یازدهم'
    if day == 12:
        return 'دوازدهم'
    if day == 13:
        return 'سیزدهم'
    if day == 14:
        return 'چهاردهم'
    if day == 15:
        return 'پانزدهم'
    if day == 16:
        return 'شانزدهم'
    if day == 17:
        return 'هفدهم'
    if day == 18:
        return 'هجدهم'
    if day == 19:
        return 'نوزدهم'
    if day == 20:
        return 'بیستم'
    if day < 30:
        return 'بسیت و ' + dayrep(day % 10)
    if day == 30:
        return 'سیم'
    return 'سی و ' + dayrep(day % 10)


day_message_was_sent = -1


def message_handler(msg):
    global day_message_was_sent
    content_type, chat_type, chat_id = telepot.glance(msg)
    if (chat_id == channel_id):
        day_message_was_sent = JalaliDatetime.now().day


if __name__ == '__main__':
    if PROXY:
        telepot.api.set_proxy(PROXY)

    bot = telepot.Bot(TOKEN)
    MessageLoop(bot, {'chat': message_handler}).run_as_thread()

    while True:
        now = JalaliDatetime.now()
        if now.minute == 59 and now.hour == 23:
            if day_message_was_sent != now.day:
                bot.sendMessage(channel_id,
                                now.weekdayname() + '\n' + dayrep(now.day) + ' ' + now.monthname() + ' ' + words(
                                    now.year % 100))
                day_message_was_sent = now.day
        # bot.sendMessage(channel_id, JalaliDate(1394, 5, 6).localdateformat())
        # break
        time.sleep(5)
