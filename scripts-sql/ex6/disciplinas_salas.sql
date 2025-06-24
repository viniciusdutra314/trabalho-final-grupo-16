SELECT 
	s.unidade_escola,
    s.numero,
    d.id AS disciplina_id
FROM sala s
JOIN unidade_escola ue ON s.unidade_escola = ue.id_unidade
JOIN disciplina d ON d.sala = s.id
ORDER BY s.unidade_escola,s.numero