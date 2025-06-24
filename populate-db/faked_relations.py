from typing import List
from faker import Faker
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from schemes.administracao import *
from schemes.comunicacao import *
from schemes.ensino import *
import random

faker = Faker('pt_BR')

def fake_unidade_escola(N: int = 10) -> List[UnidadeEscola]:
    unidades_escola:List[UnidadeEscola] = []
    for i in range(N):

        unidades_escola.append(
            UnidadeEscola(id_unidade=i+1,
        cidade=faker.city(),
        estado=faker.estado_sigla(),
        pais='Brasil',
        predio=faker.word(),
        bloco=faker.random_letter()
        ))
    return unidades_escola

def fake_usuario(N: int = 20) -> List[Usuário]:
    usuarios:List[Usuário] = []
    for i in range(N):

        usuarios.append(Usuário(
        id=i+1,
        nome=faker.first_name(),
        sobrenome=faker.last_name(),
        data_de_nascimento=faker.date_of_birth(minimum_age=18, maximum_age=60),
        endereço=faker.address(),
        sexo=random.choice(['M', 'F']),
        numero_de_telefone=faker.phone_number(),
        email=faker.email(),
        senha=faker.password(length=16),
        tipo_usuario=random.choice([x.value for x in Usuário.TiposUsuarioEnum])))
    return usuarios

def fake_aluno(usuarios:list[Usuário]) -> List[Aluno]:
    usuarios_alunos  =filter(lambda x: x.tipo_usuario == Usuário.TiposUsuarioEnum.Aluno.value, usuarios)
    alunos:list[Aluno]=[]
    for usuario_aluno in usuarios_alunos:
        alunos.append(Aluno(usuario_id=usuario_aluno.id,
                            unidade_escola=str(random.randint(1, 10))))
    return alunos

def fake_professor(usuarios:list[Usuário]) -> List[Professor]:
    usuarios_professores  =filter(lambda x: x.tipo_usuario == Usuário.TiposUsuarioEnum.Professor.value,
                                   usuarios)
    professores:list[Professor]=[]
    for usuario_professor in usuarios_professores:
        professores.append(Professor(id=usuario_professor.id,
                            area_especializacao=faker.job(),
                            titulacao=faker.word(),
                            unidade_escola=str(random.randint(1, 10))))
    return professores

def fake_funcionario_administrativo(usuarios:list[Usuário]) -> List[FuncionarioAdministrativo]:
    usuarios_administrativos  =filter(lambda x: x.tipo_usuario == Usuário.TiposUsuarioEnum.FuncionarioAdministrativo.value,
                                   usuarios)
    administrativos:list[FuncionarioAdministrativo]=[]
    for administrativo in usuarios_administrativos:
        administrativos.append(FuncionarioAdministrativo(usuario_id=administrativo.id))
    return administrativos


def fake_departamento_academico(possiveis_chefes:list[Professor]) -> List[DepartamentoAcademico]:
    N=int(0.2*len(possiveis_chefes))
    random.shuffle(possiveis_chefes)
    chefes:list[Professor] = possiveis_chefes[:N]
    departamentos_academicos:list[DepartamentoAcademico] = []
    for id,chefe in enumerate(chefes):
        departamentos_academicos.append(DepartamentoAcademico(
            codigo=id+1,
            nome=faker.company(),
            chefe_id=chefe.id
        ))
    return departamentos_academicos




def fake_aviso(N: int = 10) -> List[Aviso]:
    return [Aviso(
        id=i+1,
        texto=faker.sentence(),
        timestamp_criacao=faker.date_time_this_year()
    ) for i in range(N)]

def fake_mensagem(N: int = 10) -> List[Mensagem]:
    return [Mensagem(
        id=i+1,
        remetente_id=random.randint(1, 20),
        timestamp_criacao=faker.date_time_this_year(),
        texto=faker.text()
    ) for i in range(N)]

def fake_mensagem_destinatario(mensagens:List[Mensagem]) -> List[MensagemDestinatario]:
    destinatarios:list[MensagemDestinatario]=[]
    for mensagem in mensagens:
        num_destinatarios = random.randint(1, 5)
        destinatarios_id=random.sample(range(1, 21), num_destinatarios)
        for id in destinatarios_id:
            destinatarios.append(MensagemDestinatario(
                mensagem_id=mensagem.id,
                destinatario_id=id))
    return destinatarios

def fake_sala(unidades_escolas:list[UnidadeEscola],N:int) -> List[Sala]:
    salas:list[Sala] = []
    id=0
    for _ in range(N):
        id+=1
        salas.append(Sala(
            id=id,
            unidade_escola=str(random.choice(unidades_escolas).id_unidade),
            numero=id,
            capacidade=faker.random_int(min=30, max=100)
            ))
    return salas
def fake_curso(unidade_escola:list[UnidadeEscola],
               departamentos_academicos:list[DepartamentoAcademico]) -> List[Curso]:
    return [Curso(
        id=i+1,
        unidade_escola=str(random.choice(unidade_escola).id_unidade),
        codigo=f"CURSO{i+1}",
        nome=faker.job(),
        departamento_academico=random.choice(departamentos_academicos).codigo,
        nivel_ensino=random.choice([x.value for x in Curso.NivelEnsinoEnum]),
        carga_horaria_total=faker.random_int(min=100, max=2000),
        numero_vagas=faker.random_int(min=10, max=100),
        ementa=faker.text(),
        sala=None
    ) for i in range(100)]

def fake_disciplina(unidades_escolas:list[UnidadeEscola],N:int) -> List[Disciplina]:
    return [Disciplina(
        unidade_escola=str(random.choice(unidades_escolas).id_unidade),
        id=i+1,
        qtd_aulas_semanais=faker.random_int(min=1, max=3),
        material_didatico_basico=faker.word(),
        sala=None,
    ) for i in range(N)]

def fake_curso_requisitos(N: int = 10) -> List[CursoRequisitos]:
    from sqlalchemy import Integer as SQLAInteger
    return [CursoRequisitos(
        id_curso=SQLAInteger(),
        id_curso_requisito=SQLAInteger()
    ) for _ in range(N)]

def fake_curso_disciplina_requerida(N: int = 10) -> List[CursoDisciplinaRequerida]:
    from sqlalchemy import Integer as SQLAInteger
    return [CursoDisciplinaRequerida(
        id_curso=SQLAInteger(),
        id_disciplina=random.randint(1, 10)
    ) for _ in range(N)]

def fake_regras(N: int = 10) -> List[Regras]:
    return [Regras(
        id=i+1,
        descricao=faker.sentence()
    ) for i in range(N)]

def fake_regras_curso(cursos:List[Curso],regras:list[Regras]) -> List[RegrasCurso]:
    regras_cursos:List[RegrasCurso] = []
    for curso in cursos:
        num_regras=faker.random_int(min=0, max=len(regras))
        regras = random.sample(regras, num_regras)
        for regra in regras:
            regras_cursos.append(RegrasCurso(
                id_regra=regra.id,
                codigo_curso=curso.id
            ))
    return regras_cursos

def fake_infraestrutura(N: int = 10) -> List[Infraestrutura]:
    return [Infraestrutura(
        id=i+1,
        descricao=faker.word()
    ) for i in range(N)]


def fake_curso_requer_infraestrutura(cursos:List[Curso],infraestruturas:list[Infraestrutura]) -> List[CursoRequerInfraestrutura]:
    infraestruturas_cursos:List[CursoRequerInfraestrutura] = []
    for curso in cursos:
        num_infraestruturas=faker.random_int(min=0, max=len(infraestruturas))
        infraestruturas = random.sample(infraestruturas, num_infraestruturas)
        for infraestrutura in infraestruturas:
            infraestruturas_cursos.append(CursoRequerInfraestrutura(
                id_curso=curso.id,
                id_infraestrutura=infraestrutura.id
            ))
    return infraestruturas_cursos




def fake_disciplina_professores_responsaveis(disciplinas:list[Disciplina],professores:list[Professor]) -> List[DisciplinaProfessoresResponsaveis]:
    professores_responsaveis: list[DisciplinaProfessoresResponsaveis] = []
    num_professores=len(professores)
    for disciplina in disciplinas:
        qtd_professores= random.randint(1, num_professores // 10)
        for professor in random.sample(professores, qtd_professores):
            professores_responsaveis.append(DisciplinaProfessoresResponsaveis(
                id_disciplina=disciplina.id,
                professor_id=professor.id
        ))
    return professores_responsaveis

def fake_turma(disciplinas:list[Disciplina], salas:list[Sala],N: int = 10) -> List[Turma]:
    turmas: List[Turma] = []
    id=0
    for disciplina in disciplinas:
        num_turmas= faker.random_int(min=1, max=3)
        for _ in range(num_turmas):
            id+=1
            sala = random.choice(salas)
            turmas.append(Turma(
                                id=id,
                                id_disciplina=disciplina.id,
                                capacidade=faker.random_int(min=1, max=100),
                                periodo_letivo=f"{faker.year()}-{random.choice(['1', '2'])}",
                                sala_id=sala.id))
    return turmas

def fake_avaliacao(alunos:list[Aluno],disciplinas:list[Disciplina]) -> List[Avaliação]:
    avaliacoes: List[Avaliação] = []
    for i,aluno in enumerate(alunos):
        avaliacoes.append(Avaliação(
            id=i+1,
            aluno_id=aluno.usuario_id,
            disciplina_id=random.choice(disciplinas).id,
            comentario=faker.sentence(),
            nota_didatica=faker.random_int(min=0, max=10),
            nota_material_de_apoio=faker.random_int(min=0, max=10),
            nota_relevancia_do_conteudo=faker.random_int(min=0, max=10),
            nota_infraestutura=faker.random_int(min=0, max=10)
            )
        )
    return avaliacoes
    
def fake_matricula(alunos:list[Aluno]) -> List[Matricula]:
    matriculas: List[Matricula] = []
    i=1
    for aluno in alunos:
        i+=1
        matriculas.append(Matricula(
            id_matricula=i,
            id_aluno=aluno.usuario_id,
            data_efetivacao=faker.date_this_decade(),
            status_matricula=random.choice([x.value for x in Matricula.StatusMatriculaEnum]),
            bolsa_ou_desconto=round(random.uniform(0, 1000), 2),
            data_limite=faker.date_this_decade()
        ))
    return matriculas

def fake_matricula_disciplina(matriculas:list[Matricula],disciplinas:list[Disciplina]) -> List[MatriculaDisciplina]:
    matricula_turmas: List[MatriculaDisciplina] = []
    id=0
    for matricula in matriculas:
        num_disciplinas= random.randint(3,10 )
        disciplinas_escolhidas= random.sample(disciplinas, num_disciplinas)
        for disciplina in disciplinas_escolhidas:
            id+=1
            matricula_turmas.append(MatriculaDisciplina(
                id,
                id_matricula=matricula.id_matricula,
                id_disciplina=disciplina.id
            ))
    return matricula_turmas

def fake_notas(matricula_disciplinas:list[MatriculaDisciplina]) -> List[Notas]:
    notas:list[Notas]=[]
    for matricula_disciplina in matricula_disciplinas:
        notas.append(Notas(
            id_matricula_disciplina=matricula_disciplina.id,
            nota=round(random.uniform(0, 10), 2)
        ))
    return notas