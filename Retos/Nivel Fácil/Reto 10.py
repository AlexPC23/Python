#Escribe un programa que almacene en una lista (Array) todos los nombres de los alumnos del curso Programación para No Programadores y los muestre en por pantalla.
pelicula: dict = dict({
    'título': 'El Más Allá',
    'aka': 'E tu vivrai nel terrore - L\'aldilà',
    'director': 'Lucio Fulci',
    'año': 1981,
    'país': 'Italia'
  })

print(f"- Nombre de la película {pelicula.get('título')}")
print(f"- AKA de la película {pelicula.get('aka')}")
print(f"- Director de la película {pelicula.get('director')}")
print(f"- Año de la película {pelicula.get('año')}")
print(f"- País de la película {pelicula.get('país')}")

