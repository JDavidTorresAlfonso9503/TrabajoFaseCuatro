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
class Servicio(Entidad):
 #Crea la clase Servicio, que hereda de Entidad
 def __init__(self, id_servicio, nombre, precio_base, disponible=True):
  #Inicializa los datos principales del servicio.
  super().__init__(id_servicio, nombre)
  #Hereda el identificador y el nombre de la clase Entidad.
  self._precio_base = precio_base
  #Guarda el precio base del servicio.
  self._disponible = disponible
  #Indica si el servicio esta disponible.

@property
def disponible(self):
 return self._disponible
#Permite consultar si el servicio esta disponible.

@disponible.setter
def disponible(self, valor):
 self._disponible = valor
 #permite modificar el estado de la disponibilidad.

@abstractmethod
    def calcular_costo(self, duracion=1, impuesto=None, descuento=None):
        pass
 #Define un metodo abstracto que las clases hijas deben implementar.

@abstractmethod
    def validar(self):
        pass
 #Obliga a las clases hijas a crear sus propias validaciones.
     
 def calcular_costo_con_opciones(self, duracion=1, impuesto=0, descuento=0):
 #Crea un metodo general para calcular el costo del servicio.
        base = self._precio_base * duracion
  #Multiplica el precio base por la duracion.
        total = base + (base * impuesto / 100) - descuento
  #Calcula el valor total aplicando impuesto y descuento.
        return max(total, 0)   
  #Devuelve el resueltado y evita que sea negativo.
class ReservaSala(Servicio):
#Crea la clase ReservaSala, que hereda de Servicio.
    def __init__(self, id_servicio, nombre, precio_base, capacidad, disponible=True):
  #Recibe los datos necesarios para crear una reserva de la sala.
        super().__init__(id_servicio, nombre, precio_base, disponible)
  #Hereda los atributos de la clase Servicio.
        self.capacidad = capacidad
  #Guarda la capacidad de la sala.
        self.validar()
  #Ejecuta las validaciones de la sala.
 
def validar(self):
#Define las conndiones para validar la sala.
        if self._precio_base <= 0:
         #Comprueba que el precio sea mayor que cero.
            raise DatosInvalidosError("Precio base de sala debe ser > 0")
         #Genera un error si el precio no es valido.
        if self.capacidad <= 0:
         #Comprueba que la capacidad sea mayor que cero.
            raise DatosInvalidosError("Capacidad de sala debe ser > 0")
         #Genera un eror si la capacidad no es valida.

def calcular_costo(self, duracion=1, impuesto=None, descuento=None):
 #Define como se calcula el costo de reservar una sala.
        imp = impuesto if impuesto is not None else 19
        desc = descuento if descuento is not None else 0
        return self.calcular_costo_con_opciones(duracion, imp, desc)

def describir(self):
        return f"Sala [{self.id}] {self.nombre} | Capacidad: {self.capacidad} | Precio/hora: ${self._precio_base} | Disponible: {self._disponible}"

class AlquilerEquipo(Servicio):
    def __init__(self, id_servicio, nombre, precio_base, cantidad_stock, disponible=True):
        super().__init__(id_servicio, nombre, precio_base, disponible)
        self.cantidad_stock = cantidad_stock
        self.validar()

    def validar(self):
        if self._precio_base <= 0:
            raise DatosInvalidosError("Precio base de equipo debe ser > 0")
        if self.cantidad_stock < 0:
            raise DatosInvalidosError("Stock no puede ser negativo")
 
  def calcular_costo(self, duracion=1, impuesto=None, descuento=None):
        imp = impuesto if impuesto is not None else 19
        desc = descuento if descuento is not None else 0
        if duracion >= 5:
            desc += self._precio_base * duracion * 0.10
        return self.calcular_costo_con_opciones(duracion, imp, desc)

    def describir(self):
        return f"Equipo [{self.id}] {self.nombre} | Stock: {self.cantidad_stock} | Precio/día: ${self._precio_base} | Disponible: {self._disponible}"

class AsesoriaEspecializada(Servicio):
    def __init__(self, id_servicio, nombre, precio_base, especialista, disponible=True):
        super().__init__(id_servicio, nombre, precio_base, disponible)
        self.especialista = especialista
        self.validar()
     
 def validar(self):
        if self._precio_base <= 0:
            raise DatosInvalidosError("Precio base de asesoría debe ser > 0")
        if not self.especialista or len(self.especialista.strip()) < 3:
            raise DatosInvalidosError("Especialista inválido")

   def calcular_costo(self, duracion=1, impuesto=None, descuento=None):
        imp = impuesto if impuesto is not None else 19
        desc = descuento if descuento is not None else 0
        return self.calcular_costo_con_opciones(duracion, imp, desc)

    def describir(self):
        return f"Asesoría [{self.id}] {self.nombre} | Especialista: {self.especialista} | Precio/hora: ${self._precio_base} | Disponible: {self._disponible}"

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

