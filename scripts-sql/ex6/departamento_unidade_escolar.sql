SELECT 
    da.codigo AS departamento_codigo,
    ue.id_unidade AS unidade_de_ensino,
    ue.cidade,
    ue.predio
FROM unidade_escola ue
JOIN curso c ON c.unidade_escola = ue.id_unidade
JOIN departamento_academico da ON c.departamento_academico = da.codigo
GROUP BY ue.id_unidade, ue.cidade, ue.predio, da.codigo, da.nome;