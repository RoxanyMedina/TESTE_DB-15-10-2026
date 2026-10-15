import pytest
from operacoes import somar
from operacoes import dividir
from operacoes import classificar_idade

# def test_somar_positivos():
#     assert somar (2, 3) == 5

# def test_dividir_normal():
#     assert dividir(10, 2) == 5





@pytest.mark.parametrize(
    "idade, resultado_esperado",
    [
        (0, "MENOR DE IDADE"),
        (17,"MENOR DE IDADE"),
        (18, "MAIOR DE IDADE"),
        (30, "MAIOR DE IDADE"),
    ]
)



def test_classificar_idade(idade, resultado_esperado):
    assert classificar_idade(idade) == resultado_esperado
  
  