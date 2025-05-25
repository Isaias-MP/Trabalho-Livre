from models.usuario import Usuario
from models.transacao import Despesa, Receita
from utils.graficos import plotar_gastos_por_categoria
import os

def main():
    usuario = Usuario(input("Digite seu nome: "))
    os.makedirs("data", exist_ok=True)

    while True:
        print("\n" + "="*30)
        print("CONTROLE SEU FINANCEIRO".center(30))
        print("="*30)
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Ver Relatório")
        print("4. Ver Gráfico de Gastos")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_receita(usuario)
        elif opcao == "2":
            adicionar_despesa(usuario)
        elif opcao == "3":
            ver_relatorio(usuario)
        elif opcao == "4":
            ver_grafico(usuario)
        elif opcao == "5":
            usuario.salvar_em_json()
            print("Dados salvos. Até logo!")
            break
        else:
            print("Opção inválida!")

def adicionar_receita(usuario):
    print("\nNova Receita")
    valor = float(input("Valor: R$ "))
    descricao = input("Descrição: ")
    fonte = input("Fonte (ex: Salário, Freela): ")
    usuario.adicionar_transacao(Receita(valor, descricao, fonte))
    print("✅ Receita adicionada!")

def adicionar_despesa(usuario):
    print("\nNova Despesa")
    valor = float(input("Valor: R$ "))
    descricao = input("Descrição: ")
    categoria = input("Categoria (ex: Alimentação, Transporte): ")
    usuario.adicionar_transacao(Despesa(valor, descricao, categoria))
    print("✅ Despesa adicionada!")

def ver_relatorio(usuario):
    relatorio = usuario.gerar_relatorio()
    print("\n" + "="*30)
    print(f"Relatório de {usuario.nome}".center(30))
    print("="*30)
    print(f"Saldo Total: R$ {relatorio['saldo']:.2f}")
    print("\nTransações:")
    for t in relatorio["transacoes"]:
        tipo = "RECEITA" if t.valor > 0 else "DESPESA"
        print(f"- {tipo}: {t.descricao} (R$ {abs(t.valor):.2f})")

def ver_grafico(usuario):
    try:
        plotar_gastos_por_categoria(usuario)
    except:
        print("Erro ao gerar gráfico. Verifique se há despesas cadastradas.")

if __name__ == "__main__":
    main()