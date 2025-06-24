from comunicacao import * 
from sqlalchemy.schema import CreateTable
from sqlalchemy import create_engine
with open("../scripts-sql/generated_schema.sql", "w") as file:
    for table in Database.metadata.sorted_tables:
        file.write(str(CreateTable(table).compile(dialect=None)))


engine = create_engine("sqlite:///local.db")
Database.metadata.create_all(engine)