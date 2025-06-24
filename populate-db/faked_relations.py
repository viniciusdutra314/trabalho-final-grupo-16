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

def fake_unidade_escola() -> List[UnidadeEscola]:
    return [UnidadeEscola(id_unidade=i,
        cidade=faker.city(),
        estado=faker.estado_sigla(),
        pais='Brasil',
        predio=faker.word(),
        bloco=faker.random_letter()
    ) for i in range(10)]

def fake_departamento_academico() -> List[DepartamentoAcademico]:
    return [DepartamentoAcademico(
        codigo=i+1,
        nome=faker.company(),
        chefe_id=random.randint(1, 10)
    ) for i in range(5)]

def fake_funcionario_administrativo() -> List[FuncionarioAdministrativo]:
    return [FuncionarioAdministrativo(
        usuario_id=random.randint(1, 20)
    ) for _ in range(5)]

def fake_usuario() -> List[Usuário]:
    return [Usuário(
        id=i+1,
        nome=faker.first_name(),
        sobrenome=faker.last_name(),
        data_de_nascimento=faker.date_of_birth(minimum_age=18, maximum_age=60),
        endereço=faker.address(),
        sexo=random.choice(['M', 'F']),
        numero_de_telefone=faker.phone_number(),
        email=faker.email(),
        senha=faker.password(),
        tipo_usuario=random.choice(list(Usuário.TiposUsuarioEnum))
    ) for i in range(20)]

def fake_aviso() -> List[Aviso]:
    return [Aviso(
        id=i+1,
        texto=faker.sentence(),
        timestamp_criacao=faker.date_time_this_year()
    ) for i in range(10)]

def fake_mensagem() -> List[Mensagem]:
    return [Mensagem(
        id=i+1,
        remetente_id=random.randint(1, 20),
        timestamp_criacao=faker.date_time_this_year(),
        texto=faker.text()
    ) for i in range(10)]

def fake_mensagem_destinatario() -> List[MensagemDestinatario]:
    return [MensagemDestinatario(
        mensagem_id=random.randint(1, 10),
        destinatario_id=random.randint(1, 20)
    ) for _ in range(10)]

def fake_sala() -> List[Sala]:
    return [Sala(
        id=i+1,
        unidade_escola=str(random.randint(1, 10)),
        numero=faker.random_int(min=1, max=50),
        capacidade=faker.random_int(min=10, max=100)
    ) for i in range(10)]

def fake_curso() -> List[Curso]:
    return [Curso(
        id=i+1,
        unidade_escola=str(random.randint(1, 10)),
        codigo=f"CURSO{i+1}",
        nome=faker.job(),
        departamento_academico=random.randint(1, 5),
        nivel_ensino=random.choice(list(Curso.NivelEnsinoEnum)),
        carga_horaria_total=faker.random_int(min=100, max=2000),
        numero_vagas=faker.random_int(min=10, max=100),
        ementa=faker.text(),
        sala=random.randint(1, 10)
    ) for i in range(10)]

def fake_disciplina() -> List[Disciplina]:
    return [Disciplina(
        id=i+1,
        unidade_escola=str(random.randint(1, 10)),
        qtd_aulas_semanais=faker.random_int(min=1, max=10),
        material_didatico_basico=faker.word(),
        sala=random.randint(1, 10)
    ) for i in range(10)]

def fake_curso_requisitos() -> List[CursoRequisitos]:
    from sqlalchemy import Integer as SQLAInteger
    return [CursoRequisitos(
        id_curso=SQLAInteger(),
        id_curso_requisito=SQLAInteger()
    ) for _ in range(10)]

def fake_curso_disciplina_requerida() -> List[CursoDisciplinaRequerida]:
    from sqlalchemy import Integer as SQLAInteger
    return [CursoDisciplinaRequerida(
        id_curso=SQLAInteger(),
        id_disciplina=random.randint(1, 10)
    ) for _ in range(10)]

def fake_regras() -> List[Regras]:
    return [Regras(
        id=i+1,
        descricao=faker.sentence()
    ) for i in range(10)]

def fake_regras_curso() -> List[RegrasCurso]:
    return [RegrasCurso(
        id_regra=random.randint(1, 10),
        codigo_curso=random.randint(1, 10)
    ) for _ in range(10)]

def fake_infraestrutura() -> List[Infraestrutura]:
    return [Infraestrutura(
        id=i+1,
        descricao=faker.word()
    ) for i in range(10)]

def fake_curso_requer_infraestrutura() -> List[CursoRequerInfraestrutura]:
    return [CursoRequerInfraestrutura(
        id_curso=random.randint(1, 10),
        id_infraestrutura=random.randint(1, 10)
    ) for _ in range(10)]

def fake_aluno() -> List[Aluno]:
    return [Aluno(
        usuario_id=i+1,
        unidade_escola=str(random.randint(1, 10))
    ) for i in range(10)]

def fake_professor() -> List[Professor]:
    return [Professor(
        id=i+1,
        area_especializacao=faker.job(),
        titulacao=faker.word(),
        unidade_escola=str(random.randint(1, 10))
    ) for i in range(10)]

def fake_disciplina_professores_responsaveis() -> List[DisciplinaProfessoresResponsaveis]:
    return [DisciplinaProfessoresResponsaveis(
        id_disciplina=random.randint(1, 10),
        professor_id=random.randint(1, 10)
    ) for _ in range(10)]

def fake_turma() -> List[Turma]:
    return [Turma(
        id=i+1,
        id_disciplina=random.randint(1, 10),
        capacidade=faker.random_int(min=10, max=100),
        periodo_letivo=f"{faker.year()}-{random.choice(['1', '2'])}",
        sala_id=random.randint(1, 10)
    ) for i in range(10)]

def fake_avaliacao() -> List[Avaliação]:
    return [Avaliação(
        id=i+1,
        aluno_id=random.randint(1, 10),
        disciplina_id=random.randint(1, 10),
        comentario=faker.sentence(),
        nota_didatica=faker.random_int(min=0, max=10),
        nota_material_de_apoio=faker.random_int(min=0, max=10),
        nota_relevancia_do_conteudo=faker.random_int(min=0, max=10),
        nota_infraestutura=faker.random_int(min=0, max=10)
    ) for i in range(10)]

def fake_matricula() -> List[Matricula]:
    return [Matricula(
        id_matricula=i+1,
        id_aluno=random.randint(1, 10),
        data_efetivacao=faker.date_this_decade(),
        status_matricula=random.choice(list(Matricula.StatusMatriculaEnum)),
        bolsa_ou_desconto=round(random.uniform(0, 1000), 2),
        data_limite=faker.date_this_decade()
    ) for i in range(10)]

def fake_matricula_turma() -> List[MatriculaTurma]:
    return [MatriculaTurma(
        id_matricula=random.randint(1, 10),
        id_disciplina=random.randint(1, 10)
    ) for _ in range(10)]

def fake_notas() -> List[Notas]:
    return [Notas(
        disciplina_id=random.randint(1, 10),
        matricula_id=random.randint(1, 10),
        nota=round(random.uniform(0, 10), 2)
    ) for _ in range(10)]
