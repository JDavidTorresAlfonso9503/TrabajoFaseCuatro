print("Bienvenidos al Curso de Programación")
print("UNAD")
print("Fase4")
print("Juan David Torres Alfonso")
print("Katerin Dayanna Gil Espinosa")
print("Maria Fernanda Contreras Segura")
print("Katerin Daniela Castro Rojas")
# ============================================================
# SOFTWARE FJ - Sistema Integral de Gestión de Clientes,
# Servicios y Reservas
# Fase 4 - Programación 213023 - UNAD
# Grupo de 4 integrantes - Trabajo colaborativo
# ============================================================
# INTEGRANTES:
# 1. Juan David Torres
# 2. Katerin Dayanna Gil
# 3. Maria Fernanda Contreras
# 4. Katherin Rojas
# ============================================================
from abc import ABC, abstractmethod
from datetime import datetime
import traceback

ARCHIVO_LOGS = "logs_sistema.txt"

# ======================================================================
# ======================================================================
# INTEGRANTE 1: Juan David Torres Alfonso
# PARTE QUE LE TOCA:
# - Función de registro de logs
# - Excepciones personalizadas
# - Clase abstracta general Entidad
# - Clase Cliente con encapsulación y validaciones
# JUAN DAVID TORRES ALFONSO
# ======================================================================
# ======================================================================


# ======================================================================
# ======================================================================
# INTEGRANTE 2: Katerin Dayanna Gil
# PARTE QUE LE TOCA:
# - Clase abstracta Servicio
# - 3 servicios especializados que heredan: ReservaSala, AlquilerEquipo, AsesoriaEspecializada
# - Polimorfismo y métodos sobrecargados calcular_costo()
# KATERIN DAYANNA
# ======================================================================
# ======================================================================



# ======================================================================
# ======================================================================
# INTEGRANTE 3: Maria Fernanda Contreras
# PARTE QUE LE TOCA:
# - Clase Reserva (cliente + servicio + duración + estado)
# - Métodos confirmar(), cancelar(), procesar()
# - Clase SistemaFJ que maneja las listas internas
# MARIA FERNANDA
# ======================================================================
# ======================================================================

# Define la clase Reserva, que hereda los atributos y métodos de Entidad.
class Reserva(Entidad):

    # Constructor de la clase: recibe el identificador, cliente, servicio y duración de la reserva.
    def __init__(self, id_reserva, cliente, servicio, duracion):

        # Invoca el constructor de la clase padre Entidad e inicializa el identificador y nombre de la reserva.
        super().__init__(id_reserva, f"Reserva-{id_reserva}")

        # Almacena el objeto cliente asociado a la reserva.
        self.cliente = cliente

        # Almacena el objeto servicio que se desea reservar.
        self.servicio = servicio

        # Guarda la duración solicitada para la prestación del servicio.
        self.duracion = duracion

        # Establece el estado inicial de la reserva como Pendiente.
        self.estado = "Pendiente"

        # Inicializa el costo total de la reserva en cero.
        self.costo_total = 0

    # Define el método encargado de verificar las condiciones de validez de la reserva.
    def validar(self):

        # Comprueba que la duración de la reserva sea mayor que cero.
        if self.duracion <= 0:

            # Genera una excepción personalizada cuando la duración no es válida.
            raise ReservaInvalidaError("Duración debe ser mayor a 0")

        # Comprueba si el servicio seleccionado se encuentra disponible.
        if not self.servicio.disponible:

            # Genera una excepción personalizada cuando el servicio no está disponible.
            raise ServicioNoDisponibleError(f"Servicio {self.servicio.nombre} no está disponible")
          

# ======================================================================
# ======================================================================
# INTEGRANTE 4: Katherin Rojas
# PARTE QUE LE TOCA:
# - Simulación de las 10 operaciones (válidas e inválidas)
# - Menú en consola
# - Función main() y ejecución del programa
# - Verificación de que el sistema nunca se cae y prueba del logs
# KATHERIN, 
# ======================================================================
# ======================================================================

