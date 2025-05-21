
from sqlalchemy.orm import Session
from persistence.database import SessionLocal
from business_logic.atm import ATM
import getpass


def main():
    session: Session = SessionLocal()
    atm = ATM()

    print("=== Bienvenido al Cajero Automático ===")
    while True:
        numero = input("Ingrese número de tarjeta (16 dígitos): ").replace(" ", "").replace("-", "")
        if len(numero) == 16 and numero.isdigit():
            break
        else:
            print("❌ Número de tarjeta inválido. Debe contener exactamente 16 dígitos numéricos.")

# Validar NIP (4 dígitos ocultos)
    while True:
        nip = getpass.getpass("Ingrese su NIP (4 dígitos): ")
        if len(nip) == 4 and nip.isdigit():
            break
        else:
            print("❌ NIP inválido. Debe contener exactamente 4 dígitos numéricos.")

    tarjeta, mensaje = atm.autenticar(session, numero, nip)
    print(mensaje)

    if not tarjeta:
        return

    cuenta = tarjeta.cuenta

    while True:
        print("\n--- Menú ---")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Ver últimas transacciones")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(atm.consultar_saldo(cuenta))

        elif opcion == "2":
            try:
                monto = float(input("Monto a depositar: "))
                print(atm.depositar(session, cuenta, monto))
            except ValueError:
                print("❌ Monto inválido.")

        elif opcion == "3":
            try:
                monto = float(input("Monto a retirar: "))
                print(atm.retirar(session, cuenta, monto))
            except ValueError:
                print("❌ Monto inválido.")

        elif opcion == "4":
            print("🧾 Últimas transacciones:")
            for t in atm.ver_transacciones(session, cuenta):
                print(t)

        elif opcion == "0":
            print("👋 Gracias por usar el cajero.")
            break
        else:
            print("❌ Opción inválida.")

    session.close()

if __name__ == "__main__":
    main()

