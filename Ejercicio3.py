class CuentaBancaria:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0.00
    
    def depositar(self, monto: float):
        if monto > 0:
            self.saldo += monto 
            print("Deposito por la suma de: ", monto, " realizado") 
    
    def retiro(self, monto: float):
        if self.saldo >= monto:
            self.saldo -= monto
            print("Retiro por la suma de: ", monto, " realizado")
        else:
            print("Fondos insuficientes, Saldo actual:  ", self.saldo)

    def mostrarSaldo(self):
        print("Saldo actual: ", self.saldo)    

CuentaBancaria1 = CuentaBancaria("Daniel Giron")
CuentaBancaria1.mostrarSaldo()
CuentaBancaria1.depositar(1000)
CuentaBancaria1.mostrarSaldo()
CuentaBancaria1.retiro(500)
CuentaBancaria1.mostrarSaldo()
CuentaBancaria1.retiro(2000)
CuentaBancaria1.mostrarSaldo()

        