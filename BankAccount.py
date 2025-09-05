class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido} con numero de cuenta: {self.numero_cuenta} tiene un saldo de {self.balance}'

    def depositar(self,deposito):
        self.balance += deposito
        print('Deposito aceptado')

    def retirar(self,retiro):
        if self.balance >= retiro:
            self.balance -= retiro
            print('Retiro realizado')
        else:
            print('Fondos insuficientes')

def crear_cliente():
    nombre_cl = input('Ingrese su nombre: ')
    apellido_cl = input('Ingrese su apellido: ')
    num_cuenta = input('Ingrese su numero de cuenta: ')
    cliente = Cliente(nombre_cl,apellido_cl,num_cuenta)
    return cliente

def inicio():

    mi_cliente = crear_cliente()
    print(mi_cliente)

    opcion = 0

    while opcion !='S':
        print('Elige: Depositar(D), Retirar(R) o Salir(S)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input('Monto a depositar: '))
            mi_cliente.depositar(monto_dep)
            print(mi_cliente)
        elif opcion == 'R':
            monto_ret = int(input('Monto a retirar: '))
            mi_cliente.retirar(monto_ret)
            print(mi_cliente)
    print('Que tenga un buen dia!!!')

inicio()