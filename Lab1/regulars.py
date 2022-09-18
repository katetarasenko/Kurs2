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

for x in res:
    rr = str(x[0]+x[1])
    #reg = re.findall(r"\b\w{2}", x)l
    print(str(x) + " " +region.get(rr))


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


s = "serg@mail.com se_re@serg.com sgdfhgdfh@sgdfsg"
pattern = r"((?:[a-z0-9!#$%&'*+=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\]))"
res = re.findall(pattern, s)
if res:
    print(res)

s = "a2p333ad-23"
pattern = "[\w\d-]{8,15}"
res = re.findall(pattern, s)
if (res[0] == s):
    print("password OK")
else:
    print("password pattern incorrect")

s = "Розробіть скрипт, який буде порівнювати пароль, що вводить користувач з шаблоном, зашитим у коді. При цьому порівняння не повинно враховувати регістр, пробіли та всі інші розділові знаки, крім дефісу."
res = re.findall(r"\b\w+", s)
word = len(res)
print(res)
print("there are " + str(word) + " words in text")

# NASA UFO...
s = "numb, amber,simple,ape, e"
res = re.findall(r"\b\w+", s)
print(res)
text = ""
for x in res:
    text = text + x[0].upper()
print(text)

print(''.join(i.upper() for i in re.findall(r"\b\w{1}", s)))


#(?'slog'([^аеоіиєуюя]{0,}(?<=[^аеоіиєуюя])[аеоіиєуюя])|((?<=[аеоіиєуюя])[аеоіиєуюя])){5}[^\d]+[\/](?&slog){7}[^\d]+[\/](?&slog){5}[^\d][.!?\n]
verses=['Ще не померла! / Закінчується осінь, / Я йду за обрій.',
       'Ночую просто неба. / Виє пес. / Теж допекла, мабýть, осіння мряка!',
       'Вода замерзла, / Розколовши глечик. / І тріск раптовий розбудив мене.']
pattern = r"(?<=[^аеоіиєуюя])[аеоіиєуюя]|(?<=[аеоіиєуюя])[аеоіиєуюя]"
for verse in verses:
    print(verse)
    splitted = re.split("/", verse.lower())
    #print(splitted)
    cnt1 = len(re.findall(pattern, splitted[0]))
    #print(cnt1)
    cnt2 = len(re.findall(pattern, splitted[1]))
    #print(cnt2)
    cnt3 = len(re.findall(pattern, splitted[2]))
    #print(cnt3)
    if cnt1 == 5 & cnt2 == 7 & cnt3 == 5:
        print("Haiku")
    else:
        print("NOT Haiku"+" "+str(cnt1)+" "+str(cnt2)+" "+str(cnt3))

s = "Дуже      поширена помилка помилка - це лише      повторення повторення слова слова. Смішно, чи чи не так? Це - книга книгарні."
pattern = r'(\b\w+\s)\1'
print(s)
print(re.sub(pattern, r'\1', s))


badtext ='В        цьому\nреченні розриви рядків... Але це\nне так важливо! Зовсім? Так, зовсім! І це не повинно   заважати.'
s = re.sub(r'(\n)|(\s{2,})', ' ', badtext) #удалаем двойные пробелы или перенос строки на один пробел
print(s)

pattern = r"([^\s!.?]+[\w\s]+\.\.\.)|([^\s!.?]+[\w\s]+[.?!])"
matches = re.finditer(pattern, s, re.MULTILINE)
for match in matches:
    print(match.group())

s = "jsdj 21:34:59 sbga 23:45:50 !7dfhg dfh 15:34 add 27:55 sgsg "
pattern = r'\b(([01][\d])|([2][0123])):([012345][\d])(:([012345][\d])){0,1}\b'
matches = re.finditer(pattern, s, re.MULTILINE)
for match in matches:
    print(match.group())
s1 = re.sub(pattern, "(TBD)", s)
print(s1)

s = "abc"
pattern = r'.'
new = ""
matches = re.finditer(pattern, s, re.MULTILINE)
for match in matches:
    code = ord(match.group())
    new = new + str(code*code*code)
print(new)


s = "absdhghgfhsdgsdhgssh vgifg fkg ytty437 gyufg d"
for c in s:
    print((ord(c)^3))

