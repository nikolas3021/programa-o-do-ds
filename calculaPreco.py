# Define função para calcuclar preço final
def calcular_preco_final(nome, preco, desconto=0):
    preco_final = preco - (preco * desconto / 100)
    print(f"Preço final de {nome}: R$ {preco_final:.2f}")

# Exemplo de uso
calcular_preco_final("Fone de ouvido", 200, 15)
using System;

class Produto

{

    public string Nome { get; set; }

    public double Preco { get; set; }

    public double Desconto { get; set; }


    public double CalcularPrecoFinal()

    {

        return Preco - (Preco * Desconto / 100);

    }

}

class Program

{

    static void Main()

    {

        Produto produto = new Produto

        {

            Nome = "Fone de ouvido",

            Preco = 200,

            Desconto = 25

        };
        Console.WriteLine($"Preço iniical de {produto.Nome}: R$ {produto.Preco:F2}");
        Console.WriteLine($"Preço final de {produto.Nome}: R$ {produto.CalcularPrecoFinal():F2}");

    }

}
