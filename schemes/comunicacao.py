from schemes.ensino import *
from sqlalchemy import  PrimaryKeyConstraint,DateTime

class Aviso(Database):
    __tablename__ = "aviso"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    texto: Mapped[str] = mapped_column(String, nullable=False)
    timestamp_criacao: Mapped[datetime.datetime] = mapped_column(DateTime,nullable=False)


class Mensagem(Database):
    __tablename__ = "mensagem"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    remetente_id: Mapped[int] = mapped_column(ForeignKey(Usuário.id), nullable=False)
    timestamp_criacao: Mapped[datetime.datetime] = mapped_column(DateTime,nullable=False)
    texto: Mapped[str] = mapped_column(String, nullable=False)

class MensagemDestinatario(Database):
    __tablename__ = "mensagem_destinatario"
    mensagem_id: Mapped[int] = mapped_column(ForeignKey(Mensagem.id), nullable=False)
    destinatario_id: Mapped[int] = mapped_column(ForeignKey(Usuário.id), nullable=False)
    __table_args__=(
        PrimaryKeyConstraint(
            "mensagem_id",
            "destinatario_id",
        ),
    )
