# programa cachipun
"""
Actividad 2 Se pide crear el programa cachipun.py, donde el usuario entregará como
argumento: piedra, papel o tijera. Para que el computador pueda jugar escogerá un
valor al azar. Para eso se solicita investigar random.choice() de la librería random.
"""
import random

opciones_juego = ["piedra", "papel", "tijera"]

# juego del usuario
jugador = input("Ingrese su eleccion: piedra , papel o tijera : ")

#validaciones
if jugador != "piedra" and jugador != "papel" and jugador != "tijera":
  print("Opcion no valida, Ingrese nuevo juego")
  jugador = input("Ingrese su eleccion: piedra , papel o tijera : ")
  
# juego del computador
computadora = random.choice(opciones_juego)
input(f"el computador jugó: {computadora}")

# comparaciones
if jugador == computadora:
  print("Empate")
elif jugador == "piedra" and computadora == "tijera" or jugador == "papel" and computadora == "piedra" or jugador == "tijera" and computadora == "papel":
  print("Ganaste")
else:
  print("Perdiste")