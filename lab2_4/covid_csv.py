from datetime import datetime
import csv
# https://github.com/owid/covid-19-data/tree/master/public/data
#1. Яка загальна кількість хворих зафіксовано на Філіппінах на 30.08.2020?
#2. Коли був зафіксований найбільший приріст хворих за тиждень в Україні?
#3. Порахуйте, чи відповідають дані по загальній кількості випадків за 21.08.2020 по світу сумі випадків по країнах за цю дату?
#4. Запишіть в текстовий файл найбільший показник по випадкам по кожній з країн. Н-д: Ukraine =)
file = open("owid-covid-data.csv", "r")
csv_reader = csv.reader(file)
print(max_weekly_icu_admissions)
i = 0
for row in csv_reader:
    print(row[0], '\t', row[5])
    i += 1
    print(i)

# dict_reader = csv.DictReader(file)
# ukr_date = []
# ukr_total_cases = []
# week_increase = []
# sum_21_08_2020 = 0
# country_cases = {}
# for row in dict_reader:
#     if row.get('date') == '2020-08-30' and row.get('location') == 'Philippines':
#          print('2020-08-30 on Philippines:'+row.get('total_cases'))