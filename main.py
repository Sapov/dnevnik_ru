from pydnevnikruapi.dnevnik import dnevnik
from datetime import datetime, date
import data
import pywhatkit
import schedule


# Получаем доступ через логин и пароль
def print_homework():
    dn = dnevnik.DiaryAPI(login=data.login, password=data.password)
    curent_datetime = datetime.now()
    a = dn.get_school_homework(data.idschool,
                               datetime(curent_datetime.year, curent_datetime.month, curent_datetime.day + 1),
                               datetime(curent_datetime.year, curent_datetime.month, curent_datetime.day + 1))
    print(f'Дата: {datetime.now()}')
    # print(
    #     dn.get_school_homework(1000009667923, datetime(2022, 10, 18), datetime(2022, 10, 18))
    # )

    # a = dn.get_school_homework(1000009667923, datetime(2022, 10, 18), datetime(2022, 10, 18))
    lst_homework = []
    for i in a['works']:
        lst_homework.append(f'{"*" * 4} Предмет: {data.items[i["subjectId"]]} {"*" * 4}\nЗадание:{i["text"]}\n')
        # print(items[i["subjectId"]], i['text'])
    # print(*lst_homework)
    # print(dn.get_person_average_marks(1000012607869, time.time()))
    return lst_homework


# def scheduller():
#     schedule.every().day.at("19:31").do(main)


def main():
    lst = print_homework()
    text = ''
    for i in range(len(lst)):
        text += lst[i] + " \n"
    curent_datetime = datetime.now()

    # pywhatkit.sendwhatmsg('data.tel', text, 0, 53, 15, True, 2)
    pywhatkit.sendwhatmsg(data.tel, text, curent_datetime.hour, curent_datetime.minute + 1, 15, True, 2)


if __name__ == '__main__':
    main()