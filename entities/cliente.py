
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from persistence.database import Base


class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    
    cuentas = relationship("Cuenta", back_populates="cliente")
    
