class Carro:

  def __init__(self, marca, modelo, cor, ano):
    self.marca = marca
    self.modelo = modelo
    self.cor = cor
    self.ano = ano


carro1 = Carro(marca="Toyota", modelo="Corolla",cor="preto", ano=2020)

print(carro1.marca)