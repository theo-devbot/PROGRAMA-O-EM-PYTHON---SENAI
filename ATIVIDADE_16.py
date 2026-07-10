import tkinter as tk

def enviar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()

    janela_resultado = tk.Toplevel()
    janela_resultado.title('Dados do Cliente')
    janela_resultado.geometry("400x200")

    tk.Label(janela_resultado, text="Dados Cadastrados", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(janela_resultado, text=f"Nome: {nome}", font=("Arial", 12)).pack()
    tk.Label(janela_resultado, text=f"Idade: {idade}", font=("Arial", 12)).pack()
    tk.Label(janela_resultado, text=f"E-mail: {email}", font=("Arial", 12)).pack()



janela = tk.Tk()
janela.title('Formulario Cliente')
janela.geometry('1700x750')

tk.Label(janela, text='Nome:', font=("Arial", 12)).pack(pady=(15, 2))
entry_nome = tk.Entry(janela, width=30)
entry_nome.pack()

tk.Label(janela, text="Idade:", font=("Arial", 12)).pack(pady=(5, 2))
entry_idade = tk.Entry(janela, width=30)
entry_idade.pack()

tk.Label(janela, text="E-mail:", font=("Arial", 12)).pack(pady=(5, 2))
entry_email = tk.Entry(janela, width=30)
entry_email.pack()

botao_enviar = tk.Button(janela, text="Enviar", command=enviar_dados, font=("Arial", 12))
botao_enviar.pack(pady=20)



janela.mainloop()