"""Tuplas, las tuplas son secuencias inmutables de objetos"""
def run():
    # Las tuplas son inmutables
    tupla = (1,"2",3.0)
    # Agregar una coma cuando es una tupla de un valor
    tupla_one_value = (5,)
    # Sumar tuplas
    tuple_join = tupla + tupla_one_value
    # desempaquetar tupla
    a, b, c = tupla
    # devolver una tupla con una funcion
    def coordenada():
        return (1,3)
    
    x, y = coordenada()


    print(f"""
            tupla \t\t-> {tupla}
            tupla_one_value \t-> {tupla_one_value}
            tuple_join \t\t-> {tuple_join}
            a, b, c \t\t-> {a} {b} {c}
            x, y \t\t-> {x} {y}
    """)


if __name__ == '__main__':
    run()
    
