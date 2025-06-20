from schemas import *
import random 
from faker import Faker
import itertools

def take(n, generator):
    return [next(generator()) for _ in range(n)]


def fake_usuário_generator() -> Usuário:
    fake=Faker(locale='pt_BR')
    id=0
    while True:
        id+=1
        sexo = random.choice(['M', 'F'])
        if sexo == 'M':
            nome = fake.first_name_male()
            sobrenome =fake.last_name_male()
        else:
            nome = fake.first_name_female()
            sobrenome = fake.last_name_female()
        yield Usuário(
            id=id,
            nome=nome,
            sobrenome=sobrenome,
            data_de_nascimento=fake.date_of_birth(minimum_age=18, maximum_age=90),
            endereço=fake.address().replace("\n", ", "),
            sexo=sexo,
            numero_de_telefone=fake.phone_number(),
            email=fake.email(),
            senha=fake.password()
        )

for x in take(10,fake_usuário_generator):
    print(x)
