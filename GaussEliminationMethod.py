import numpy as np

def Elimination(n, a, b):
    for k in range(n-1): #итератор по строкам (для диагнональных элементов которых (которых - это строки)
      #будем занулять коэффициенты, расположенные ниже)
      #range(n-1), т.к. последняя строка не нужна - под ней ничего нет
      
      for i in range(k+1, n): #берем все строки, расположенные ниже текущей
            if a[i, k]==0: #если элемент под диагональным равен 0, то пропускаем
                continue
              
            #находим число, на которое надо умножить коэффициент, чтобы получить 0 под текущем диагнольным элементом
            factor = a[k, k] / a[i, k]
            for j in range(k, n):#итератор по столбцам (матрица квадратная), начиная от текущего диагонального элемента
            #a[i, j] - текущий элемент под и правее диагонального 
            #(левее вычислять смысла нет, так как там a[k, j]=0 с прошлых и позапрошлых итераций для всех j)
            
                a[i, j] = a[k, j] - a[i, j]*factor #зануление элементов
            b[i] = b[k] - b[i]*factor #для b столбец всего один
    print("a:")
    print(a)
    print("b:")
    print(b)
    return a, b
  
def Back_substitution(x, b, a, n):
    x[n-1] = b[n-1] / a[n-1, n-1] #находим x_n (решение уравнения a_n * x_n = b_n)
    for i in range(n-2, -1, -1): #начинаем движение от последнего уравнения к следующим
      #выполняя деление на диагональный коэффициент, т.к. все что правее него найдено на предыдущих шагах
      #все что левее него равно 0, значит этих переменных в уравнении не будет
        
        sum_ax = 0
        #по всем перемнным, по которым были найдены решения на предыдущих шагах находим текущий x_i
        for j in range(i+1, n):
            
            #пример решение уравнения a1*x1 + a2*x2 + a3*x3 = b1 => x1 = [b1 - (a2*x2 + a3*x3)] / a1
            sum_ax += a[i, j] * x[j]
            x[i] = (b[i] - sum_ax) / a[i, i] 
    print("Solution: x = ", x)
    return x
