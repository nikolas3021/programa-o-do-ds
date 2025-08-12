-- Ver todos os países disponíveis na tabela Customers
SELECT DISTINCT Country FROM Customers;

-- Ver clientes do Brasil
SELECT * FROM Customers WHERE Country = 'Brazil';

-- Ver clientes do Reino Unido
SELECT * FROM Customers WHERE Country = 'UK';

-- Ver clientes da França
SELECT * FROM Customers WHERE Country = 'France';

-- Ver clientes da Argentina
SELECT * FROM Customers WHERE Country = 'Argentina';
