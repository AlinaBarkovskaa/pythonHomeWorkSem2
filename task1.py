# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#  Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
#  были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
#  5 -> 1 0 1 1 0

coins = int(input('Введите кол-во мoнет: '))
list_orel = []
list_reshka = []
count_orel=0
count_reshka=0
for i in range(coins):
    index = int(input('Введите 0 или 1: ' ))
    if(index == 1):
        list_orel.append(index) 
    elif(index==0):
        list_reshka.append(index)
    else:
        print(input('Вы ввели неверное значение: '))     
if(len(list_orel)> len(list_reshka)):
    count_reshka=len(list_reshka)
    print(count_reshka)
elif(len(list_orel)< len(list_reshka)):
    count_orel=len(list_orel)
    print(count_orel)
else:
    count_orel=len(list_orel)
    print(count_orel)





