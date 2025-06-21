import datetime

from sqlalchemy import Date, Integer, String, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column


class Database(MappedAsDataclass,DeclarativeBase):
    pass

class Usuário(Database):
    __tablename__ = 'usuario'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    nome:Mapped[str] = mapped_column(String,nullable=False)
    sobrenome:Mapped[str]=mapped_column(String,nullable=False)
    data_de_nascimento:Mapped[datetime.date] = mapped_column(Date,nullable=False)
    endereço:Mapped[str] = mapped_column(String,nullable=False)
    sexo:Mapped[str] = mapped_column(String(1),nullable=False)
    numero_de_telefone:Mapped[str] = mapped_column(String(15),nullable=False)
    email:Mapped[str]= mapped_column(String,nullable=False) 
    senha:Mapped[str]= mapped_column(String,nullable=False)
    
    __table_args__ = (
        UniqueConstraint('nome', 'sobrenome', 'numero_de_telefone', 
                        name='unicidade_nome_sobrenome_telefone'),
    )

