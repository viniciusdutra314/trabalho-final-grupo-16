from typing import Any, List
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.dialects import postgresql
from faked_relations import *

with open("scripts-sql/populate.sql", "w") as sqlfile:
    insert_objects: List[List[Any]] = []
    insert_objects.append(fake_unidade_escola())
    insert_objects.append(fake_usuario())
    insert_objects.append(fake_departamento_academico())
    insert_objects.append(fake_funcionario_administrativo())
    insert_objects.append(fake_sala())
    insert_objects.append(fake_curso())
    insert_objects.append(fake_disciplina())
    insert_objects.append(fake_professor())
    insert_objects.append(fake_aluno())
    insert_objects.append(fake_aviso())
    insert_objects.append(fake_mensagem())
    insert_objects.append(fake_mensagem_destinatario())
    insert_objects.append(fake_disciplina_professores_responsaveis())
    insert_objects.append(fake_turma())
    insert_objects.append(fake_avaliacao())
    insert_objects.append(fake_matricula())
    insert_objects.append(fake_matricula_turma())
    insert_objects.append(fake_notas())
    insert_objects.append(fake_regras())
    insert_objects.append(fake_regras_curso())
    insert_objects.append(fake_infraestrutura())
    insert_objects.append(fake_curso_requer_infraestrutura())

    for obj_list in insert_objects:
        for obj in obj_list:
            values = {column: getattr(obj, column) for column in obj.__table__.c.keys()}
            insert_stmt = insert(obj.__table__).values(**values)
            sql = str(insert_stmt.compile(dialect=postgresql.dialect(), compile_kwargs={"literal_binds": True}))
            sqlfile.write(sql + ";\n")

