-- Criação e uso do banco de dados (descomentado em ambientes locais)
-- CREATE DATABASE Northwind;
-- USE Northwind;

-- Adicionar as colunas para a tabela de Categorias
ALTER TABLE Categorias
ADD COLUMN CategoriaID INT,
ADD COLUMN Nome VARCHAR(100),
ADD COLUMN Descricao TEXT;

-- Adicionar as colunas para a tabela de Clientes
ALTER TABLE Clientes
ADD COLUMN ClienteID INT,
ADD COLUMN Nome VARCHAR(100),
ADD COLUMN Endereco VARCHAR(200),
ADD COLUMN Cidade VARCHAR(100),
ADD COLUMN Estado VARCHAR(100),
ADD COLUMN Cep VARCHAR(20),
ADD COLUMN Pais VARCHAR(50),
ADD COLUMN Telefone VARCHAR(50);

-- Adicionar as colunas para a tabela de Fornecedores
ALTER TABLE Fornecedores
ADD COLUMN FornecedorID INT,
ADD COLUMN Nome VARCHAR(100),
ADD COLUMN Endereco VARCHAR(200),
ADD COLUMN Cidade VARCHAR(100),
ADD COLUMN Estado VARCHAR(100),
ADD COLUMN Cep VARCHAR(20),
ADD COLUMN Pais VARCHAR(50),
ADD COLUMN Telefone VARCHAR(50);

-- Adicionar as colunas para a tabela de Produtos
ALTER TABLE Produtos
ADD COLUMN ProdutoID INT,
ADD COLUMN Nome VARCHAR(100),
ADD COLUMN CategoriaID INT,
ADD COLUMN FornecedorID INT,
ADD COLUMN Preco DECIMAL(10, 2),
ADD COLUMN QuantidadeEmEstoque INT,
ADD COLUMN QuantidadeMinima INT,
ADD COLUMN UnidadeMedida VARCHAR(50);

-- Adicionar as colunas para a tabela de Funcionários
ALTER TABLE Funcionarios
ADD COLUMN FuncionarioID INT,
ADD COLUMN Nome VARCHAR(100),
ADD COLUMN Cargo VARCHAR(50),
ADD COLUMN Endereco VARCHAR(200),
ADD COLUMN Cidade VARCHAR(100),
ADD COLUMN Estado VARCHAR(100),
ADD COLUMN Cep VARCHAR(20),
ADD COLUMN Pais VARCHAR(50),
ADD COLUMN Telefone VARCHAR(50);

-- Adicionar as colunas para a tabela de Pedidos
ALTER TABLE Pedidos
ADD COLUMN PedidoID INT,
ADD COLUMN ClienteID INT,
ADD COLUMN FuncionarioID INT
