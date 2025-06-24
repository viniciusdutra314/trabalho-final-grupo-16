SELECT DISTINCT
    d.id AS disciplina_id,
    da.nome AS departamento
FROM departamento_academico da
JOIN curso c ON c.departamento_academico = da.codigo
JOIN disciplina d ON d.unidade_escola = c.unidade_escola;