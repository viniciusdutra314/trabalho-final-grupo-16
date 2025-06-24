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