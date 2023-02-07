from pydnevnikruapi.dnevnik import dnevnik
from datetime import datetime
import data
import pywhatkit
import schedule
# import send_mail
from send_mail import send_mail


# Получаем доступ через логин и пароль
def print_homework(login, password):
    dn = dnevnik.DiaryAPI(login, password)
    curent_datetime = datetime.now()
    a = dn.get_school_homework(data.idschool,
                               datetime(curent_datetime.year, curent_datetime.month, curent_datetime.day + 1),
                               datetime(curent_datetime.year, curent_datetime.month, curent_datetime.day + 1))
    lst_homework = []
    for i in a['works']:
        lst_homework.append(f'{"=" * 4} Предмет: {data.items[i["subjectId"]]} {"=" * 4}\nЗадание:{i["text"]}\n')
    return lst_homework




def main():
    today_ = datetime.today()
    time_format = today_.strftime('%m/%d/%y')

    lst = print_homework(login=data.login, password=data.password)
    text = str(f'{"-" * 6} Дата: {time_format} {"-" * 6}\n\n')
    for i in range(len(lst)):
        text += lst[i] + " \n"
    print(text)

    send_mail(text, f'Илюшкина домашка на {time_format}', dest_email='grechanka83@mail.ru')
    send_mail(text, f'Илюшкина домашка на {time_format}', dest_email='sapov@mail.ru')

    # pywhatkit.sendwhatmsg('data.tel', text, 0, 53, 15, True, 2)
    # pywhatkit.sendwhatmsg(data.tel, text, curent_datetime.hour, curent_datetime.minute + 1, 15, True, 2)


if __name__ == '__main__':
    main()
    # schedule.every().day.at("14:00").do(main)
    schedule.every().monday.at("16:20").do(main)
    schedule.every().tuesday.at("18:55").do(main)
    schedule.every().wednesday.at("14:00").do(main)
    schedule.every().thursday.at("14:00").do(main)
    schedule.every().friday.at("14:00").do(main)
    while True:
        schedule.run_pending()
