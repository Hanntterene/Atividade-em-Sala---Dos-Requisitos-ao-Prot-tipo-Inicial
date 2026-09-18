## - login feito com RA e senha
## - no cadastro podem ser colocadas até duas placas
## - login fica salvo no aplicativo não desconectando

import tkinter as tk
from tkinter import messagebox, ttk


def abrir_login(apos_login=None):
	usuarios = {}
	janela = tk.Tk()
	janela.title("Mapa de Vagas - Login")
	janela.geometry("420x500")
	janela.resizable(False, False)
	janela.configure(bg="#eef3f7")

	estilo = ttk.Style()
	estilo.theme_use("clam")
	estilo.configure("Titulo.TLabel", background="#176b87", foreground="white", font=("Segoe UI", 20, "bold"))
	estilo.configure("Subtitulo.TLabel", background="#176b87", foreground="#d9f1f7", font=("Segoe UI", 10))
	estilo.configure("Campo.TLabel", background="white", foreground="#243746", font=("Segoe UI", 10, "bold"))
	estilo.configure("Entrar.TButton", background="#176b87", foreground="white", font=("Segoe UI", 10, "bold"), padding=8)
	estilo.configure("Cadastro.TButton", background="white", foreground="#176b87", font=("Segoe UI", 10, "bold"), padding=8)

	cabecalho = tk.Frame(janela, bg="#176b87", height=120)
	cabecalho.pack(fill="x")
	cabecalho.pack_propagate(False)
	ttk.Label(cabecalho, text="Mapa de Vagas", style="Titulo.TLabel").pack(pady=(25, 2))
	ttk.Label(cabecalho, text="Entre para consultar as vagas do campus", style="Subtitulo.TLabel").pack()

	cartao = tk.Frame(janela, bg="white", padx=32, pady=24)
	cartao.pack(fill="both", expand=True, padx=24, pady=20)

	ttk.Label(cartao, text="RA", style="Campo.TLabel").pack(anchor="w")
	ra_entry = ttk.Entry(cartao, font=("Segoe UI", 11))
	ra_entry.pack(fill="x", pady=(6, 12), ipady=5)

	ttk.Label(cartao, text="Senha", style="Campo.TLabel").pack(anchor="w")
	senha_entry = ttk.Entry(cartao, show="*", font=("Segoe UI", 11))
	senha_entry.pack(fill="x", pady=(6, 12), ipady=5)

	lembrar_var = tk.BooleanVar(value=True)
	tk.Checkbutton(cartao, text="Manter meu login salvo", variable=lembrar_var).pack(anchor="w", pady=(0, 12))

	def validar_login():
		ra = ra_entry.get().strip()
		senha = senha_entry.get()

		if not ra or not senha:
			messagebox.showwarning("Atenção", "Informe o RA e a senha.")
			ra_entry.focus()
			return

		if ra not in usuarios or usuarios[ra]["senha"] != senha:
			messagebox.showwarning("Atenção", "RA ou senha incorretos. Faça seu cadastro primeiro.")
			ra_entry.focus()
			return

		janela.destroy()
		if apos_login:
			apos_login(ra, usuarios[ra]["placas"])

	def abrir_cadastro():
		cadastro = tk.Toplevel(janela)
		cadastro.title("Cadastro - Mapa de Vagas")
		cadastro.geometry("420x470")
		cadastro.resizable(False, False)
		cadastro.configure(bg="#eef3f7")

		cabecalho_cadastro = tk.Frame(cadastro, bg="#176b87", height=100)
		cabecalho_cadastro.pack(fill="x")
		cabecalho_cadastro.pack_propagate(False)
		ttk.Label(cabecalho_cadastro, text="Criar cadastro", style="Titulo.TLabel").pack(pady=(20, 2))
		ttk.Label(cabecalho_cadastro, text="Cadastre suas placas para acessar o mapa", style="Subtitulo.TLabel").pack()

		formulario = tk.Frame(cadastro, bg="white", padx=32, pady=20)
		formulario.pack(fill="both", expand=True, padx=24, pady=18)

		campos = []
		for texto, ocultar in (("RA", False), ("Senha", True), ("Placa principal", False), ("Segunda placa (opcional)", False)):
			ttk.Label(formulario, text=texto, style="Campo.TLabel").pack(anchor="w")
			campo = ttk.Entry(formulario, show="*" if ocultar else "", font=("Segoe UI", 11))
			campo.pack(fill="x", pady=(5, 10), ipady=4)
			campos.append(campo)

		def salvar_cadastro():
			novo_ra, nova_senha = campos[0].get().strip(), campos[1].get()
			placas = [campo.get().strip().upper() for campo in campos[2:] if campo.get().strip()]
			if not novo_ra or not nova_senha or not placas:
				messagebox.showwarning("Atenção", "Preencha o RA, a senha e pelo menos uma placa.", parent=cadastro)
				return
			if len(nova_senha) < 4:
				messagebox.showwarning("Atenção", "A senha deve ter pelo menos 4 caracteres.", parent=cadastro)
				return
			usuarios[novo_ra] = {"senha": nova_senha, "placas": placas}
			ra_entry.delete(0, tk.END)
			ra_entry.insert(0, novo_ra)
			senha_entry.delete(0, tk.END)
			messagebox.showinfo("Cadastro concluído", "Cadastro realizado. Agora entre com seu RA e senha.", parent=cadastro)
			cadastro.destroy()
			ra_entry.focus()

		ttk.Button(formulario, text="SALVAR CADASTRO", style="Entrar.TButton", command=salvar_cadastro).pack(fill="x", pady=(4, 0))

	ttk.Button(cartao, text="ENTRAR", style="Entrar.TButton", command=validar_login).pack(fill="x")
	ttk.Button(cartao, text="NÃO POSSUO CADASTRO", style="Cadastro.TButton", command=abrir_cadastro).pack(fill="x", pady=(8, 0))
	ra_entry.focus()
	janela.bind("<Return>", lambda evento: validar_login())
	janela.mainloop()


if __name__ == "__main__":
	abrir_login()
