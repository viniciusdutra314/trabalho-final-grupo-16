import random
from time import time

from faker import Faker
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from schemas import Database, Usuário


def generate_fake_usuários(num_usuarios: int) -> list[Usuário]:
    fake = Faker(locale="pt_BR")
    usuarios: list[Usuário] = []
    for id in range(num_usuarios):
        sexo = random.choice(["M", "F"])
        nome = fake.first_name_male() if sexo == "M" else fake.first_name_female()
        sobrenome = fake.last_name()
        usuarios.append(
            Usuário(
                id=id,
                nome=nome,
                sobrenome=sobrenome,
                data_de_nascimento=fake.date_of_birth(minimum_age=18, maximum_age=90),
                endereço=fake.address().replace("\n", ", "),
                sexo=sexo,
                numero_de_telefone=fake.phone_number(),
                email=fake.email(),
                senha=fake.password(),
            )
        )
    return usuarios


engine = create_engine("sqlite:///database.db")
Database.metadata.create_all(engine)

with Session(engine) as session:
    session.add_all(generate_fake_usuários(100_000))
    session.commit()

    time_start = time()
    session.execute(text("SELECT MAX(data_de_nascimento) FROM usuario"))
    time_no_index = 1000 * (time() - time_start)

    session.execute(
        text("CREATE INDEX idx_data_nascimento ON usuario (data_de_nascimento)")
    )
    session.commit()

    time_start = time()
    session.execute(text("SELECT MAX(data_de_nascimento) FROM usuario"))
    time_with_index = 1000 * (time() - time_start)
    print(
        f"{time_no_index=:.2f} (ms), {time_with_index=:.2f} (ms), speedup= {time_no_index / time_with_index:.2f}"
    )
