import exercicio as exer
import math

"""Questão 1"""

def test_paramentros_positivos():
    resultado = exer.calcular_area(1,2)
    assert resultado == 1
    resultado = exer.calcular_area(3,4)
    assert resultado == 6
    resultado = exer.calcular_area(5,2)
    assert resultado == 5

def test_paramentros_negativos():
    resultado = exer.calcular_area(-1,2)
    assert math.isnan(resultado)
    resultado = exer.calcular_area(1,-2)
    assert math.isnan(resultado)
    resultado = exer.calcular_area(-1,-2)
    assert math.isnan(resultado)

def test_retorno():
    resultado = exer.calcular_area(1,2)
    assert type(resultado) == float

"""Questão 2"""

def test_paramentros_positivos():
    perimetro = exer.calcular_perimetro(1,2,3)
    assert perimetro == 6
    perimetro = exer.calcular_perimetro(3,3,3)
    assert perimetro == 9
    perimetro = exer.calcular_perimetro(5,1,9)
    assert perimetro == 15

def test_paramentros_negativos():
    perimetro = exer.calcular_perimetro(-1,2)
    assert math.isnan(perimetro)
    perimetro = exer.calcular_perimetro(1,-2)
    assert math.isnan(perimetro)
    perimetro = exer.calcular_perimetro(-1,-2)
    assert math.isnan(perimetro)

"""Questão 3"""

def test_paramentros_positivos():
    perimetro = exer.calcular_almoco(5,4,10)
    assert total == 36.3
    perimetro = exer.calcular_almoco(4,20,2)
    assert total == 28.6
    perimetro = exer.calcular_almoco(10,45,10)
    assert total == 71.5

def test_paramentros_negativos():
    total = exer.calcular_almoco(-1,2,3)
    assert math.isnan(total)
    total = exer.calcular_almoco(1,-2,3)
    assert math.isnan(total)
    total = exer.calcular_almoco(1,2,-3)
    assert math.isnan(total)
    total = exer.calcular_almoco(-1,-2,3)
    assert math.isnan(total)
    total = exer.calcular_almoco(1,-2,-3)
    assert math.isnan(total)
    total = exer.calcular_almoco(-1,2,-3)
    assert math.isnan(total)
    total = exer.calcular_almoco(-1,-2,-3)
    assert math.isnan(total)

"""Questão 4"""

def test_paramentros_positivos():
    qte_gasoloina = exer.calcular_qte_gasolina(5)
    assert qte_gasolina == 0.416
    qte_gasolina = exer.calcular_qte_gasolina(14)
    assert qte_gasolina == 1.166
    qte_gasolina = exer.calcular_qte_gasolina(378)
    assert qte_gasolina == 31.5

def test_paramentros_negativos():
    qte_gasolina = exer.calcular_qte_gasolina(-1)
    assert math.isnan(qte_gasolina)
    qte_gasolina = exer.calcular_qte_gasolina(-54)
    assert math.isnan(qte_gasolina)
    qte_gasolina = exer.calcular_qte_gasolina(-894)
    assert math.isnan(qte_gasolina)

"""Questão 5"""

def test_contar_letras():
    contar = exer.ler_nome(alexia)
    assert contar = alexia, 6
    contar = exer.ler_nome(fischer15)
    assert contar = fischer, 9
    contar = exer.ler_nome(n@th@li@)
    assert contar = nathalia, 8

"""Questão 6"""






    
