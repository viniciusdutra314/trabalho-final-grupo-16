SELECT 
    d.id AS disciplina_id,
    p.id AS professor_id,
    u.nome AS professor_nome,
    u.sobrenome AS professor_sobrenome
FROM professor p
JOIN usuario u ON p.id = u.id
JOIN disciplina_professor dp ON p.id = dp.professor_id
JOIN disciplina d ON dp.id_disciplina = d.id
ORDER BY d.id;