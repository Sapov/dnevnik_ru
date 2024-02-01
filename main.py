import pywhatkit
from pydnevnikruapi.dnevnik import dnevnik
from datetime import datetime, time
import data_pass_for_prod
import schedule
from send_mail import send_mail

from time import sleep


class HomeWork:
    def __init__(self, login, password):
        self.password = password
        self.login = login

    # Получаем доступ через логин и пароль
    def print_homework(self, login, password):
        """получаем домашку на следующий день"""
        dn = dnevnik.DiaryAPI(login, password)
        current_datetime = datetime.now()
        a = dn.get_school_homework(data_pass_for_prod.idschool,
                                   datetime(current_datetime.year, current_datetime.month, current_datetime.day + 1),
                                   datetime(current_datetime.year, current_datetime.month, current_datetime.day + 1))
        lst_homework = []
        for i in a['works']:
            lst_homework.append(
                f'{"=" * 4} Предмет: {data_pass_for_prod.items[i["subjectId"]]} {"=" * 4}\nЗадание:{i["text"]}\n')
        return lst_homework

    def main(self):
        today_ = datetime.today()
        time_format = today_.strftime('%d/%m/%y')

        lst = self.print_homework(login=data_pass_for_prod.login, password=data_pass_for_prod.password)
        text = str(f'{"-" * 6} Дата: {time_format} {"-" * 6}\n\n')
        for i in range(len(lst)):
            text += lst[i] + " \n"
        print(text)

        # send_mail(text, f'Илюшкина домашка на {time_format}', dest_email=data_pass_for_prod.mail_mather)
        send_mail(text, f'Илюшкина домашка на {time_format}', dest_email=data_pass_for_prod.mail_phather)

        # pywhatkit.sendwhatmsg('+79531193367', text, 11, 40, 1, True, 2)


# pywhatkit.sendwhatmsg(data_pass_for_prod.tel, text, current_datetime.hour, current_datetime.minute + 1, 15, True, 2)


if __name__ == '__main__':
    hm = HomeWork(data_pass_for_prod.login, data_pass_for_prod.password)

    schedule.every().monday.at("21:12").do(hm.main)
    schedule.every().tuesday.at("11:10").do(hm.main)
    schedule.every().wednesday.at("11:00").do(hm.main)
    schedule.every().thursday.at("11:25").do(hm.main)
    #   schedule.every().friday.at("19:00").do(main)
    schedule.every().sunday.at("11:00").do(hm.main)
    while True:
        schedule.run_pending()
        sleep(1)
        data = datetime.now()

        print('каждую сек __::__', data)
