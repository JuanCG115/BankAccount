class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('negro','Tucan')

print(f'Mi pajara es un {mi_pajaro.especie} de color {mi_pajaro.color}')

print(Pajaro.alas)
print(mi_pajaro.alas)