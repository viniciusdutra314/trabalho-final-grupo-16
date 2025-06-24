import dis
from importlib import metadata
from typing import Any, List
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.dialects import postgresql
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from faked_relations import *

with open("scripts-sql/populate.sql", "w") as sqlfile:
    insert_objects: List[List[Any]] = []
    insert_objects.append(unidades_escolas:=fake_unidade_escola(10))
    insert_objects.append(usuarios:=fake_usuario(1000))
    insert_objects.append(professores:=fake_professor(usuarios))
    insert_objects.append(alunos:=fake_aluno(usuarios))
    insert_objects.append(funcionarios_administrativos:=fake_funcionario_administrativo(usuarios))

    insert_objects.append(departamentos_academicos:=fake_departamento_academico(professores))
    insert_objects.append(salas:=fake_sala(unidades_escolas,len(unidades_escolas))*30)
    insert_objects.append(cursos:=fake_curso(unidades_escolas, departamentos_academicos))
    insert_objects.append(disciplinas:=fake_disciplina(unidades_escolas,len(unidades_escolas)*10))

    insert_objects.append(aviso:=fake_aviso())
    insert_objects.append(mensagens:=fake_mensagem())
    insert_objects.append(mensagem_destinatarios:=fake_mensagem_destinatario(mensagens))
    insert_objects.append(professores_responsaveis:=fake_disciplina_professores_responsaveis(disciplinas, professores))
    insert_objects.append(turmas:=fake_turma(disciplinas,salas))
    insert_objects.append(avaliações:=fake_avaliacao())
    insert_objects.append(matriculas:=fake_matricula(alunos))
    insert_objects.append(matricula_disciplinas:=fake_matricula_disciplina(matriculas,disciplinas))
    insert_objects.append(notas:=fake_notas(matricula_disciplinas))
    insert_objects.append(regras:=fake_regras())
    insert_objects.append(regras_cursos:=fake_regras_curso(cursos,regras))
    insert_objects.append(infraestruturas:=fake_infraestrutura())
    insert_objects.append(curso_requer_infraestrutura:=fake_curso_requer_infraestrutura(cursos, infraestruturas))

    for obj_list in insert_objects:
        for obj in obj_list:
            values = {column: getattr(obj, column) for column in obj.__table__.c.keys()}
            insert_stmt = insert(obj.__table__).values(**values)
            sql = str(insert_stmt.compile(dialect=postgresql.dialect(), compile_kwargs={"literal_binds": True}))
            sqlfile.write(sql + ";\n")

sqlite_engine = create_engine('sqlite:///localdb.sqlite3')
Database.metadata.create_all(sqlite_engine)
with Session(sqlite_engine) as session:
    for obj_list in insert_objects:
        for obj in obj_list:
            session.add(obj)
    session.commit()

