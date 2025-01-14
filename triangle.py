def area(a, h):
    """
         Функция "площадь треугольника"
         На вход : число (а),(h) (длина стророны и высоты квадрата) .
         (a)  является стороной квадрата
         (h) является высотой,проведенно к стороне (а)
         Функция возвращает a*h*(0.5),что яляется площадью треугольника .

         >>>area(4,3)
         6

         >>>area(0.5,0.8)
         0.2
    """
    return a * h / 2 

def perimeter(a, b, c):
    """
         Функция "периметр  треугольника"
         На вход : число (а),(b),(c) (длина стророн треугольника) .
         (a),(b),(c)  являются сторонами квадрата
         Функция возвращает a+b+c,что яляется периметром треугольника .

         >>>perimeter(2,3,4)
         9

         >>>perimeter(0.5,1.15,1,2)
         2.85
     """
    return a + b + c 
