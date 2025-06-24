SELECT id, texto,timestamp_criacao
FROM aviso 
WHERE timestamp_criacao BETWEEN '2025-06-24' AND '2025-08-24'
ORDER BY timestamp_criacao DESC;