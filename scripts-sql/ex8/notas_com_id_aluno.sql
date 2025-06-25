CREATE VIEW vw_notas_com_id_aluno AS
SELECT
    n.id_matricula_disciplina,
    md.id_matricula,
    m.id_aluno AS aluno_id,
    n.nota
FROM notas n
JOIN matricula_disciplina md ON n.id_matricula_disciplina = md.id
JOIN matricula m ON md.id_matricula = m.id_matricula;
SELECT * FROM vw_notas_com_id_aluno;