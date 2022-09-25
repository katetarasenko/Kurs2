from datetime import datetime
import csv
# https://github.com/owid/covid-19-data/tree/master/public/data
#1. Яка загальна кількість хворих зафіксовано на Філіппінах на 30.08.2020?
#2. Коли був зафіксований найбільший приріст хворих за тиждень в Україні?
#3. Порахуйте, чи відповідають дані по загальній кількості випадків за 21.08.2020 по світу сумі випадків по країнах за цю дату?
#4. Запишіть в текстовий файл найбільший показник по випадкам по кожній з країн. Н-д: Ukraine =)
file = open("owid-covid-data.csv", "r")
# csv_reader = csv.reader(file)
# i = 0
# for row in csv_reader:
#     print(row[0], '\t', row[5])
#     i += 1
# print(i)

dict_reader = csv.DictReader(file)
ukr_date = []
ukr_total_cases = []
week_increase = []
sum_21_08_2020 = 0
country_cases = {}
countries = {}
for row in dict_reader:
    iso_code = row.get('iso_code')
    location = row.get('location')
    if row.get('date') == '2020-08-30' and location == 'Philippines':
         print('2020-08-30 on Philippines:'+row.get('total_cases'))
    if row.get('iso_code') == 'UKR':
        ukr_date.append(row.get('date'))
        ukr_total_cases.append(int(float(row.get('total_cases'))))
        #print(row.get('total_cases'))
#print(ukr_total_cases)
    if row.get('date') == '2020-08-21' and row.get('total_cases') != '':
        if iso_code.find('OWID') == -1:
            sum_21_08_2020 = sum_21_08_2020 + int(float(row.get("total_cases")))
        if iso_code == "OWID_WRL":
            world = int(float(row.get("total_cases")))
    if row.get('new_cases') != '':
        case = int(float(row.get("new_cases")))
        if location in countries.keys():
            if case > countries.get(location):
                countries.update({location : case})
        else:
            countries.update({location : case})

for i in  range(0,len(ukr_total_cases)-7):
    week_increase.append(ukr_total_cases[i+7] - ukr_total_cases[i])
    #print(ukr_total_cases[i+7] - ukr_total_cases[i])
#print(week_increase)
x = week_increase.index(max(week_increase))
print('maximal increase of covid infection:'+ str(max(week_increase)) + 'in 7 days period from '+ ukr_date[x] +'-'+ukr_date[x+6])
print("counted total covid cases: "+ str(sum_21_08_2020))
print('cunted cases in table:'+str(world))
file = open("countries_statistics.txt", "w")
for i in countries:
    #print(i + "="+str(countries.get(i)), file)
    file.write(i + "="+str(countries.get(i))+"\n")