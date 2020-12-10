import funciones
from modelos.entidades import Persona
from modelos.entidades import Empleado
from servicios.seguridad.login import login
import servicios.logicanegocio as servicio

funciones.saludar("Ale")
funciones.despedir("Ale")

p=Persona("Ale", "Ramirez")
p=Empleado("Jesus", "Casanova", 1000)

if (login("luismi", "12345")):
    print("Bienvenido")

s=servicio.
