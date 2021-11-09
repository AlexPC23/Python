#Haz uso de exec() para ejecutar ambas operaciones
miCodigo = 'print("Hola Mundo")'
otroCodigo = '''
  def multiplicar(x,y):
      return x*y
    print('Multiplica: 2 * 4: ',multiplicar(2,4))
  '''
exec(miCodigo)
exec(otroCodigo)