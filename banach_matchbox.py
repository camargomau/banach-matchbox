import math
from utilities import *

def matchbox(n, k):
	return math.comb(2*n-k, n) * (1/2)**(2*n-k)

if __name__ == "__main__":
	clear_screen()

	print("La Caja de Cerillos de Banach\n\n"
		"Suponga que un matemático lleva siempre dos cajas de cerillos: una en "
		"el bolsillo izquierdo y otra en el derecho. Cada vez que necesita un "
		"cerillo, es igual de probable que lo tome de cualquiera de los dos "
		"bolsillos. Suponga que el matemático mete la mano en el bolsillo y "
		"descubre por primera vez que la caja que eligió está vacía.\n\nSuponga "
		"que cada una de las cajas contenía originalmente n cerillos, ¿cuál es "
		"la probabilidad de que haya exactamente k cerillos en la otra caja?\n")

	total = input_integer("• ¿Cuántos cerillos contienen las cajas (n)? ")
	remaining = input_integer("• ¿Cuántos cerillos quedan en la otra caja (k)? ")

	while remaining > total:
		remaining = input_integer(f"-> Introduzca un entero menor o igual que {total}: ")

	print(f"\nLa probabilidad de que en la caja no vacía queden {remaining} "
		f"cerillos es del: {round(matchbox(total, remaining)*100, 6)} %")
