CREATE VIEW vw_chefes_departamento_contato AS
SELECT
    da.codigo AS departamento_id,
    da.nome AS departamento_nome,
    p.id AS chefe_id,
    u.nome AS chefe_nome,
    u.sobrenome AS chefe_sobrenome,
    u.email AS chefe_email,
    u.numero_de_telefone AS chefe_telefone
FROM departamento_academico da
JOIN professor p ON da.chefe_id = p.id
JOIN usuario u ON p.id = u.id;