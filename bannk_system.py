import tkinter as tk
from tkinter import messagebox
from tkinter import messagebox, simpledialog

class BankSystem:
    def __init__(self, root):
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

        self.root = root
        self.root.title("Sistema Bancário")
        
        self.create_widgets()

    def create_widgets(self):
        self.deposit_button = tk.Button(self.root, text="Depositar", command=self.depositar)
        self.deposit_button.pack(pady=10)
        
        self.withdraw_button = tk.Button(self.root, text="Sacar", command=self.sacar)
        self.withdraw_button.pack(pady=10)
        
        self.extrato_button = tk.Button(self.root, text="Extrato", command=self.ver_extrato)
        self.extrato_button.pack(pady=10)
        
        self.exit_button = tk.Button(self.root, text="Sair", command=self.root.quit)
        self.exit_button.pack(pady=10)
        
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def depositar(self):
        valor = self.get_value("Informe o valor do depósito:")
        if valor is not None:
            if valor > 0:
                self.saldo += valor
                self.extrato += f"Depósito: R$ {valor:.2f}\n"
                self.result_label.config(text="Depósito realizado com sucesso")
            else:
                self.result_label.config(text="Operação falhou! O valor informado é inválido.")

    def sacar(self):
        valor = self.get_value("Informe o valor do saque:")
        if valor is not None:
            excedeu_saldo = valor > self.saldo
            excedeu_limite = valor > self.limite
            excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

            if excedeu_saldo:
                self.result_label.config(text="Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                self.result_label.config(text="Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                self.result_label.config(text="Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                self.saldo -= valor
                self.extrato += f"Saque: R$ {valor:.2f}\n"
                self.numero_saques += 1
                self.result_label.config(text="Saque realizado com sucesso")
            else:
                self.result_label.config(text="Operação falhou! O valor informado é inválido.")

    def ver_extrato(self):
        extrato_msg = "Não foram realizadas movimentações." if not self.extrato else self.extrato
        extrato_msg += f"\nSaldo: R$ {self.saldo:.2f}"
        messagebox.showinfo("Extrato", extrato_msg)

    def get_value(self, prompt):
        value = tk.simpledialog.askfloat("Entrada", prompt)
        return value

if __name__ == "__main__":
    root = tk.Tk()
    app = BankSystem(root)
    root.mainloop()
