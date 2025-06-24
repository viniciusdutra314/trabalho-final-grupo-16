from schemes.administracao import *


class Sala(Database):
    __tablename__ = "sala"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    unidade_escola: Mapped[str] = mapped_column(
        Integer,ForeignKey(UnidadeEscola.id_unidade)
    )
    numero:Mapped[int]=mapped_column(Integer)
    capacidade:Mapped[int]=mapped_column(Integer,nullable=False)
    __table_args__=(
        UniqueConstraint(
            "unidade_escola",
            "numero",
        ),
    )

class Curso(Database):
    __tablename__="curso"    
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    unidade_escola:Mapped[str] = mapped_column(
        Integer, ForeignKey(UnidadeEscola.id_unidade), 
        nullable=False)
    
    codigo:Mapped[str] = mapped_column((String),nullable=False)
    nome:Mapped[str] = mapped_column((String),nullable=False)
    departamento_academico:Mapped[int] = mapped_column(
        Integer, ForeignKey(DepartamentoAcademico.codigo), nullable=False
    )

    class NivelEnsinoEnum(enum.Enum):
        Fundamental = "Fundamental"
        Medio = "Médio"
        Tecnico = "Técnico"
        Graduacao = "Graduação"

    nivel_ensino:Mapped[NivelEnsinoEnum] = mapped_column(
        Enum(NivelEnsinoEnum), nullable=False
    )
    carga_horaria_total:Mapped[int] = mapped_column(Integer, nullable=False)
    numero_vagas:Mapped[int] = mapped_column(Integer, nullable=False)
    ementa:Mapped[str] = mapped_column(String)
    sala: Mapped[int] = mapped_column(
        Integer, ForeignKey(Sala.id),nullable=True
    )


class Disciplina(Database):
    __tablename__ = "disciplina"
    unidade_escola:Mapped[str] = mapped_column(
        Integer, ForeignKey(UnidadeEscola.id_unidade),
        nullable=False
    )
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    qtd_aulas_semanais:Mapped[int]=mapped_column(Integer,nullable=False)
    material_didatico_basico:Mapped[str]=mapped_column(String,nullable=False)
    sala : Mapped[int] = mapped_column(
        Integer, ForeignKey(Sala.id), nullable=True
    )

class CursoRequisitos(Database):
    __tablename__ = "curso_requisitos"
    id_curso:Mapped[Integer] = mapped_column(
        Integer, ForeignKey(Curso.id), primary_key=True
    )
    id_curso_requisito:Mapped[Integer] = mapped_column(
        Integer, ForeignKey(Curso.id), primary_key=True
    )

class CursoDisciplinaRequerida(Database):
    __tablename__ = "curso_disciplina_requerida"
    id_curso:Mapped[Integer] = mapped_column(
        Integer, ForeignKey(Curso.id), primary_key=True
    )
    id_disciplina:Mapped[int] = mapped_column(
        Integer, ForeignKey(Disciplina.id), primary_key=True
    )


class Regras(Database):
    __tablename__="regras"
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    descricao:Mapped[str] = mapped_column(String, nullable=False)

class RegrasCurso(Database):
    __tablename__ = "regras_curso"
    id_regra:Mapped[int] = mapped_column(
        Integer, ForeignKey(Regras.id), primary_key=True
    )
    codigo_curso:Mapped[int] = mapped_column(
        Integer, ForeignKey(Curso.id), primary_key=True
    )

class Infraestrutura(Database):
    __tablename__ = "infraestrutura"
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    descricao:Mapped[str] = mapped_column(String, nullable=False)

class CursoRequerInfraestrutura(Database):
    __tablename__ = "curso_requer_infraestrutura"
    id_curso:Mapped[int] = mapped_column(
        Integer, ForeignKey(Curso.id), primary_key=True
    )
    id_infraestrutura:Mapped[int] = mapped_column(
        Integer, ForeignKey(Infraestrutura.id), primary_key=True
    )


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
    ##isso deve ser usado por um trigger de verificação
    class TiposUsuarioEnum(enum.Enum):
        Aluno = "Aluno"
        Professor = "Professor"
        FuncionarioAdministrativo = "Funcionário Administrativo"

    tipo_usuario: Mapped[TiposUsuarioEnum] = mapped_column(
        Enum(TiposUsuarioEnum), nullable=False
    )
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
    unidade_escola: Mapped[str] = mapped_column(
        Integer, ForeignKey(UnidadeEscola.id_unidade), nullable=False
    )


class Professor(Database):
    __tablename__ = "professor"
    id: Mapped[int] = mapped_column(
        Integer, ForeignKey(Usuário.id), primary_key=True
    )
    area_especializacao:Mapped[str] = mapped_column(String,nullable=False)
    titulacao:Mapped[str] = mapped_column(String,nullable=False)
    unidade_escola: Mapped[str] = mapped_column(
        Integer, ForeignKey(UnidadeEscola.id_unidade), nullable=False
    )

class DisciplinaProfessoresResponsaveis(Database):
    __tablename__ = "disciplina_professor"
    id_disciplina:Mapped[int] = mapped_column(
        Integer, ForeignKey(Disciplina.id), primary_key=True
    )
    professor_id:Mapped[int] = mapped_column(
        Integer, ForeignKey(Professor.id), primary_key=True
    )




class Turma(Database):
    __tablename__="turma"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    id_disciplina:Mapped[int]=mapped_column(Integer,ForeignKey(Disciplina.id))
    capacidade:Mapped[int]=mapped_column(Integer,nullable=False)
    periodo_letivo:Mapped[str]=mapped_column(String,nullable=False)
    sala_id:Mapped[int]=mapped_column(Integer,ForeignKey(Sala.id))


class Avaliação(Database):
    __tablename__ = "avaliacao"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    aluno_id:Mapped[int]=mapped_column(Integer,ForeignKey(Aluno.usuario_id))
    disciplina_id:Mapped[int]=mapped_column(Integer,ForeignKey(Disciplina.id))
    comentario:Mapped[str]=mapped_column(String,nullable=False)
    nota_didatica:Mapped[int]=mapped_column(Integer,nullable=False)
    nota_material_de_apoio:Mapped[int]=mapped_column(Integer,nullable=False)
    nota_relevancia_do_conteudo:Mapped[int]=mapped_column(Integer,nullable=False)
    nota_infraestutura:Mapped[int]=mapped_column(Integer,nullable=False)

class Matricula(Database):
    __tablename__ = "matricula"
    id_matricula:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    id_aluno:Mapped[int]=mapped_column(Integer,ForeignKey(Aluno.usuario_id),nullable=False)
    data_efetivacao:Mapped[datetime.date]=mapped_column(Date,nullable=False)
    
    class StatusMatriculaEnum(enum.Enum):
        Ativa = "Ativa"
        Trancada = "Trancada"
        Concluida = "Concluída"
        Reprovada = "Reprovada"
        Cancelada = "Cancelada"
    
    status_matricula:Mapped[StatusMatriculaEnum]=mapped_column(Enum(StatusMatriculaEnum),nullable=False)
    bolsa_ou_desconto:Mapped[float]=mapped_column(Float,nullable=False)
    data_limite:Mapped[datetime.date]=mapped_column(Date,nullable=False)
    

class MatriculaTurma(Database):
    __tablename__ = "matricula_turma"
    id_matricula:Mapped[int]=mapped_column(Integer,ForeignKey(Matricula.id_matricula),primary_key=True)
    id_disciplina:Mapped[int]=mapped_column(Integer,ForeignKey(Disciplina.id),primary_key=True)

class Notas(Database):
    __tablename__ = "notas"
    disciplina_id:Mapped[int]=mapped_column(Integer,ForeignKey(Disciplina.id),primary_key=True)
    matricula_id:Mapped[int]=mapped_column(Integer,ForeignKey(Matricula.id_matricula),primary_key=True)
    nota:Mapped[float]=mapped_column(Float)
