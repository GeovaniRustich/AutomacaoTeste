import fordev
from tkinter import *

def dados(text):
    print(text)

janela = Tk()
janela.title("Teste Geral")
janela.geometry('400x250')
input1 = Label(janela, text="Nome para cadastros: ")
input1.grid(column=0, row=2, padx=15, pady=5, sticky=NSEW)
entry1 = Entry(janela)
entry1.grid (column=1, row=2, padx=15, pady=5)

salvar = Button(janela, text="Salvar variaveis", command=lambda: dados(entry1.get()))
salvar.grid(column=0, row=6)

botao = Button(janela, text="Iniciar", command=janela.quit)
botao.grid(column=1, row=6)

botao = Button(janela, text="Cancelar", command=janela.destroy)
botao.grid(column=2, row=6)
janela.mainloop()

print()
