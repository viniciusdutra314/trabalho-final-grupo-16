SELECT 
    d.id AS disciplina_id,
	s.id AS sala_id

FROM sala s
JOIN disciplina d ON d.sala = s.id
ORDER BY disciplina_id