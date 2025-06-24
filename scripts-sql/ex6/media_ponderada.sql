SELECT 
    a.usuario_id,
    u.nome,
    u.sobrenome,
    AVG(n.nota) AS media_ponderada
FROM aluno a
JOIN usuario u ON a.usuario_id = u.id
JOIN matricula m ON m.id_aluno = a.usuario_id
JOIN matricula_disciplina md ON md.id_matricula = m.id_matricula
JOIN notas n ON n.id_matricula_disciplina = md.id
GROUP BY a.usuario_id, u.nome, u.sobrenome
ORDER BY AVG(n.nota) DESC;