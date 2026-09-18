#- após fazer o login é mostrado um mapa do estacionamento
#- no mapa as vagas em verde são as livre e as vagas em vermelho são as ocupadas

import tkinter as tk
from tkinter import messagebox


def vagas_disponiveis():
	return ["A1", "A3", "B2", "B3", "C1", "C2", "C4", "D2", "D3"]


def vagas_restritas_funcionarios():
	return ["A4", "B4", "D1"]


def abrir_mapa(usuario, placas):
	janela = tk.Tk()
	janela.title("Mapa de Vagas - Estacionamento")
	janela.geometry("760x590")
	janela.minsize(650, 500)
	janela.configure(bg="#eef3f7")

	cabecalho = tk.Frame(janela, bg="#176b87", padx=24, pady=16)
	cabecalho.pack(fill="x")
	tk_label = tk.Label
	tk_label(cabecalho, text="Mapa do estacionamento", bg="#176b87", fg="white", font=("Segoe UI", 20, "bold")).pack(anchor="w")
	tk_label(cabecalho, text=f"Usuário: {usuario}  |  Placas: {', '.join(placas)}", bg="#176b87", fg="#d9f1f7", font=("Segoe UI", 10)).pack(anchor="w", pady=(4, 0))

	conteudo = tk.Frame(janela, bg="#eef3f7", padx=24, pady=20)
	conteudo.pack(fill="both", expand=True)

	legenda = tk.Frame(conteudo, bg="#eef3f7")
	legenda.pack(fill="x", pady=(0, 12))
	for cor, texto in (("#36a269", "Livre"), ("#d95c5c", "Ocupada"), ("#8b949e", "Restrita a funcionários")):
		tk.Label(legenda, text="  ", bg=cor).pack(side="left", padx=(0, 4))
		tk.Label(legenda, text=texto, bg="#eef3f7", fg="#344955", font=("Segoe UI", 10)).pack(side="left", padx=(0, 18))

	mapa = tk.Canvas(conteudo, bg="#d7dde2", highlightthickness=0)
	mapa.pack(fill="both", expand=True)

	vagas = [
		("A1", "livre"), ("A2", "ocupada"), ("A3", "livre"), ("A4", "restrita"),
		("B1", "ocupada"), ("B2", "livre"), ("B3", "livre"), ("B4", "restrita"),
		("C1", "livre"), ("C2", "livre"), ("C3", "ocupada"), ("C4", "livre"),
		("D1", "restrita"), ("D2", "livre"), ("D3", "livre"), ("D4", "ocupada"),
	]
	assert set(vagas_disponiveis()) == {nome for nome, situacao in vagas if situacao == "livre"}
	assert set(vagas_restritas_funcionarios()) == {nome for nome, situacao in vagas if situacao == "restrita"}
	cores = {"livre": "#36a269", "ocupada": "#d95c5c", "restrita": "#8b949e"}

	def desenhar_mapa(evento=None):
		mapa.delete("all")
		largura = max(mapa.winfo_width(), 500)
		altura = max(mapa.winfo_height(), 300)
		colunas = 4
		margem_x, margem_y, espacamento = 55, 30, 18
		box_largura = (largura - 2 * margem_x - (colunas - 1) * espacamento) / colunas
		box_altura = min(86, (altura - 2 * margem_y - 3 * espacamento) / 4)

		for indice, (nome, situacao) in enumerate(vagas):
			linha, coluna = divmod(indice, colunas)
			x1 = margem_x + coluna * (box_largura + espacamento)
			y1 = margem_y + linha * (box_altura + espacamento)
			x2, y2 = x1 + box_largura, y1 + box_altura
			mapa.create_rectangle(x1, y1, x2, y2, fill=cores[situacao], outline="white", width=2, tags=nome)
			mapa.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=nome, fill="white", font=("Segoe UI", 14, "bold"), tags=nome)

		mapa.create_text(largura / 2, altura - 15, text="Entrada principal", fill="#344955", font=("Segoe UI", 10, "bold"))

	def selecionar_vaga(evento):
		itens = mapa.find_withtag("current")
		if not itens:
			return
		nome = mapa.itemcget(itens[0], "text")
		for vaga, situacao in vagas:
			if vaga == nome:
				status = {"livre": "está livre", "ocupada": "está ocupada", "restrita": "é reservada para funcionários"}[situacao]
				messagebox.showinfo("Detalhes da vaga", f"A vaga {nome} {status}.", parent=janela)
				return

	mapa.bind("<Configure>", desenhar_mapa)
	mapa.bind("<Button-1>", selecionar_vaga)
	desenhar_mapa()
	janela.mainloop()


if __name__ == "__main__":
	abrir_mapa("visitante", ["ABC1D23"])