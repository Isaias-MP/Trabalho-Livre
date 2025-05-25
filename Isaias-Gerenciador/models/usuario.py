import json
from typing import List
from models.transacao import Transacao

class Usuario:
    def __init__(self, nome: str):
        self.nome = nome
        self._transacoes: List[Transacao] = []

    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append(transacao)

    def gerar_relatorio(self) -> dict:
        return {
            "saldo": sum(t.calcular_impacto() for t in self._transacoes),
            "transacoes": self._transacoes
        }

    def salvar_em_json(self, arquivo: str = "data/transacoes.json"):
        with open(arquivo, 'w') as f:
            json.dump([t.__dict__ for t in self._transacoes], f, indent=4)

    @property
    def transacoes(self):
        return self._transacoes
