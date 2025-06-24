from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from faked_relations import *

engine = create_engine("sqlite:///local.db")
Database.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all(fake_unidade_escola())
    session.add_all(fake_usuario())
    session.add_all(fake_departamento_academico())
    session.add_all(fake_funcionario_administrativo())
    session.add_all(fake_sala())
    session.add_all(fake_curso())
    session.add_all(fake_disciplina())
    session.add_all(fake_professor())
    session.add_all(fake_aluno())
    session.add_all(fake_aviso())
    session.add_all(fake_mensagem())
    session.add_all(fake_mensagem_destinatario())
    session.add_all(fake_disciplina_professores_responsaveis())
    session.add_all(fake_turma())
    session.add_all(fake_avaliacao())
    session.add_all(fake_matricula())
    session.add_all(fake_matricula_turma())
    session.add_all(fake_notas())
    session.add_all(fake_regras())
    session.add_all(fake_regras_curso())
    session.add_all(fake_infraestrutura())
    session.add_all(fake_curso_requer_infraestrutura())
    session.commit()

