
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from persistence.database import Base


class Tarjeta(Base):
    __tablename__ = 'tarjeta'
    id = Column(Integer, primary_key=True)
    numero = Column(String, nullable=False)
    nip = Column(String, nullable=False)
    intentos_fallidos = Column(Integer, default=0)
    bloqueada = Column(Boolean, default=False)
    cuenta_id = Column(Integer, ForeignKey('cuenta.id'))

    cuenta = relationship("Cuenta", back_populates="tarjeta")