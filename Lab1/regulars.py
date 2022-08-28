import re
# 1
s = "Розробити скрипт, який рахує кількість слів у введеному тексті."
res = re.findall(r"\b\w+", s)
word = len(res)
print(res)
print("there are " + str(word) + " words in text")

#2 Розробити скрипт, який буде отримувати номер авто та визначати валідність номеру та регіон реєстрації. Номера, що можуть бути введені відповідають поточному українському законодавству (лише стандартні номери, номери на замовлення не використовуємо). Використайте лише 3 регіони реєстрації України.
s = "fhsdgfsdgfhsdfg AA1234AB jgsdhfgshggdf AE4536GH dgfhsdgfh AH6789HB"
res = re.findall(r"\b[A-Z]{2}\d{4}[A-Z]{2}",s)
print(res)
region = dict{'AA':'Kyiv', 'AE':'Dnipropetrivsk obl', 'AH':'Donetsk'}
for x in res:
    reg = re.search(r"\w{2}")
    print(region.get(reg))