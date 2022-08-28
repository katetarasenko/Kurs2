import re
# 1
s = "Розробити скрипт, який рахує кількість слів у введеному тексті."
res = re.findall(r"\b\w+", s)
word = len(res)
print(res)
print("there are " + str(word) + " words in text")

#2 Розробити скрипт, який буде отримувати номер авто та визначати валідність номеру та регіон реєстрації. Номера, що можуть бути введені відповідають поточному українському законодавству (лише стандартні номери, номери на замовлення не використовуємо). Використайте лише 3 регіони реєстрації України.
"""
s = "fhsdgfsdgfhsdfg AA1234AB jgsdhfgshggdf AE4536GH dgfhsdgfh AH6789HB"
res = re.findall(r"\b[A-Z]{2}\d{4}[A-Z]{2}",s)
print(res)
region = {'AA':'Kyiv', 'AE':'Dnipropetrivsk obl', 'AH':'Donetsk'}

for x in res:
    rr = str(x[0]+x[1])
    #reg = re.findall(r"\b\w{2}", x)l
    print(str(x) + " " +region.get(rr))
"""

region = {'AA':'Kyiv', 'AE':'Dnipropetrivsk obl', 'AH':'Donetsk'}
#s = "fhsdgfsdgfhsdfg AA1234AB jgsdhfgshggdf AE4536GH dgfhsdgfh AH6789HB"
s = "BA1234AB"

pattern = r"\b[A-Z]{2}\d{4}[A-Z]{2}\b"
res = re.findall(pattern, s)
if res:
    autonumber = res[0]
    first2 = autonumber[0]+autonumber[1]
    reg = region.get(first2)
    if reg:
        print(autonumber + " " + reg)
    else:
        print(first2 + " Not region exist")
else:
    print(s + " Not valid number")


s = "serg@mail.ru se_re@serg.ru"
pattern = r"((?:[a-z0-9!#$%&'*+=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\]))"
res = re.findall(pattern, s)
if res:
    print(res)