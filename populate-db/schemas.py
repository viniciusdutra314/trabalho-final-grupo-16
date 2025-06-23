import datetime
import enum

from sqlalchemy import Date, Integer, String, UniqueConstraint, ForeignKey,Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column

# enumerações usadas

class NivelEnsinoEnum(enum.Enum):
    Fundamental = "Fundamental"
    Medio = "Médio"
    Tecnico = "Técnico"
    Graduacao = "Graduação"


class StatusMatriculaEnum(enum.Enum):
    Ativa = "Ativa"
    Trancada = "Trancada"
    Concluida = "Concluída"
    Reprovada = "Reprovada"
    Cancelada = "Cancelada"


##relações propriamente ditas


class Database(MappedAsDataclass, DeclarativeBase):
    pass


class Usuário(Database):
    __tablename__ = "usuario"
    id: Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    sobrenome: Mapped[str] = mapped_column(String, nullable=False)
    data_de_nascimento: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    endereço: Mapped[str] = mapped_column(String, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    numero_de_telefone: Mapped[str] = mapped_column(String(15), nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    senha: Mapped[str] = mapped_column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "nome",
            "sobrenome",
            "numero_de_telefone",
            name="unicidade_nome_sobrenome_telefone",
        ),
    )


class Aluno(Database):
    __tablename__ = "aluno"
    usuario_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Usuário.id), primary_key=True
    )


class Professor(Database):
    __tablename__ = "professor"
    usuario_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Usuário.id), primary_key=True
    )
    area_especializacao:Mapped[str] = mapped_column(String)
    titulacao:Mapped[str] = mapped_column(String)



class FuncionarioAdministrativo(Database):
    __tablename__ = "funcionario_administrativo"
    usuario_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Usuário.id), primary_key=True
    )



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


class Sala(Database):
    __tablename__ = "sala"
    unidade_escola: Mapped[str] = mapped_column(
        Integer,ForeignKey(UnidadeEscola.id_unidade)
    )
    numero:Mapped[int]=mapped_column(Integer,primary_key=True)
    capacidade:Mapped[int]=mapped_column(Integer,nullable=False)


class Disciplina(Database):
    __tablename__ = "disciplina"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    qtd_aulas_semanais:Mapped[int]=mapped_column(Integer,nullable=False)
    material_didatico_basico:Mapped[str]=mapped_column(String,nullable=False)


class Matricula(Database):
    __tablename__ = "matricula"
    id_matricula:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    id_disciplina:Mapped[int]=mapped_column(Integer,ForeignKey(Disciplina.id))
    id_aluno:Mapped[int]=mapped_column(Integer,ForeignKey(Aluno.usuario_id))
    status_matricula:Mapped[StatusMatriculaEnum]=mapped_column(Enum(StatusMatriculaEnum),nullable=False)

