import datetime
import enum

from sqlalchemy import Date, Float, Integer, String, UniqueConstraint, ForeignKey,Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column

class Database(MappedAsDataclass, DeclarativeBase):
    pass

class UnidadeEscola(Database):
    __tablename__ = "unidade_escola"
    id_unidade:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cidade:Mapped[str] = mapped_column(String, nullable=False)
    estado:Mapped[str] =  mapped_column(String, nullable=False)
    pais:Mapped[str] =  mapped_column(String, nullable=False)
    predio:Mapped[str]=  mapped_column(String, nullable=False)
    bloco:Mapped[str] =  mapped_column(String, nullable=False)

class DepartamentoAcademico(Database):
    __tablename__ = "departamento_academico"
    codigo:Mapped[int] = mapped_column(Integer,
                           primary_key=True,autoincrement=True)
    nome:Mapped[str] = mapped_column(String, 
                                     nullable=False)


class FuncionarioAdministrativo(Database):
    __tablename__ = "funcionario_administrativo"
    usuario_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("usuario.id"), primary_key=True
    )