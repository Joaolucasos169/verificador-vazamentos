import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import ttk
from backend import verificador

def verificar():
    entrada = entrada_texto.get()
    tipo = tipo_var.get()
    salvar = salvar_var.get()
    
    if tipo == "senha":
        resultado = verificador.verificar_senha(entrada)
    else:
        resultado = verificador.verificar_email(entrada)
        
    resultado_label.config(text=resultado)
    
    if salvar:
        sucesso = verificador.salvar_resultado(resultado)
        if sucesso:
            resultado_label.config(text=resultado + "\n✅ Resultado salvo")
        else:
            resultado_label.config(text=resultado + "\n⚠️ Erro ao salvar.")
            
janela = tk.Tk()
janela.title("Verificador de Vazamentos")
janela.geometry("450x300")
janela.resizable(False, False)

tk.Label(janela, text="Digite seu e-mail ou senha:").pack(pady=5)
entrada_texto = tk.Entry(janela, width=40)
entrada_texto.pack(pady=5)

tipo_var = tk.StringVar(value="email")
tk.Radiobutton(janela, text="Verificar e-mail", variable=tipo_var, value="email").pack()
tk.Radiobutton(janela, text="Verificar senha", variable=tipo_var, value="senha").pack()

salvar_var = tk.BooleanVar()
tk.Checkbutton(janela, text="Salvar resultado em arquivo", variable=salvar_var).pack(pady=5)

tk.Button(janela, text="Verificar", command=verificar).pack(pady=10)

resultado_label = tk.Label(janela, text="", wraplength=400, justify="left", fg="blue")
resultado_label.pack(pady=10)

janela.mainloop()

