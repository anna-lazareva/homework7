"""
Это приложение разбирает строку "bla-bla-bla" из file.txt на отдельные слова,
создавая список из этих слов. Затем вычисляет длину этого списка, и помещает результат
количества слов в файл output.txt.
"""

# Открыть и записать в файл.
with open("file.txt", "w") as f:
    f.write("bla-bla-bla")

# Чтение данных из файла.
with open('file.txt', 'r') as f:
    data = f.read().strip()

# Обработка данных
result = len(data.split('-'))

# Запись результата в файл.
with open('output.txt', 'w') as f:
    f.write(str(result))
    