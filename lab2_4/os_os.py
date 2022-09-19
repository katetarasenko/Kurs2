import os

# Створіть функцію, яка буде зчитувати дані з одного типу файлу та зберігати їх у файлі іншого типу.
# Вона буде приймати 3 аргументи: шлях до файлу; змінну, яка буде визначати тип цього файлу;
# змінна, яка буде визначати тип файлу, у який потрібно зберегти дані.
# Функція буде працювати з файлами типу *.txt, *.csv, *.dat. Протестуйте роботу функції…

def rename_file(path, type1, type2):
    fullname = path+'.'+type1
    new_name = path+'.'+type2
    if os.path.exists(fullname):
        print("Renaming to ", new_name)
        os.rename(fullname, new_name)
    else:
        print("Path not exist")

rename_file('test', 'csv', 'txt')
rename_file('test', 'txt', 'csv')

# prjpath = os.getcwd()
# print(prjpath)
# newdir = prjpath + r"/dir3"
# norm = os.path.normpath(newdir)
# print(newdir)
# print(os.path.abspath(newdir))
# if os.path.exists(newdir):
#     print("Path already exist")
# else:
#     os.mkdir(newdir)
# os.mkdir("d:\dir1")
# p = r"d:\dir1\dir2"
# os.mkdir(p)

