import matplotlib.pyplot as plt

def plotar_gastos_por_categoria(usuario):
    categorias = {}
    for t in usuario.transacoes:
        if hasattr(t, 'categoria'):
            categorias[t.categoria] = categorias.get(t.categoria, 0) + t.valor
    
    plt.bar(categorias.keys(), categorias.values())
    plt.title("Gastos por Categoria")
    plt.show()