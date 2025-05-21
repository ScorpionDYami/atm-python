from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from persistence.database import Base


class Cuenta(Base):
    __tablename__ = 'cuenta'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    saldo = Column(Float, default=0.0)

    cliente = relationship("Cliente", back_populates="cuentas")
    tarjeta = relationship("Tarjeta", uselist=False, back_populates="cuenta")
    transacciones = relationship("Transaccion", back_populates="cuenta")