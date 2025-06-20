import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from typing import Optional
from sqlalchemy.schema import CreateTable
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class Database(DeclarativeBase):
    pass

class Curso(Database):
    __tablename__ = "curso"
    id : Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(sa.String(100))
    nickname: Mapped[Optional[str]] = mapped_column(sa.String(50))

for table in Database.metadata.sorted_tables:
    print(CreateTable(table).compile(dialect=postgresql.dialect()))