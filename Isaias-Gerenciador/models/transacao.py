from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor = valor
        self.descricao = descricao
        self.data = datetime.now().strftime("%d/%m/%Y")

    @abstractmethod
    def calcular_impacto(self) -> float:
        pass

class Despesa(Transacao):
    def __init__(self, valor: float, descricao: str, categoria: str):
        super().__init__(valor, descricao)
        self.categoria = categoria

    def calcular_impacto(self) -> float:
        return -self.valor

class Receita(Transacao):
    def __init__(self, valor: float, descricao: str, fonte: str):
        super().__init__(valor, descricao)
        self.fonte = fonte

    def calcular_impacto(self) -> float:
        return self.valor