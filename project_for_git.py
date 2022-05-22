'''
Вариант 12

Максимальный элемент каждой строки массива

'''

from random import random
from numpy import max as np_max
from numpy import array as arr
from numpy import loadtxt
import time

#формируем массив из 50 матриц со случайными элементами
#и сразу записываем их в файлы

for k in range(0, 50):
    f = open("D:/рабочий стол/4сем/проект/project/matrix"+str(k), 'w')
    for i in range(0, 100):
        for j in range(0, 100):
            f.write(str(200*random()-100))
            f.write(',') if j!=99 else None
        f.write('\n')
    f.close()

#создаем файл для хранения времени выполнения
f = open("D:/рабочий стол/4сем/проект/project/p_time", 'w')
#создаем файл для хранения результата

for i in range(50):    

    start_time = time.time()        #начинаем отсчет времени

    f1 = open("D:/рабочий стол/4сем/проект/project/res_p"+str(i), 'w')      #открытие файла для записи найденного максимума
    b = loadtxt("D:/рабочий стол/4сем/проект/project/matrix" + str(i), delimiter=',')       #чтение матрицы
    f1.write(str(np_max(b, axis = 1)) + '\n')       #запись найденных максимумов
    f1.close()
    
    t = time.time()-start_time      #заканчиваем отсчет времени

    f.write(str(t))                 #записываем полученное число в файл
    f.write(',') if i!=49 else None
    
f.close()