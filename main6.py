def z1():
    a = {
        'Россия': 'Москва',
        'Испания': 'Мадрид',
        'Польша': 'Варшава',
        'Китай': 'Пекин',
        'Турция': 'Анкара'
    }

    print("Пары:")
    for strn, stl in a.items():
        print(strn, "-", stl)

    strn = input("Введите название страны: ")
    if strn in a:
        print("Столица страны ", strn, ":", a.get(strn))
    else:
        print("Такой страны нет в словаре.")

    s = sorted(a.keys())
    print("В алфавитном порядке по стране:")
    for key in s:
        print(key, "-", a[key])

def z2():
    a = {
        'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
        'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
        'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
        'Й': 4, 'Ы': 4,
        'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
        'Ш': 8, 'Э': 8, 'Ю': 8,
        'Ф': 10, 'Щ': 10, 'Ъ': 10
    }

    b = input("Введите слово: ").upper()
    s = sum(a.get(i) for i in b)
    print("Стоимость слова: ", s)
