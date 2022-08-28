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
region = {'AA':'Kyiv', 'AE':'Dnipropetrivsk obl', 'AH':'Donetsk'}

#matches = re.finditer(r"\b\w{2}", s)
#for matchNum, match in enumerate(matches, start=1):
#    print(match)

for x in res:
    rr = str(x[0]+x[1])
    #reg = re.findall(r"\b\w{2}", x)
    print(str(x)+region.get(rr))
