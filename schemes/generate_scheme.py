from comunicacao import * 
from sqlalchemy.schema import CreateTable

with open("../scripts-sql/generated_schema.sql", "w") as file:
    for table in Database.metadata.sorted_tables:
        file.write(str(CreateTable(table).compile(dialect=None)))