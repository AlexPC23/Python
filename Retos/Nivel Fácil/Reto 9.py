#Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no
Year = int(input("Introduce un año: "))  
if (Year % 4) == 0:  
   if (Year % 100) == 0:  
       if (Year % 400) == 0:  
           print("{0} es un año bisiesto".format(Year))  
       else:  
           print("{0} no es un año bisiesto".format(Year))  
   else:  
       print("{0} es un año bisiesto".format(Year))  
else:  
   print("{0} no es un año bisiesto".format(Year))
