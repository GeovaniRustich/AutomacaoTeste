import fordev
from tkinter import *

    
janela = Tk()
janela.title("Teste Geral")
janela.geometry('400x250')
input1 = Label(janela, text="Nome para cadastros: ")
input1.grid(column=0, row=2, padx=12, pady=5, sticky=NSEW)
entry1 = Entry(janela)
entry1.grid (column=1, row=2, padx=12, pady=5)

input2 = Label(janela, text="Código para o Centro de Custo: ")
input2.grid(column=0, row=3, padx=12, pady=5, sticky=NSEW)
entry2 = Entry(janela)
entry2.grid(column=1, row=3, padx=12, pady=5)

input3 = Label(janela, text="Fórmula Sistema de Avaliação: ")
input3.grid(column=0, row=4, padx=12, pady=5, sticky=NSEW)
entry3 = Entry(janela)
entry3.grid(column=1, row=4, padx=12, pady=5)

input4 = Label(janela, text="E-mail principal do aluno: ")
input4.grid(column=0, row=5, padx=12, pady=5, sticky=NSEW)
entry4 = Entry(janela)
entry4.grid(column=1, row=5, padx=12, pady=5)


botao = Button(janela, text="Iniciar", command= janela.quit)
botao.grid(column=0, row=7)

botao = Button(janela, text="Cancelar", command=janela.destroy)
botao.grid(column=0, row=8)
janela.mainloop()

nomeCadastro = entry1.get()
centroCusto = entry2.get()
formula = entry3.get()
emailPrincipal = entry4.get()

print(nomeCadastro, centroCusto, formula, emailPrincipal)
