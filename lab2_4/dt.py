from datetime import datetime
import locale

def add_event():
    #datetime_str = input("Date: day/month/year(4 digits)")
    #event = input("Event:")
    event = "Event 1"
    datetime_str = '19/02/2018'
    event_date = datetime.strptime(datetime_str, '%d/%m/%Y')
    f = open('Calendar.txt', 'a')
    formatted_date = event_date.strftime("%d.%m.%Y")
    print(formatted_date)
    f.write(formatted_date+" "+event+"\n")

#Створіть функцію, яка має наступний функціонал: користувач вводить дату да текст.
# Функція записує у файл «Календар» дату та відповідну подію. Сортувати дати не потрібно.
add_event()

#Розрахуйте дату свого народження та свій вік (від сьогодні) так, як його рахує комп’ютер (у мілісекундах).
mydate_str = '03/05/1976'
my_date = datetime.strptime(mydate_str, '%d/%m/%Y')
now = datetime.now()
delta = now - my_date
print("My age:")
print(delta)
print("My age: in ms {}".format(int(delta.total_seconds()*1000000)))
#event_date = datetime.strptime(datetime_str, '%d/%m/%Y')

#Виведіть поточну дату у форматах, прийнятих у різних сторонах світу.
now = datetime.now()
locale.setlocale(locale.LC_ALL, "uk_UA")
print(locale.getlocale()) #get current locale
print(now.strftime('%c'))#output date+time in locale format

locale.setlocale(locale.LC_ALL, 'ja_JP')
print(locale.getlocale())
print(now.strftime('%c'))

locale.setlocale(locale.LC_ALL, 'en_us')
print(locale.getlocale())
print(now.strftime('%c'))
