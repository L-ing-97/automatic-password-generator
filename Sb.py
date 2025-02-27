# Sistema Bancario Interactivo
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.historial = []

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            self.historial.append(f"Depósito: +${monto}")
            print(f"✅ Depósito exitoso. Nuevo saldo: ${self.saldo}")
        else:
            print("⚠️ El monto debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            self.historial.append(f"Retiro: -${monto}")
            print(f"✅ Retiro exitoso. Nuevo saldo: ${self.saldo}")
        else:
            print("❌ Fondos insuficientes o monto inválido.")

    def transferir(self, monto, otra_cuenta):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            otra_cuenta.saldo += monto
            self.historial.append(f"Transferencia enviada: -${monto} a {otra_cuenta.titular}")
            otra_cuenta.historial.append(f"Transferencia recibida: +${monto} de {self.titular}")
            print(f"✅ Transferencia de ${monto} a {otra_cuenta.titular} completada.")
        else:
            print("❌ Fondos insuficientes o monto inválido.")

    def ver_saldo(self):
        print(f"💰 Saldo actual de {self.titular}: ${self.saldo}")

    def ver_historial(self):
        print(f"📜 Historial de {self.titular}:")
        for transaccion in self.historial:
            print(f"  - {transaccion}")
        if not self.historial:
            print("🔹 Sin transacciones.")

# 🚀 Función principal con menú interactivo
def iniciar_sistema():
    print("🏦 Bienvenido al Sistema Bancario")
    
    # Crear cuentas de prueba
    cuenta1 = CuentaBancaria("Usuario 1", 1000)
    cuenta2 = CuentaBancaria("Usuario 2", 500)

    cuentas = {"1": cuenta1, "2": cuenta2}

    while True:
        print("\n📌 Menú Principal:")
        print("1️⃣ Depositar dinero")
        print("2️⃣ Retirar dinero")
        print("3️⃣ Transferir dinero")
        print("4️⃣ Ver saldo")
        print("5️⃣ Ver historial de transacciones")
        print("6️⃣ Salir")

        opcion = input("🔹 Elige una opción: ")

        if opcion == "1":
            cuenta = input("🔹 ¿En qué cuenta? (1/2): ")
            if cuenta in cuentas:
                monto = float(input("💰 Ingresa el monto a depositar: "))
                cuentas[cuenta].depositar(monto)
            else:
                print("⚠️ Cuenta no encontrada.")

        elif opcion == "2":
            cuenta = input("🔹 ¿Desde qué cuenta? (1/2): ")
            if cuenta in cuentas:
                monto = float(input("🏧 Ingresa el monto a retirar: "))
                cuentas[cuenta].retirar(monto)
            else:
                print("⚠️ Cuenta no encontrada.")

        elif opcion == "3":
            desde = input("🔹 ¿Desde qué cuenta? (1/2): ")
            hacia = input("🔹 ¿A qué cuenta? (1/2): ")
            if desde in cuentas and hacia in cuentas:
                monto = float(input("💳 Ingresa el monto a transferir: "))
                cuentas[desde].transferir(monto, cuentas[hacia])
            else:
                print("⚠️ Una de las cuentas no existe.")

        elif opcion == "4":
            cuenta = input("🔹 ¿De qué cuenta? (1/2): ")
            if cuenta in cuentas:
                cuentas[cuenta].ver_saldo()
            else:
                print("⚠️ Cuenta no encontrada.")

        elif opcion == "5":
            cuenta = input("🔹 ¿De qué cuenta? (1/2): ")
            if cuenta in cuentas:
                cuentas[cuenta].ver_historial()
            else:
                print("⚠️ Cuenta no encontrada.")

        elif opcion == "6":
            print("👋 ¡Gracias por usar el sistema bancario!")
            break

        else:
            print("❌ Opción inválida. Intenta de nuevo.")

# Ejecutar el sistema
iniciar_sistema()
