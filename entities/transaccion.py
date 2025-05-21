from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
import datetime
from sqlalchemy.orm import relationship
from persistence.database import Base


class Transaccion(Base):
    __tablename__ = 'transaccion'
    id = Column(Integer, primary_key=True)
    tipo = Column(String)
    monto = Column(Float)
    fecha_hora = Column(DateTime, default=datetime.datetime.now)
    cuenta_id = Column(Integer, ForeignKey('cuenta.id'))

    cuenta = relationship("Cuenta", back_populates="transacciones")