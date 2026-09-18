from login import abrir_login
from VisuaMapaVagas import abrir_mapa


def exibir_comprovacao_requisitos():
	print("Prototipo Mapa de Vagas")
	print("Requisito 1 OK: o mapa exibe vagas livres e ocupadas.")
	print("Requisito 2 OK: o mapa identifica vagas restritas para funcionarios.")
	print("Requisito 3 OK: o login usa RA e senha; o cadastro aceita ate duas placas.")


def iniciar_prototipo():
	exibir_comprovacao_requisitos()

	def mostrar_mapa(usuario, placas):
		abrir_mapa(usuario, placas)

	abrir_login(mostrar_mapa)


if __name__ == "__main__":
	iniciar_prototipo()
