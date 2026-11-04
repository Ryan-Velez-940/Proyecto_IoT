# Ryan X. Velez Negron y Axel Algarin Diaz
# Proyecto_Internet_Of_Things_EstaLibre

from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23, max_distance=2)

while True:
    cm = sensor.distance * 100
    estado = "Ocupado" if cm < 50 else "Disponible"
    print(f"{estado} ({cm:.0f} cm)")
    sleep(1)
