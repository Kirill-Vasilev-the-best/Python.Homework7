
# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках 
# не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм 
# есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из 
# одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все 
# в порядке и “Пам парам”, если с ритмом все не в порядке

def word(words):
    str = words.lower().split()
    l = lambda x: sum(1 for i in x if i in 'аоиеёэыуюя')
    spm = l(str[0])
    if all([l(i) == spm for i in str]):
        return 'Парам пам-пам'
    return 'Пам парам'

print(word("Если-конечно,-вовремя-подкрепиться - да"))


# print(word("Хорошо-живет-на-свете-Винни-Пух!")) то результат 'Парам пам-пам'
# print(word("Оттого-поет-он-эти-Песни-вслух!")) то результат 'Парам пам-пам'
# print(word("Если-конечно,-вовремя-подкрепиться - да")) то результат 'Пам парам'

