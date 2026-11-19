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

# Declara la clase Reserva, que agrupa los datos y comportamientos de este componente.
class Reserva(Entidad):
 # Define el constructor e inicializa los atributos del objeto.
 def __init__(self, id_reserva, cliente, servicio, duracion):
  # Invoca el constructor de la clase padre para inicializar los atributos heredados.
  super().__init__(id_reserva, f"Reserva-{id_reserva}")
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self.cliente = cliente
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self.servicio = servicio
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self.duracion = duracion
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self.estado = "Pendiente"
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self.costo_total = 0

 # Define el método que comprueba que los datos cumplan las reglas establecidas.
 def validar(self):
  # Evalúa la condición para decidir si se ejecuta el bloque siguiente.
  if self.duracion <= 0:
   # Lanza una excepción para informar que se presentó una condición no válida.
   raise ReservaInvalidaError("Duración debe ser mayor a 0")
  # Evalúa la condición para decidir si se ejecuta el bloque siguiente.
  if not self.servicio.disponible:
   # Lanza una excepción para informar que se presentó una condición no válida.
   raise ServicioNoDisponibleError(f"Servicio {self.servicio.nombre} no está disponible")

 # Define el método que devuelve una descripción legible del objeto.
 def describir(self):
  # Devuelve el resultado de la operación o la información solicitada.
  return f"Reserva [{self.id}] Cliente: {self.cliente.nombre} | Servicio: {self.servicio.nombre} | Duración: {self.duracion} | Estado: {self.estado} | Costo: ${self.costo_total:.2f}"

 # Define el proceso de validación y confirmación de una reserva.
 def confirmar(self):
  # Inicia un bloque protegido para controlar posibles excepciones.
  try:
   # Ejecuta la instrucción indicada dentro del flujo del programa.
   self.validar()
   # Asigna o actualiza un atributo del objeto con el valor indicado.
   self.costo_total = self.servicio.calcular_costo(self.duracion)
   # Asigna o actualiza un atributo del objeto con el valor indicado.
   self.estado = "Confirmada"
   # Registra en el archivo de logs el evento o error producido.
   registrar_log(f"Reserva {self.id} confirmada - Cliente {self.cliente.nombre} - ${self.costo_total:.2f}")
  # Captura el tipo de excepción indicado para gestionar el error.
  except (ReservaInvalidaError, ServicioNoDisponibleError) as e:
   # Asigna o actualiza un atributo del objeto con el valor indicado.
   self.estado = "Fallida"
   # Registra en el archivo de logs el evento o error producido.
   registrar_log(f"Reserva {self.id} FALLIDA: {e}", es_error=True)
   # Lanza una excepción para informar que se presentó una condición no válida.
   raise ReservaInvalidaError(f"No se pudo confirmar reserva {self.id}") from e
  # Ejecuta este bloque únicamente si el bloque try finalizó sin excepciones.
  else:
   # Muestra en consola el mensaje o la información indicada.
   print(f" Reserva confirmada: {self.describir()}")
  # Ejecuta este bloque siempre, haya ocurrido o no una excepción.
  finally:
   # Muestra en consola el mensaje o la información indicada.
   print(f" -> Proceso de confirmación finalizado para reserva {self.id}")

 # Define el proceso para cancelar una reserva.
 def cancelar(self):
  # Inicia un bloque protegido para controlar posibles excepciones.
  try:
   # Evalúa la condición para decidir si se ejecuta el bloque siguiente.
   if self.estado == "Cancelada":
    # Lanza una excepción para informar que se presentó una condición no válida.
    raise ReservaInvalidaError("La reserva ya estaba cancelada")
   # Asigna o actualiza un atributo del objeto con el valor indicado.
   self.estado = "Cancelada"
   # Registra en el archivo de logs el evento o error producido.
   registrar_log(f"Reserva {self.id} cancelada")
  # Captura el tipo de excepción indicado para gestionar el error.
  except ReservaInvalidaError as e:
   # Registra en el archivo de logs el evento o error producido.
   registrar_log(f"Error al cancelar {self.id}: {e}", es_error=True)
   # Muestra en consola el mensaje o la información indicada.
   print(f" {e}")
  # Ejecuta este bloque únicamente si el bloque try finalizó sin excepciones.
  else:
   # Muestra en consola el mensaje o la información indicada.
   print(f" Reserva {self.id} cancelada")
  # Ejecuta este bloque siempre, haya ocurrido o no una excepción.
  finally:
   # Muestra en consola el mensaje o la información indicada.
   print(" -> Proceso de cancelación terminado")

 # Define el flujo que procesa una reserva y controla los posibles errores.
 def procesar(self):
  # Inicia un bloque protegido para controlar posibles excepciones.
  try:
   # Muestra en consola el mensaje o la información indicada.
   print(f"\nProcesando {self.describir()}")
   # Ejecuta la instrucción indicada dentro del flujo del programa.
   self.confirmar()
  # Captura el tipo de excepción indicado para gestionar el error.
  except ReservaInvalidaError as e:
   # Muestra en consola el mensaje o la información indicada.
   print(f" Error al procesar: {e}")
   # Muestra en consola el mensaje o la información indicada.
   print(f"Causa original: {e.__cause__}")
  # Ejecuta este bloque únicamente si el bloque try finalizó sin excepciones.
  else:
   # Muestra en consola el mensaje o la información indicada.
   print(" Procesada sin errores")
  # Ejecuta este bloque siempre, haya ocurrido o no una excepción.
  finally:
   # Muestra en consola el mensaje o la información indicada.
   print(" Fin de procesar() - el sistema sigue vivo")

# Declara la clase SistemaFJ, que agrupa los datos y comportamientos de este componente.
class SistemaFJ:
 # Define el constructor e inicializa los atributos del objeto.
 def __init__(self):
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self.clientes = []
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self.servicios = []
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self.reservas = []

 # Define la operación para registrar un cliente en el sistema.
 def agregar_cliente(self, cliente):
  # Agrega el elemento indicado al final de la lista correspondiente.
  self.clientes.append(cliente)
  # Registra en el archivo de logs el evento o error producido.
  registrar_log(f"Cliente agregado: {cliente.nombre}")
  # Muestra en consola el mensaje o la información indicada.
  print(f" Cliente agregado: {cliente.describir()}")

 # Define la operación para registrar un servicio en el sistema.
 def agregar_servicio(self, servicio):
  # Agrega el elemento indicado al final de la lista correspondiente.
  self.servicios.append(servicio)
  # Registra en el archivo de logs el evento o error producido.
  registrar_log(f"Servicio agregado: {servicio.nombre}")
  # Muestra en consola el mensaje o la información indicada.
  print(f" Servicio agregado: {servicio.describir()}")

 # Define la operación para crear, almacenar y procesar una reserva.
 def crear_reserva(self, id_reserva, cliente, servicio, duracion):
  # Calcula y asigna el valor correspondiente a la variable indicada.
  reserva = Reserva(id_reserva, cliente, servicio, duracion)
  # Agrega el elemento indicado al final de la lista correspondiente.
  self.reservas.append(reserva)
  # Ejecuta la instrucción indicada dentro del flujo del programa.
  reserva.procesar()
  # Devuelve el resultado de la operación o la información solicitada.
  return reserva

 # Define la operación que muestra los clientes, servicios y reservas registrados.
 def mostrar_todo(self):
  # Muestra en consola el mensaje o la información indicada.
  print("\n===== CLIENTES =====")
  # Recorre los elementos de la colección para procesarlos uno por uno.
  for c in self.clientes:
   # Muestra en consola el mensaje o la información indicada.
   print(c.describir())
  # Muestra en consola el mensaje o la información indicada.
  print("\n===== SERVICIOS =====")
  # Recorre los elementos de la colección para procesarlos uno por uno.
  for s in self.servicios:
   # Muestra en consola el mensaje o la información indicada.
   print(s.describir())
  # Muestra en consola el mensaje o la información indicada.
  print("\n===== RESERVAS =====")
  # Recorre los elementos de la colección para procesarlos uno por uno.
  for r in self.reservas:
   # Muestra en consola el mensaje o la información indicada.
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

