"""
2. Utilizando a linguagem Python, crie um programa que implemente as operações de uma
calculadora simples (adição, subtração, multiplicação e divisão). Para cada operação, crie um
método, que receberá dois valores como parâmetro e retornará o resultado do
processamento. Não é necessário ler os valores do teclado, você pode deixar os valores dos
parâmetros fixos no código.
"""

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subtrai(self):
        return self.a - self.b

    def multiplica(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


c = Calculadora(10,2)
print('Soma:', c.soma())
print('Subtração:', c.subtrai())
print('Multiplicação:', c.multiplica())
print('Divisão:', c.divide())
