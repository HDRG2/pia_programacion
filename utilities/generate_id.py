import random
import string


#actualmente esta funcion es la que funciona, ya que todos los id son NUMBER de 4 digitos
def generate_id():
    #esto genera un numero random de 5 digitos
    new_id = random.randint(1000,9999)
    return new_id

#la mejor opcion seria que el id sea una cadena de texto
def generate_id_best_option():
    longitud = 5
    #esto genera una cadena de 5 digitos y letras
    cadena_aleatoria = ''.join(random.choices(string.ascii_letters + string.digits, k=longitud))
    print(cadena_aleatoria)

