import math
try:
   n = int(input())
   if n < 0:
       print("Vui long nhap so tu nhien!")
   elif n < 2:
       print("{} khong la so nguyen to!".format(n))
   else:
       for i in range(2, int(math.sqrt(n))+1):
           if n % i == 0:
               print("{} khong la so nguyen to!".format(n))
               break
       else:
           print("{} la so nguyen to!".format(n))
except:
   print("Dinh dang dau vao khong hop le!")
