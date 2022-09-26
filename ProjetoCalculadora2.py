"""
3. Altere o programa anterior, transferindo os métodos que representam as operações (adição,
subtração, multiplicação e divisão) para um arquivo chamado Calculadora.py. Crie um
outro arquivo ProjetoCalculadora2.py que inicialize o programa e utilize a classe
Calculadora para realizar as operações.
"""

from Calculadora import Calculadora

c = Calculadora(10,3)
print('Soma:', c.soma())
print('Subtração:', c.subtrai())
print('Multiplicação:', c.multiplica())
print('Divisão:', c.divide())
