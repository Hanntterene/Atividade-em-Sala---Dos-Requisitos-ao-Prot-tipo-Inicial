from login import abrir_login
from VisuaMapaVagas import abrir_mapa



def iniciar_prototipo():

	def mostrar_mapa(usuario, placas):
		abrir_mapa(usuario, placas)

	abrir_login(mostrar_mapa)


if __name__ == "__main__":
	iniciar_prototipo()
