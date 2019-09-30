import random
import string
import re

CHARS = string.ascii_letters + string.digits + "~!@#$%^&()_+="


def pwd_generator(strings_count=1):
    for i in range(0, strings_count):
        string_length = random.randint(0, 40) # Я специально увеличила длину пароля, чтобы было на чем проверять, как отрабатывает код
        yield str(''.join(random.choice(CHARS) for i in range(string_length)))

def check_pwd_length(text):
    if bool(len(text) > 5) is False:
        print ( "Invalid password  " + i + "  Password should contain at least 6 characters" ) # Task 2.1
        return False
    else:
        return True

def check_pwd_specsymbols(text):
    if bool(set("~!@#$%^&()_+=").intersection(text)) is False:
        print ( "Invalid password  " + i + "  Password should contain at least 1 special symbol" ) # Task 2.1
        return False
    else:
        return True

def check_pwd_digits(text):
    if bool(set(string.digits).intersection(text)) is False:
        print ( "Invalid password  " + i + "  Password should contain at least 1 digit" ) # Task 2.1
        return False
    else:
        return True

def check_pwd_alphabetic(text):
    if bool(''.join(set(string.ascii_letters).intersection(text))) is False:
        print ( "Invalid password  " + i + "  Password should contain letters" ) # Task 2.1
        return False
    else:
        return True

def check_pwd_uppercase(text):
    if bool(''.join(set(string.ascii_letters).intersection(text)).islower()) is True:
        print ( "Invalid password  " + i + "  Password should contain at least 1 letter in upper case" ) # Task 2.1
        return False
    else:
        return True

def check_pwd_lowercase(text):
    if bool(''.join(set(string.ascii_letters).intersection(text)).isupper()) is True:
        print ( "Invalid password  " + i + "  Password should contain at least 1 letter in lower case" ) # Task 2.1
        return False
    else:
        return True

# Задание 1(уровень - лёгкое) (Task 2.1)
# Надо вывести невалидные пароли в командную строку с причиной, где была найдена ошибка

# Уже было и так сделано в рамках самого первого задания по валидации пароля - причина выводится.

# Задание 2(дополнение к Заданию 1. Уровень - лёгкое) (Task 2.2):    
# 1. Длина пароля
def get_pwd_length(text): # Task 2.2 (1)
    print("Password length:  " + str(len(text)))


# 2. Кол-во букв верхнего регистра
# # 3. Кол-во букв нижнего регистра
# # 4. Кол-во спец символов
def get_pwd_content(args): # Task 2.2 (2-4)
    u = len(re.findall(r'[A-Z]', args))
    l = len(re.findall(r'[a-z]', args))
    s = len(re.findall(r'[~!@#$%^&()_+=]', args))
    print("Password contains:  " + str(u) + " letter(s) in upper case, " + str(l) + " letter(s) in lower case, " + str(s) + " special symbol(s).")


# Задание 3(дополнение к Заданию 2. Уровень - неоч изи уже) (Task 2.3):
# Если существует пароль, в котором встречается использование одной буквы более одного раза, то:
# 1. Вывести эту букву
# 2. Вывести позиции, в котором расположились элементы пароля одной буквы
# Заметка: Пока что, не обращаем внимание на регистры в этой задаче
def find_doubles(text): # Task 2.3
    p = list(text)
# Преобразуем пароль в множество, чтобы отсечь все дубликаты, оставляем только буквы и опять преобразуем ег в список:
    d = list(set(string.ascii_letters).intersection(str(set(text))))
    a = []
    b = {}
    for i in range(len(d)):
        for j in range(len(p)):
            if d[i] == p[j]:
                a.append(j)
        if len(a) > 1:
            b[d[i]] = a
        a = []
    if b != {}:
        print("Positions of duplicates: ")
        print(b)
    else:
        print("Password doesn't contain duplicates.")
    print("------------------------------------------------------------------------------------------------")

#-------------------------------------------------------------------------------------------

if __name__ == '__main__':

    for i in pwd_generator(10):
        if all((check_pwd_length(i), check_pwd_specsymbols(i), check_pwd_digits(i), check_pwd_alphabetic(i), check_pwd_uppercase(i), check_pwd_lowercase(i))) is True:
            print ( "------------------------------------------------------------------------------------------------" )
            print("Valid password: " + i) # Task 1
            get_pwd_length(i) # Task 2.2 (1)
            get_pwd_content(i) # Task 2.2 (2-4)
            find_doubles(i) # Task 2.3
            
#---------------------------------------------------------------------------------------------------------------------------------------
# Task 2:
# Задание 1(уровень - лёгкое) (Task 2.1)
# Надо вывести невалидные пароли в командную строку с причиной, где была найдена ошибка пароля
#
# Задание 2(дополнение к Заданию 1. Уровень - лёгкое) (Task 2.2)
# Правильные пароли надо вывести со следующей информацией:
# 1. Длина пароля
# 2. Кол-во букв верхнего регистра
# 3. Кол-во букв нижнего регистра
# 4. Кол-во спец символов
#
# Задание 3(дополнение к Заданию 2. Уровень - неоч изи уже) (Task 2.3)
# Если существует пароль, в котором встречается использование одной буквы более одного раза, то:
# 1. Вывести эту букву
# 2. Вывести позиции, в котором расположились элементы пароля одной буквы
# Заметка: Пока что, не обращаем внимание на регистры в этой задаче
