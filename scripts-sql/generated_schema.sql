
CREATE TABLE aviso (
	id SERIAL NOT NULL, 
	texto VARCHAR NOT NULL, 
	timestamp_criacao TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
	PRIMARY KEY (id)
)


CREATE TABLE infraestrutura (
	id SERIAL NOT NULL, 
	descricao VARCHAR NOT NULL, 
	PRIMARY KEY (id)
)


CREATE TABLE regras (
	id SERIAL NOT NULL, 
	descricao VARCHAR NOT NULL, 
	PRIMARY KEY (id)
)


CREATE TABLE unidade_escola (
	id_unidade SERIAL NOT NULL, 
	cidade VARCHAR NOT NULL, 
	estado VARCHAR NOT NULL, 
	pais VARCHAR NOT NULL, 
	predio VARCHAR NOT NULL, 
	bloco VARCHAR NOT NULL, 
	PRIMARY KEY (id_unidade)
)


CREATE TABLE usuario (
	id SERIAL NOT NULL, 
	nome VARCHAR NOT NULL, 
	sobrenome VARCHAR NOT NULL, 
	data_de_nascimento DATE NOT NULL, 
	"endereço" VARCHAR NOT NULL, 
	sexo VARCHAR(1) NOT NULL, 
	numero_de_telefone VARCHAR(15) NOT NULL, 
	email VARCHAR NOT NULL, 
	senha VARCHAR NOT NULL, 
	tipo_usuario tiposusuarioenum NOT NULL, 
	PRIMARY KEY (id), 
	CONSTRAINT unicidade_nome_sobrenome_telefone UNIQUE (nome, sobrenome, numero_de_telefone)
)


CREATE TABLE aluno (
	usuario_id INTEGER NOT NULL, 
	unidade_escola INTEGER NOT NULL, 
	PRIMARY KEY (usuario_id), 
	FOREIGN KEY(usuario_id) REFERENCES usuario (id), 
	FOREIGN KEY(unidade_escola) REFERENCES unidade_escola (id_unidade)
)


CREATE TABLE funcionario_administrativo (
	usuario_id INTEGER NOT NULL, 
	PRIMARY KEY (usuario_id), 
	FOREIGN KEY(usuario_id) REFERENCES usuario (id)
)


CREATE TABLE mensagem (
	id SERIAL NOT NULL, 
	remetente_id INTEGER NOT NULL, 
	timestamp_criacao TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
	texto VARCHAR NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(remetente_id) REFERENCES usuario (id)
)


CREATE TABLE professor (
	id INTEGER NOT NULL, 
	area_especializacao VARCHAR NOT NULL, 
	titulacao VARCHAR NOT NULL, 
	unidade_escola INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES usuario (id), 
	FOREIGN KEY(unidade_escola) REFERENCES unidade_escola (id_unidade)
)


CREATE TABLE sala (
	id SERIAL NOT NULL, 
	unidade_escola INTEGER NOT NULL, 
	numero INTEGER NOT NULL, 
	capacidade INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (unidade_escola, numero), 
	FOREIGN KEY(unidade_escola) REFERENCES unidade_escola (id_unidade)
)


CREATE TABLE departamento_academico (
	codigo SERIAL NOT NULL, 
	nome VARCHAR NOT NULL, 
	chefe_id INTEGER NOT NULL, 
	PRIMARY KEY (codigo), 
	FOREIGN KEY(chefe_id) REFERENCES professor (id)
)


CREATE TABLE disciplina (
	unidade_escola INTEGER NOT NULL, 
	id SERIAL NOT NULL, 
	qtd_aulas_semanais INTEGER NOT NULL, 
	material_didatico_basico VARCHAR NOT NULL, 
	sala INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(unidade_escola) REFERENCES unidade_escola (id_unidade), 
	FOREIGN KEY(sala) REFERENCES sala (id)
)


CREATE TABLE matricula (
	id_matricula SERIAL NOT NULL, 
	id_aluno INTEGER NOT NULL, 
	data_efetivacao DATE NOT NULL, 
	status_matricula statusmatriculaenum NOT NULL, 
	bolsa_ou_desconto FLOAT NOT NULL, 
	data_limite DATE NOT NULL, 
	PRIMARY KEY (id_matricula), 
	FOREIGN KEY(id_aluno) REFERENCES aluno (usuario_id)
)


CREATE TABLE mensagem_destinatario (
	mensagem_id INTEGER NOT NULL, 
	destinatario_id INTEGER NOT NULL, 
	PRIMARY KEY (mensagem_id, destinatario_id), 
	FOREIGN KEY(mensagem_id) REFERENCES mensagem (id), 
	FOREIGN KEY(destinatario_id) REFERENCES usuario (id)
)


CREATE TABLE avaliacao (
	id SERIAL NOT NULL, 
	aluno_id INTEGER NOT NULL, 
	disciplina_id INTEGER NOT NULL, 
	comentario VARCHAR NOT NULL, 
	nota_didatica INTEGER NOT NULL, 
	nota_material_de_apoio INTEGER NOT NULL, 
	nota_relevancia_do_conteudo INTEGER NOT NULL, 
	nota_infraestutura INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(aluno_id) REFERENCES aluno (usuario_id), 
	FOREIGN KEY(disciplina_id) REFERENCES disciplina (id)
)


CREATE TABLE curso (
	id SERIAL NOT NULL, 
	unidade_escola INTEGER NOT NULL, 
	codigo VARCHAR NOT NULL, 
	nome VARCHAR NOT NULL, 
	departamento_academico INTEGER NOT NULL, 
	nivel_ensino nivelensinoenum NOT NULL, 
	carga_horaria_total INTEGER NOT NULL, 
	numero_vagas INTEGER NOT NULL, 
	ementa VARCHAR NOT NULL, 
	sala INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(unidade_escola) REFERENCES unidade_escola (id_unidade), 
	FOREIGN KEY(departamento_academico) REFERENCES departamento_academico (codigo), 
	FOREIGN KEY(sala) REFERENCES sala (id)
)


CREATE TABLE disciplina_professor (
	id_disciplina INTEGER NOT NULL, 
	professor_id INTEGER NOT NULL, 
	PRIMARY KEY (id_disciplina, professor_id), 
	FOREIGN KEY(id_disciplina) REFERENCES disciplina (id), 
	FOREIGN KEY(professor_id) REFERENCES professor (id)
)


CREATE TABLE matricula_turma (
	id_matricula INTEGER NOT NULL, 
	id_disciplina INTEGER NOT NULL, 
	PRIMARY KEY (id_matricula, id_disciplina), 
	FOREIGN KEY(id_matricula) REFERENCES matricula (id_matricula), 
	FOREIGN KEY(id_disciplina) REFERENCES disciplina (id)
)


CREATE TABLE notas (
	disciplina_id INTEGER NOT NULL, 
	matricula_id INTEGER NOT NULL, 
	nota FLOAT NOT NULL, 
	PRIMARY KEY (disciplina_id, matricula_id), 
	FOREIGN KEY(disciplina_id) REFERENCES disciplina (id), 
	FOREIGN KEY(matricula_id) REFERENCES matricula (id_matricula)
)


CREATE TABLE turma (
	id SERIAL NOT NULL, 
	id_disciplina INTEGER NOT NULL, 
	capacidade INTEGER NOT NULL, 
	periodo_letivo VARCHAR NOT NULL, 
	sala_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id_disciplina) REFERENCES disciplina (id), 
	FOREIGN KEY(sala_id) REFERENCES sala (id)
)


CREATE TABLE curso_disciplina_requerida (
	id_curso INTEGER NOT NULL, 
	id_disciplina INTEGER NOT NULL, 
	PRIMARY KEY (id_curso, id_disciplina), 
	FOREIGN KEY(id_curso) REFERENCES curso (id), 
	FOREIGN KEY(id_disciplina) REFERENCES disciplina (id)
)


CREATE TABLE curso_requer_infraestrutura (
	id_curso INTEGER NOT NULL, 
	id_infraestrutura INTEGER NOT NULL, 
	PRIMARY KEY (id_curso, id_infraestrutura), 
	FOREIGN KEY(id_curso) REFERENCES curso (id), 
	FOREIGN KEY(id_infraestrutura) REFERENCES infraestrutura (id)
)


CREATE TABLE curso_requisitos (
	id_curso INTEGER NOT NULL, 
	id_curso_requisito INTEGER NOT NULL, 
	PRIMARY KEY (id_curso, id_curso_requisito), 
	FOREIGN KEY(id_curso) REFERENCES curso (id), 
	FOREIGN KEY(id_curso_requisito) REFERENCES curso (id)
)


CREATE TABLE regras_curso (
	id_regra INTEGER NOT NULL, 
	codigo_curso INTEGER NOT NULL, 
	PRIMARY KEY (id_regra, codigo_curso), 
	FOREIGN KEY(id_regra) REFERENCES regras (id), 
	FOREIGN KEY(codigo_curso) REFERENCES curso (id)
)

