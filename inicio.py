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
          
# Define el método que genera una descripción textual de la reserva.
    def describir(self):

        # Retorna una cadena con los datos principales de la reserva.
        # El costo se presenta con dos cifras decimales mediante el formato :.2f.
        return f"Reserva [{self.id}] Cliente: {self.cliente.nombre} | Servicio: {self.servicio.nombre} | Duración: {self.duracion} | Estado: {self.estado} | Costo: ${self.costo_total:.2f}"

    # Define el método encargado de ejecutar el proceso de confirmación de la reserva.
    def confirmar(self):

        # Inicia un bloque de control de excepciones para gestionar posibles errores.
        try:

            # Ejecuta las validaciones de duración y disponibilidad del servicio.
            self.validar()

            # Calcula el costo total utilizando el método del servicio y la duración solicitada.
            self.costo_total = self.servicio.calcular_costo(self.duracion)

            # Actualiza el estado de la reserva a Confirmada.
            self.estado = "Confirmada"

            # Registra en el archivo o sistema de logs la confirmación de la reserva.
            registrar_log(f"Reserva {self.id} confirmada - Cliente {self.cliente.nombre} - ${self.costo_total:.2f}")

        # Captura los errores relacionados con una reserva inválida o un servicio no disponible.
        except (ReservaInvalidaError, ServicioNoDisponibleError) as e:

            # Cambia el estado de la reserva a Fallida cuando ocurre una excepción controlada.
            self.estado = "Fallida"

            # Registra el error ocurrido, indicando que se trata de un evento de error.
            registrar_log(f"Reserva {self.id} FALLIDA: {e}", es_error=True)

            # Genera una nueva excepción y conserva como causa el error original.
            raise ReservaInvalidaError(f"No se pudo confirmar reserva {self.id}") from e

        # Se ejecuta únicamente cuando el bloque try termina sin generar excepciones.
        else:

            # Muestra un mensaje de confirmación junto con la descripción completa de la reserva.
            print(f"✅ Reserva confirmada: {self.describir()}")

        # Se ejecuta siempre, independientemente de que el proceso termine correctamente o con error.
        finally:

            # Informa que el proceso de confirmación ha finalizado.
            print(f"   -> Proceso de confirmación finalizado para reserva {self.id}")

    # Define el método encargado de cancelar una reserva existente.
    def cancelar(self):

        # Inicia el bloque de control de excepciones para gestionar errores durante la cancelación.
        try:

            # Comprueba si la reserva ya se encuentra cancelada.
            if self.estado == "Cancelada":

                # Genera una excepción cuando se intenta cancelar una reserva previamente cancelada.
                raise ReservaInvalidaError("La reserva ya estaba cancelada")

            # Cambia el estado de la reserva a Cancelada.
            self.estado = "Cancelada"

            # Registra en el sistema de logs la cancelación realizada.
            registrar_log(f"Reserva {self.id} cancelada")

        # Captura los errores relacionados con la operación de cancelación.
        except ReservaInvalidaError as e:

            # Registra el error producido durante el intento de cancelación.
            registrar_log(f"Error al cancelar {self.id}: {e}", es_error=True)

            # Muestra una advertencia con la descripción del error.
            print(f"⚠️ {e}")

        # Se ejecuta cuando la cancelación termina sin generar excepciones.
        else:

            # Informa que la reserva fue cancelada correctamente.
            print(f"❌ Reserva {self.id} cancelada")

        # Se ejecuta siempre, independientemente del resultado de la cancelación.
        finally:

            # Informa que el proceso de cancelación ha terminado.
            print("   -> Proceso de cancelación terminado")

    # Define el método que ejecuta el flujo completo de procesamiento de una reserva.
    def procesar(self):

        # Inicia el bloque de control de excepciones del proceso.
        try:

            # Muestra los datos actuales de la reserva antes de iniciar su confirmación.
            print(f"\nProcesando {self.describir()}")

            # Invoca el método encargado de validar y confirmar la reserva.
            self.confirmar()

        # Captura las excepciones de tipo ReservaInvalidaError generadas durante el procesamiento.
        except ReservaInvalidaError as e:

            # Informa que ocurrió un error durante el procesamiento de la reserva.
            print(f"⚠️ Error al procesar: {e}")

            # Muestra la causa original de la excepción, si existe.
            print(f"Causa original: {e.__cause__}")

        # Se ejecuta cuando el procesamiento termina sin generar excepciones.
        else:

            # Informa que la reserva fue procesada correctamente.
            print("✔️ Procesada sin errores")

        # Se ejecuta siempre, incluso cuando se presenta un error durante el procesamiento.
        finally:

            # Informa la finalización del proceso y que el sistema continúa ejecutándose.
            print("✔️ Fin de procesar() - el sistema sigue vivo")


# Define la clase principal encargada de administrar clientes, servicios y reservas.
class SistemaFJ:

    # Constructor de la clase que inicializa las estructuras de almacenamiento del sistema.
    def __init__(self):

        # Crea una lista vacía para almacenar los clientes registrados.
        self.clientes = []

        # Crea una lista vacía para almacenar los servicios disponibles.
        self.servicios = []

        # Crea una lista vacía para almacenar las reservas generadas.
        self.reservas = []

    # Define el método para incorporar un nuevo cliente al sistema.
    def agregar_cliente(self, cliente):

        # Agrega el objeto cliente a la lista de clientes registrados.
        self.clientes.append(cliente)

        # Registra en el sistema de logs la incorporación del cliente.
        registrar_log(f"Cliente agregado: {cliente.nombre}")

        # Muestra un mensaje de confirmación junto con la descripción del cliente.
        print(f"✅ Cliente agregado: {cliente.describir()}")

    # Define el método para registrar un nuevo servicio en el sistema.
    def agregar_servicio(self, servicio):

        # Agrega el objeto servicio a la lista de servicios.
        self.servicios.append(servicio)

        # Registra en el sistema de logs la incorporación del servicio.
        registrar_log(f"Servicio agregado: {servicio.nombre}")

        # Muestra un mensaje de confirmación con la información del servicio.
        print(f"✅ Servicio agregado: {servicio.describir()}")

    # Define el método para crear y procesar una nueva reserva.
    def crear_reserva(self, id_reserva, cliente, servicio, duracion):

        # Crea una instancia de la clase Reserva con los datos recibidos.
        reserva = Reserva(id_reserva, cliente, servicio, duracion)

        # Almacena la nueva reserva en la lista general de reservas.
        self.reservas.append(reserva)

        # Ejecuta el procesamiento de la reserva, incluyendo su validación y confirmación.
        reserva.procesar()

        # Retorna el objeto reserva para permitir su consulta o utilización posterior.
        return reserva

    # Define el método encargado de mostrar la información de todos los registros del sistema.
    def mostrar_todo(self):

        # Imprime el encabezado correspondiente a la sección de clientes.
        print("\n===== CLIENTES =====")

        # Recorre todos los clientes almacenados en la lista.
        for c in self.clientes:

            # Muestra la descripción individual de cada cliente.
            print(c.describir())

        # Imprime el encabezado correspondiente a la sección de servicios.
        print("\n===== SERVICIOS =====")

        # Recorre todos los servicios registrados en el sistema.
        for s in self.servicios:

            # Muestra la descripción individual de cada servicio.
            print(s.describir())

        # Imprime el encabezado correspondiente a la sección de reservas.
        print("\n===== RESERVAS =====")

        # Recorre todas las reservas almacenadas en el sistema.
        for r in self.reservas:

            # Muestra la descripción individual de cada reserva.
            print(r.describir())

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

