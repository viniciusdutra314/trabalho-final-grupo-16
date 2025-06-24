import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from schemes.comunicacao import * 
from sqlalchemy.schema import CreateTable,CreateIndex
from sqlalchemy.dialects import postgresql
from sqlalchemy import Index, text
from schemes.ensino import Usuário, Matricula, Curso

used_dialect = postgresql.dialect()


with open("scripts-sql/generated_schema.sql", "w") as file:
    for table in Database.metadata.sorted_tables:
        file.write(str(CreateTable(table).compile(dialect=used_dialect)))
        file.write(";\n")

indices_ex_7:list[tuple[Index,str]] = [
    (
        Index("ix_usuario_email", Usuário.email),
        "index_email.sql"
    ),
    (
        Index(
            "ix_matricula_status_ativa",
            Matricula.status_matricula,
            postgresql_where=text("status_matricula = 'Ativa'")
        ),
        "index_matricula_ativa.sql"
    ),
]
for index, filename in indices_ex_7:
    with open(f"scripts-sql/ex7/{filename}", "w") as file:
        file.write(str(CreateIndex(index).compile(dialect=used_dialect)))
