SELECT 
	s.unidade_escola,
    s.id AS sala_id, 
    COUNT(t.id) AS total_turmas
FROM sala s	
JOIN unidade_escola ue ON s.unidade_escola = ue.id_unidade
LEFT JOIN turma t ON t.sala_id = s.id
GROUP BY s.id, s.numero, ue.cidade, ue.predio
ORDER BY COUNT(t.id) DESC