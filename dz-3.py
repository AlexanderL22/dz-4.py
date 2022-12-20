# В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4



def change_spisok(spisok: list[str], accept: str) -> str:
    file_spisok = ''
    for name in spisok:
        if name.count(accept):
            name = name.upper()
        string = name +'\n'
        file_spisok += string     
    return file_spisok

file_spisok = open('bal.txt', 'r', encoding='utf-8')
lines_spisok = file_spisok.read().split('\n')
file_spisok.close()

spisok_new = change_spisok(lines_spisok, accept='5')

file_spisok = open('bal.txt', 'w', encoding='utf-8')
file_spisok.write(spisok_new)
file_spisok.close()