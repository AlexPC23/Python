#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
peso_payaso = 0.112
peso_muñeca = 0.75
payasos_vendidos = int(input("¿Cuantos payasos se han vendido?"))
muñecas_vendidas = int(input("¿Cuantos muñecas se han vendido?"))
peso_total = print("El peso es de " + (str((payasos_vendidos * peso_payaso) + (muñecas_vendidas * peso_muñeca))))