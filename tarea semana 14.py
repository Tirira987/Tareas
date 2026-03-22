#Calcular promedio de 3 notas
# 1 Función
def calcular_promedio(nota1, nota2, nota3):      
    promedio =(nota1 + nota2 + nota3) / 3

 # 2 Uso de return  
    return promedio                                                        
print ("-"*20,"Bienvenido","-"*20) 
print ("Ingrese las notas")                         
   
# 3 Ingreso de datos
n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))

if 0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10:
   
# 4 Llamada de la función
   resultado = calcular_promedio(n1,n2,n3)
   
# 5 Mostrar el resultado
   print ("El promedio es",resultado)
else:
    print ("Error: Datos no validos")
print ("Gracias")