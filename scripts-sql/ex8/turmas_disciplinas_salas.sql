CREATE VIEW vw_turmas_disciplinas_salas AS
SELECT
    t.id AS turma_id,
    d.id AS disciplina_id,
    d.material_didatico_basico AS disciplina_nome,
    s.id AS sala_id,
    s.numero AS sala_numero,
    ue.cidade AS unidade_cidade,
    ue.predio AS unidade_predio
FROM turma t
JOIN disciplina d ON t.id_disciplina = d.id
JOIN sala s ON t.sala_id = s.id
JOIN unidade_escola ue ON s.unidade_escola = ue.id_unidade;
SELECT * FROM vw_turmas_disciplinas_salas;