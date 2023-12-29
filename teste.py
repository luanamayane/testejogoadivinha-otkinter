from tkinter import *
import random


class JogoAdivinhacao:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo de Adivinhação")

        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0

        self.lbl_instrucao = Label(master, text="Tente adivinhar o número secreto (entre 1 e 100):")
        self.lbl_instrucao.pack()

        self.entry_tentativa = Entry(master, width=20)
        self.entry_tentativa.pack()

        self.btn_adivinhar = Button(master, text="Adivinhar", command=self.adivinhar)
        self.btn_adivinhar.pack()

        self.lbl_resultado = Label(master, text="")
        self.lbl_resultado.pack()

    def adivinhar(self):
        tentativa = int(self.entry_tentativa.get())
        self.tentativas += 1

        if tentativa == self.numero_secreto:
            self.lbl_resultado.config(text=f"Parabéns! Você acertou o número secreto em {self.tentativas} tentativas!")
        elif tentativa > self.numero_secreto:
            self.lbl_resultado.config(text="Tente um número menor.")
        else:
            self.lbl_resultado.config(text="Tente um número maior.")


root = Tk()
jogo = JogoAdivinhacao(root)
root.mainloop()
