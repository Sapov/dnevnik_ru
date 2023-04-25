from pydnevnikruapi.dnevnik import dnevnik
from datetime import datetime, time
import data_pass_for_prod
import schedule
from send_mail import send_mail

from time import sleep


# Получаем доступ через логин и пароль
def print_homework(login, password):
    dn = dnevnik.DiaryAPI(login, password)
    curent_datetime = datetime.now()
    a = dn.get_school_homework(data_pass_for_prod.idschool,
                               datetime(curent_datetime.year, curent_datetime.month, curent_datetime.day + 1),
                               datetime(curent_datetime.year, curent_datetime.month, curent_datetime.day + 1))
    lst_homework = []
    for i in a['works']:
        lst_homework.append(f'{"=" * 4} Предмет: {data_pass_for_prod.items[i["subjectId"]]} {"=" * 4}\nЗадание:{i["text"]}\n')
    return lst_homework


def main():
    today_ = datetime.today()
    print(today_)
    print(type(today_))
    time_format = today_.strftime('%d/%m/%y')

    lst = print_homework(login=data_pass_for_prod.login, password=data_pass_for_prod.password)
    text = str(f'{"-" * 6} Дата: {time_format} {"-" * 6}\n\n')
    for i in range(len(lst)):
        text += lst[i] + " \n"
    print(text)

    send_mail(text, f'Илюшкина домашка на {time_format}', dest_email=data_pass_for_prod.mail_mather)
    send_mail(text, f'Илюшкина домашка на {time_format}', dest_email=data_pass_for_prod.mail_phather)


    # pywhatkit.sendwhatmsg('data.tel', text, 0, 53, 15, True, 2)


#    pywhatkit.sendwhatmsg(data_pass.tel, text, curent_datetime.hour, curent_datetime.minute + 1, 15, True, 2)


if __name__ == '__main__':
    main()

    # schedule.every().day.at("14:00").do(main)
    schedule.every().monday.at("11:20").do(main)
    schedule.every().tuesday.at("11:10").do(main)
    schedule.every().wednesday.at("11:00").do(main)
    schedule.every().thursday.at("11:25").do(main)
    #   schedule.every().friday.at("19:00").do(main)
    schedule.every().sunday.at("11:00").do(main)
    while True:
        schedule.run_pending()
        sleep(1)
        data = datetime.now()

        print('каждую сек __::__', data)
