"""
Código utilizado para fins didáticos no Curso de Sistemas de Informação
da Universidade Federal de Santa Maria - Campus Frederico Westphalen
Autor: Prof. Dr. Joel da Silva

Este módulo de exemplo implenta a Classe Calculadora.

"""
class Calculadora:
    """
        Todo método de uma classe recebe como primeiro parâmetro uma referência à instância que chama o método,
        permitindo assim que o objeto acesse os seus próprios atributos e métodos.
        Por convenção, chamamos esse primeiro parâmetro de self, mas qualquer outro nome poderia ser utilizado.

        O método especial __init__ é chamado automaticamente após a criação de um objeto, e no caso de uma Calculadora,
        na nova instância são criados os atributos ‘a’,  e ‘b’ com os valores dados como argumentos
        do construtor.

        Assim, no corpo de qualquer método, um atributo pode ser criado,
        acessado ou modificado usando self.nome_do_atributo.
    """

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
