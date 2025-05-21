
import bcrypt
from entities.tarjeta import Tarjeta
from entities.cuenta import Cuenta
from entities.transaccion import Transaccion
from sqlalchemy.orm import Session
from datetime import datetime

class ATM:

    def autenticar(self, session: Session, numero_tarjeta: str, nip_ingresado: str):
        tarjeta = session.query(Tarjeta).filter(Tarjeta.numero == numero_tarjeta).first()

        if not tarjeta:
            return None, "❌ Tarjeta no encontrada."

        if tarjeta.bloqueada:
            return None, "🔒 Tarjeta bloqueada. Contacte al banco."

        if bcrypt.checkpw(nip_ingresado.encode(), tarjeta.nip.encode()):
            tarjeta.intentos_fallidos = 0
            session.commit()
            return tarjeta, f"✅ Bienvenido, {tarjeta.cuenta.cliente.nombre}."
        else:
            tarjeta.intentos_fallidos += 1
            if tarjeta.intentos_fallidos >= 3:
                tarjeta.bloqueada = True
                session.commit()
                return None, "🔒 Tarjeta bloqueada tras 3 intentos fallidos."
            else:
                intentos_restantes = 3 - tarjeta.intentos_fallidos
                session.commit()
                return None, f"❌ NIP incorrecto. Intentos restantes: {intentos_restantes}"

    def consultar_saldo(self, cuenta: Cuenta):
        return f"💰 Saldo actual: ${cuenta.saldo:.2f}"

    def depositar(self, session: Session, cuenta: Cuenta, monto: float):
        cuenta.saldo += monto
        trans = Transaccion(tipo="DEPOSITO", monto=monto, cuenta=cuenta, fecha_hora=datetime.now())
        session.add(trans)
        session.commit()
        return f"✅ Depósito exitoso. Nuevo saldo: ${cuenta.saldo:.2f}"