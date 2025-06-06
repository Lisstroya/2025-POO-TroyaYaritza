class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0 :
            self._saldo +=monto
    def retirar(self, monto):
        if 0 < monto <= self ._saldo:
            self._saldo -= monto

    def mostrar_saldo(self):
        print(f"saldo actual: $ {self._saldo}")

cuenta = CuentaBancaria (500)
cuenta.depositar (100)
cuenta.retirar (80)
cuenta.mostrar_saldo()

