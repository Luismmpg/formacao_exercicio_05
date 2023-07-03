import tkinter as tk
from tkinter import messagebox
import csv
import matplotlib.pyplot as plt

# Função para ler dados do arquivo CSV
def ler_dados_csv(caminho_ficheiro):
    with open(caminho_ficheiro, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

# Função para botão que executa o algoritmo 1
def clique_botao_algoritmo_01():
    resultado_text.delete("1.0", tk.END)
    messagebox.showinfo(
        "Algorimo de Ordenação", "Escolheu o Algoritmo de Ordenação Bubble Sort"
    )
    n = len(produtos_quantidades)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if produtos_quantidades[j][1] > produtos_quantidades[j + 1][1]:
                produtos_quantidades[j], produtos_quantidades[j + 1] = (
                    produtos_quantidades[j + 1],
                    produtos_quantidades[j],
                )

    for produto, quantidade in produtos_quantidades:
        resultado_text.insert(
            tk.END, f"Artigo: {produto}\nQuantidade Vendida: {quantidade}\n\n"
        )

    produtos = [produto for produto, _ in produtos_quantidades]
    quantidades = [quantidade for _, quantidade in produtos_quantidades]

    plt.bar(produtos, quantidades)
    plt.xlabel("Produtos")
    plt.ylabel("Quantidade Vendida")
    plt.title("Quantidade Vendida por Produto - Bubble Sort")
    plt.xticks(rotation=45)
    plt.show()
    
# Função para botão que executa o algoritmo 2
def clique_botao_algoritmo_02():
    resultado_text.delete("1.0", tk.END)
    messagebox.showinfo(
        "Algoritmo de Ordenação", "Escolheu o Algoritmo de Ordenação Quick Sort."
    )

    def quicksort(produtos_quantidades):
        if len(produtos_quantidades) <= 1:
            return produtos_quantidades
        else:
            # pivot = produtos_quantidades[len(produtos_quantidades) // 2]
            pivot = produtos_quantidades[0][1]
            menor = [
                produto for produto in produtos_quantidades[1:] if produto[1] <= pivot
            ]
            # middle = [x for x in produtos_quantidades if x == pivot]
            maior = [
                produto for produto in produtos_quantidades[1:] if produto[1] > pivot
            ]
            return quicksort(menor) + [produtos_quantidades[0]] + quicksort(maior)
  
    for produto, quantidade in produtos_quantidades:
        resultado_text.insert(
            tk.END, f"Artigo: {produto}\nQuantidade Vendida: {quantidade}\n\n"
        )
    produtos = [produto for produto, _ in produtos_quantidades]
    quantidades = [quantidade for _, quantidade in produtos_quantidades]

    plt.bar(produtos, quantidades)
    plt.xlabel("Produtos")
    plt.ylabel("Quantidade Vendida")
    plt.title("Quantidade Vendida por Produto - Quick Sort")
    plt.xticks(rotation=45)
    plt.show()
    
# Função para botão de saída da aplicação / clicar em "Não" apenas para apagar conteúdo da caixa de texto
def clique_botao_sair():
    resposta = messagebox.askyesno(
        "Sair da Aplicação",
        "Tem certeza que deseja sair?",
    )
    if resposta:
        menu.destroy()
    else:
        resultado_text.delete("1.0", tk.END)        
        
dados = ler_dados_csv(
    "C:/Users/luis.goncalves/OneDrive - SAMSIC/_Privado/2023 - Fundamentos de Python/formacao_exercicios/AtividadePedagogica4_10793_02.csv"
)

# Quando passar para o GitHub, usar esta variável
# dados = ler_dados_csv("AtividadePedagogica4_10793_02.csv")        

# Soma das quantidades vendidas de cada produto
soma_quantidade_vendida = {}
for produto in dados:
    nome_produto = produto["produto"]
    quantidade_vendida = int(produto["quantidade_vendida"])
    if nome_produto in soma_quantidade_vendida:
        soma_quantidade_vendida[nome_produto] += quantidade_vendida
    else:
        soma_quantidade_vendida[nome_produto] = quantidade_vendida

produtos_quantidades = [
    (produto, soma_quantidade_vendida[produto]) for produto in soma_quantidade_vendida
]

# Construção da interface
menu = tk.Tk()
menu.title("Consulta de Dados Ordenados")
titulo = tk.Label(menu, text="Escolha o tipo de ordenção pretendida.")
titulo.place(x=200, y=30)

# Centrar a janela do tkinter no ecrã
w = 600
h = 550
screen_width = menu.winfo_screenwidth()
screen_height = menu.winfo_screenheight()
x = (screen_width / 2) - (w / 2)
y = (screen_height / 2) - (h / 2)
menu.geometry("%dx%d+%d+%d" % (w, h, x, y))

# Campo de apresentação de resultados
resultado_text = tk.Text(menu, width=50, height=16)
resultado_text.pack()
resultado_text.place(x=100, y=60)

# Botão de Ordenação Bubble Sort
botao_01 = tk.Button(
    menu,
    text="Ordenação Bubble Sort",
    height=3,
    width=25,
    command=clique_botao_algoritmo_01,
)
botao_01.place(x=210, y=350)

# Botão de Ordenação Quick Sort
botao_02 = tk.Button(
    menu,
    text="Ordenação Quick Sort",
    height=3,
    width=25,
    command=clique_botao_algoritmo_02,
)
botao_02.place(x=210, y=450)

# Botão de saída da aplicação
botao_03 = tk.Button(menu, text="Sair", height=3, width=8, command=clique_botao_sair)
botao_03.place(x=440, y=450)

menu.mainloop()