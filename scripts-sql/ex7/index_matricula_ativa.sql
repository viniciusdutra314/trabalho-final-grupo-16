CREATE INDEX ix_matricula_status_ativa ON matricula (status_matricula) 
WHERE status_matricula = 'Ativa'