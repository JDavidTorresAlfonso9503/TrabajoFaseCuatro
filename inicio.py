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
# Define la función que registra eventos y errores en el archivo de logs.
def registrar_log(mensaje, es_error=False):
 # Ejecuta la instrucción indicada dentro del flujo del programa.
 """Guarda todo en logs_sistema.txt y no deja que el programa se caiga"""
 # Inicia un bloque protegido para controlar posibles excepciones.
 try:
  # Obtiene la fecha y hora actuales con el formato establecido.
  hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  # Determina si el registro corresponde a un error o a un evento normal.
  tipo = "ERROR" if es_error else "EVENTO"
  # Construye la línea de texto que se guardará en el archivo de logs.
  linea = f"[{hora}] [{tipo}] {mensaje}\n"
  # Abre el archivo indicado y garantiza su cierre al terminar el bloque.
  with open(ARCHIVO_LOGS, "a", encoding="utf-8") as f:
   # Escribe el registro construido en el archivo de logs.
   f.write(linea)
 # Captura el tipo de excepción indicado para gestionar el error.
 except Exception as e:
  # Muestra en consola el mensaje o la información indicada.
  print(f"No se pudo escribir en logs: {e}")
  # --- Excepciones personalizadas - Juan David Torres ---
# Declara la clase DatosInvalidosError, que agrupa los datos y comportamientos de este componente.
class DatosInvalidosError(Exception):
 # Indica un bloque vacío; se utiliza como implementación provisional de este método.
 pass

# Declara la clase ServicioNoDisponibleError, que agrupa los datos y comportamientos de este componente.
class ServicioNoDisponibleError(Exception):
 # Indica un bloque vacío; se utiliza como implementación provisional de este método.
 pass

# Declara la clase ReservaInvalidaError, que agrupa los datos y comportamientos de este componente.
class ReservaInvalidaError(Exception):
 # Indica un bloque vacío; se utiliza como implementación provisional de este método.
 pass

# Declara la clase ClienteInvalidoError, que agrupa los datos y comportamientos de este componente.
class ClienteInvalidoError(DatosInvalidosError):
 # Indica un bloque vacío; se utiliza como implementación provisional de este método.
 pass
 # --- Clase Cliente - Juan David Torres ---
# Declara la clase Cliente, que agrupa los datos y comportamientos de este componente.
class Cliente(Entidad):
 # Define el constructor e inicializa los atributos del objeto.
 def __init__(self, id_cliente, nombre, correo, telefono, documento):
  # Invoca el constructor de la clase padre para inicializar los atributos heredados.
  super().__init__(id_cliente, nombre)
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self.__correo = correo
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self.__telefono = telefono
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self.__documento = documento
  # Ejecuta la instrucción indicada dentro del flujo del programa.
  self.validar()

 # Indica que el método siguiente permite consultar un atributo mediante una propiedad.
 @property
 # Define el método correo de la clase o módulo correspondiente.
 def correo(self):
  # Devuelve el resultado de la operación o la información solicitada.
  return self.__correo

 # Indica que el método siguiente establece o modifica el valor de la propiedad.
 @correo.setter
 # Define el método correo de la clase o módulo correspondiente.
 def correo(self, nuevo):
  # Evalúa la condición para decidir si se ejecuta el bloque siguiente.
  if "@" not in nuevo or "." not in nuevo:
   # Lanza una excepción para informar que se presentó una condición no válida.
   raise ClienteInvalidoError(f"Correo inválido: {nuevo}")
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self.__correo = nuevo

 # Indica que el método siguiente permite consultar un atributo mediante una propiedad.
 @property
 # Define el método telefono de la clase o módulo correspondiente.
 def telefono(self):
  # Devuelve el resultado de la operación o la información solicitada.
  return self.__telefono

 # Indica que el método siguiente permite consultar un atributo mediante una propiedad.
 @property
 # Define el método documento de la clase o módulo correspondiente.
 def documento(self):
  # Devuelve el resultado de la operación o la información solicitada.
  return self.__documento

 # Define el método que comprueba que los datos cumplan las reglas establecidas.
 def validar(self):
  # Inicia un bloque protegido para controlar posibles excepciones.
  try:
   # Evalúa la condición para decidir si se ejecuta el bloque siguiente.
   if not self.nombre or len(self.nombre.strip()) < 3:
    # Lanza una excepción para informar que se presentó una condición no válida.
    raise ClienteInvalidoError("El nombre debe tener mínimo 3 caracteres")
   # Evalúa la condición para decidir si se ejecuta el bloque siguiente.
   if "@" not in self.__correo or "." not in self.__correo:
    # Lanza una excepción para informar que se presentó una condición no válida.
    raise ClienteInvalidoError(f"Correo inválido: {self.__correo}")
   # Evalúa la condición para decidir si se ejecuta el bloque siguiente.
   if not str(self.__telefono).isdigit() or len(str(self.__telefono)) < 7:
    # Lanza una excepción para informar que se presentó una condición no válida.
    raise ClienteInvalidoError(f"Teléfono inválido: {self.__telefono}")
   # Evalúa la condición para decidir si se ejecuta el bloque siguiente.
   if not str(self.__documento).isdigit():
    # Lanza una excepción para informar que se presentó una condición no válida.
    raise ClienteInvalidoError(f"Documento debe ser numérico: {self.__documento}")
  # Captura el tipo de excepción indicado para gestionar el error.
  except ClienteInvalidoError as e:
   # Lanza una excepción para informar que se presentó una condición no válida.
   raise DatosInvalidosError(f"Error al validar cliente {self.nombre}") from e

 # Define el método que devuelve una descripción legible del objeto.
 def describir(self):
  # Devuelve el resultado de la operación o la información solicitada.
  return f"Cliente [{self.id}] {self.nombre} | Correo: {self.__correo} | Tel: {self.__telefono} | Doc: {self.__documento}"

# --- Clase abstracta general - Juan David Torres ---
# Declara la clase Entidad, que agrupa los datos y comportamientos de este componente.
class Entidad(ABC):
 # Define el constructor e inicializa los atributos del objeto.
 def __init__(self, id_entidad, nombre):
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self._id = id_entidad
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self._nombre = nombre
  # Asigna o actualiza un atributo del objeto con el valor indicado.
  self._fecha_creacion = datetime.now()

 # Indica que el método siguiente permite consultar un atributo mediante una propiedad.
 @property
 # Define el método id de la clase o módulo correspondiente.
 def id(self):
  # Devuelve el resultado de la operación o la información solicitada.
  return self._id

 # Indica que el método siguiente permite consultar un atributo mediante una propiedad.
 @property
 # Define el método nombre de la clase o módulo correspondiente.
 def nombre(self):
  # Devuelve el resultado de la operación o la información solicitada.
  return self._nombre

 # Declara un método abstracto que las clases concretas deben implementar.
 @abstractmethod
 # Define el método que devuelve una descripción legible del objeto.
 def describir(self):
  # Indica un bloque vacío; se utiliza como implementación provisional de este método.
  pass

 # Declara un método abstracto que las clases concretas deben implementar.
 @abstractmethod
 # Define el método que comprueba que los datos cumplan las reglas establecidas.
 def validar(self):
  # Indica un bloque vacío; se utiliza como implementación provisional de este método.
  pass

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
 # Crea la clase Servicio, que hereda de Entidad
class Servicio(Entidad):
 # Inicializa los datos principales del servicio.
 def __init__(self, id_servicio, nombre, precio_base, disponible=True):
  # Hereda el identificador y el nombre de la clase Entidad.
  super().__init__(id_servicio, nombre)
  # Guarda el precio base del servicio.
  self._precio_base = precio_base
  # Indica si el servicio esta disponible.
  self._disponible = disponible

# Permite consultar si el servicio esta disponible
@property
def disponible(self):
 return self._disponible
 
# Permite modificar el estado de la disponibilidad.
@disponible.setter
def disponible(self, valor):
 self._disponible = valor

# Define un metodo abstracto que las clases hijas deben implementar.
@abstractmethod
    def calcular_costo(self, duracion=1, impuesto=None, descuento=None):
        pass

# Obliga a las clases hijas a crear sus propias validaciones.
@abstractmethod
    def validar(self):
        pass

# Crea un metodo general para calcular el costo del servicio.
 def calcular_costo_con_opciones(self, duracion=1, impuesto=0, descuento=0):
# Multiplica el precio base por la duracion.
        base = self._precio_base * duracion
  # Calcula el valor total aplicando impuesto y descuento.
        total = base + (base * impuesto / 100) - descuento
   # Devuelve el resueltado y evita que sea negativo.
        return max(total, 0)   
 # Crea la clase ReservaSala, que hereda de Servicio. 
class ReservaSala(Servicio):
# Recibe los datos necesarios para crear una reserva de la sala.
    def __init__(self, id_servicio, nombre, precio_base, capacidad, disponible=True):
  # Hereda los atributos de la clase Servicio.
        super().__init__(id_servicio, nombre, precio_base, disponible)
  # Guarda la capacidad de la sala.
        self.capacidad = capacidad
  # Ejecuta las validaciones de la sala.
        self.validar()

# Define las conndiones para validar la sala.
def validar(self):
# Comprueba que el precio sea mayor que cero.
        if self._precio_base <= 0:
            # Genera un error si el precio no es valido.
            raise DatosInvalidosError("Precio base de sala debe ser > 0")
        # Comprueba que la capacidad sea mayor que cero.
        if self.capacidad <= 0:
            # Genera un eror si la capacidad no es valida.
            raise DatosInvalidosError("Capacidad de sala debe ser > 0")
        
# Define como se calcula el costo de reservar una sala.
def calcular_costo(self, duracion=1, impuesto=None, descuento=None):
 # Establece el impuesto en 19% cuando no se proporciona otro valor
        imp = impuesto if impuesto is not None else 19
 # Establece el descuento en cero si no se proporciona uno.
        desc = descuento if descuento is not None else 0
 # Llama al metodo general de calculo de costos y devuelve el resultado.
        return self.calcular_costo_con_opciones(duracion, imp, desc)
 
# Define el metodo que permite mostrar la informacion de la sala.
def describir(self):
# Devuelve la informacion de la sala, incluyendo el identificador, nombre, capacidad, precio por hora.
        return f"Sala [{self.id}] {self.nombre} | Capacidad: {self.capacidad} | Precio/hora: ${self._precio_base} | Disponible: {self._disponible}"

# Crea la clase AlquilerEquipo, que hereda las caracteristicas del servicio y permite administrar el alquiler de equipos.
class AlquilerEquipo(Servicio):
# Es el contructor que recibe los datos del equipo, incluyendo su cantidad en inventario.
    def __init__(self, id_servicio, nombre, precio_base, cantidad_stock, disponible=True):
         # Reutiliza el constructor de la clase de servicio para inicializar los datos generales.
        super().__init__(id_servicio, nombre, precio_base, disponible)
      # Guarda la cantidad de equipos disponibles en el inventario.
        self.cantidad_stock = cantidad_stock
    # Ejecuta las validaciones para comprobar que el precio y el inventario sean correctos.
        self.validar()
     
    # Define el metodo que comprueba los datos de alquiler de equipos.
    def validar(self):
        # Comprueba que el precio base sea mayor que cero.
        if self._precio_base <= 0:
       # Genera un error si el precio del equipo es invalido.
            raise DatosInvalidosError("Precio base de equipo debe ser > 0")
        # Comprueba que la cantidad de equipos no sea negativa. 
        if self.cantidad_stock < 0:
        # Genera un error si el inventario tiene una cantidad negativa.
            raise DatosInvalidosError("Stock no puede ser negativo")
      
 # Define el calculo del costo del alquiler de equipos.
  def calcular_costo(self, duracion=1, impuesto=None, descuento=None):
   # Establece el impuesto en 19% cuando no se proporciona otro valor.
        imp = impuesto if impuesto is not None else 19
   # Establece el descuento en cero si no se proporciona uno.
        desc = descuento if descuento is not None else 0
   # Comprueba si el alquiler tiene una duracion de cinco dias o mas.
        if duracion >= 5:
        # Si se cumple la condicion anterior, calcula y agrega un descuento adicional del 10%.
            desc += self._precio_base * duracion * 0.10
        # Envia la  duracion, el impuesto y el descuento al metodo general para obtener el costo final.
        return self.calcular_costo_con_opciones(duracion, imp, desc)

    # Define el metodo que permite mostrar la informacion del equipo.
    def describir(self):
     # Devuelve el identificador, nombre, cantidad en inventario, precio por dia y disponibilidad del equipo.
        return f"Equipo [{self.id}] {self.nombre} | Stock: {self.cantidad_stock} | Precio/día: ${self._precio_base} | Disponible: {self._disponible}"

# Crea la clase AsesoriaEspecializada, que hereda de servicio y permite administrar asesorias especializadass.
class AsesoriaEspecializada(Servicio):
 # Es el contructor que recibe el identificador, nombre, precio, especialista y disponibilidad.
    def __init__(self, id_servicio, nombre, precio_base, especialista, disponible=True):
     # Llama al constructor de servicio para reutilizar los datos generales.
        super().__init__(id_servicio, nombre, precio_base, disponible)
     # Guarda el nombre del especialista encargado de realizar la asesoria.
        self.especialista = especialista
     # Ejecuta el metodo de validacion para comprobar que los datos sean correctos.
        self.validar()

# Define el metodo encargado de validar la informacion de la asesoria.
 def validar(self):
  # Comprueba que el precio base sea mayor a cero.
        if self._precio_base <= 0:
         # Genera un error si el precio es menor o igual a cero.
            raise DatosInvalidosError("Precio base de asesoría debe ser > 0")
        # Comprueba que el nombre del especialista no este vacio y que tenga minimo tres caracteres. Tambien elimina los espacios al principio y al final para realizar la comprobacion.
        if not self.especialista or len(self.especialista.strip()) < 3:
         # Genera un error si el nombre del especialista no cumple las condiciones.
            raise DatosInvalidosError("Especialista inválido")

# Define el metodoo para calcular el costo de una asesoria personalizada.
   def calcular_costo(self, duracion=1, impuesto=None, descuento=None):
    # Establece un impuesto del 19% cuando no se proporciona otro valor.
        imp = impuesto if impuesto is not None else 19
    # Establece un descuento de cero cuando no se especifica uno.
        desc = descuento if descuento is not None else 0
    # Llama al metodo general para calcular el costo final de la asesoria.
        return self.calcular_costo_con_opciones(duracion, imp, desc)

# Define el metodo que permite mostrar la informacion de la asesoria.
    def describir(self):
     # Devuelve la informacion de la asesoria, incluyendo identificador, nombre, especialista, precio por hora y disponibilidad.
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

# Define la simulación de diez operaciones válidas e inválidas.
def simulacion_10_operaciones(sistema):
 # Muestra en consola el mensaje o la información indicada.
 print("\n" + "="*60)
 # Muestra en consola el mensaje o la información indicada.
 print("SIMULACIÓN AUTOMÁTICA - 10 OPERACIONES")
 # Muestra en consola el mensaje o la información indicada.
 print("="*60)

 # Op 1: Cliente válido
 # Inicia un bloque protegido para controlar posibles excepciones.
 try:
  # Calcula y asigna el valor correspondiente a la variable indicada.
  c1 = Cliente(1, "Juan David Torres", "juan@gmail.com", "3001234567", "1012345678")
  # Ejecuta la instrucción indicada dentro del flujo del programa.
  sistema.agregar_cliente(c1)
 # Captura el tipo de excepción indicado para gestionar el error.
 except Exception as e:
  # Registra en el archivo de logs el evento o error producido.
  registrar_log(f"Op1 error: {e}", True)
  # Muestra en consola el mensaje o la información indicada.
  print(f"Op1 falló: {e}")

 # Op 2: Cliente INVÁLIDO
 # Inicia un bloque protegido para controlar posibles excepciones.
 try:
  # Calcula y asigna el valor correspondiente a la variable indicada.
  c_malo = Cliente(2, "Ana", "correo-malo", "123", "abc")
  # Ejecuta la instrucción indicada dentro del flujo del programa.
  sistema.agregar_cliente(c_malo)
 # Captura el tipo de excepción indicado para gestionar el error.
 except Exception as e:
  # Registra en el archivo de logs el evento o error producido.
  registrar_log(f"Op2 cliente inválido capturado: {e}", True)
  # Muestra en consola el mensaje o la información indicada.
  print(f"Op2 - Cliente inválido capturado: {e} | Causa: {e.__cause__}")

 # Op 3: Cliente válido 2
 # Inicia un bloque protegido para controlar posibles excepciones.
 try:
  # Calcula y asigna el valor correspondiente a la variable indicada.
  c2 = Cliente(3, "Milena Muñoz", "milena@unad.edu.co", "3109876543", "1098765432")
  # Ejecuta la instrucción indicada dentro del flujo del programa.
  sistema.agregar_cliente(c2)
 # Captura el tipo de excepción indicado para gestionar el error.
 except Exception as e:
  # Registra en el archivo de logs el evento o error producido.
  registrar_log(f"Op3 error: {e}", True)
  # Muestra en consola el mensaje o la información indicada.
  print(f"Op3 falló: {e}")

 # Op 4: Sala válida
 # Inicia un bloque protegido para controlar posibles excepciones.
 try:
  # Calcula y asigna el valor correspondiente a la variable indicada.
  s1 = ReservaSala(1, "Sala de Juntas A", 50000, capacidad=20)
  # Ejecuta la instrucción indicada dentro del flujo del programa.
  sistema.agregar_servicio(s1)
 # Captura el tipo de excepción indicado para gestionar el error.
 except Exception as e:
  # Registra en el archivo de logs el evento o error producido.
  registrar_log(f"Op4 error: {e}", True)
  # Muestra en consola el mensaje o la información indicada.
  print(f"Op4 falló: {e}")

 # Op 5: Equipo válido
 # Inicia un bloque protegido para controlar posibles excepciones.
 try:
  # Calcula y asigna el valor correspondiente a la variable indicada.
  s2 = AlquilerEquipo(2, "Proyector Epson", 30000, cantidad_stock=5)
  # Ejecuta la instrucción indicada dentro del flujo del programa.
  sistema.agregar_servicio(s2)
 # Captura el tipo de excepción indicado para gestionar el error.
 except Exception as e:
  # Registra en el archivo de logs el evento o error producido.
  registrar_log(f"Op5 error: {e}", True)
  # Muestra en consola el mensaje o la información indicada.
  print(f"Op5 falló: {e}")

 # Op 6: Asesoría válida
 # Inicia un bloque protegido para controlar posibles excepciones.
 try:
  # Calcula y asigna el valor correspondiente a la variable indicada.
  s3 = AsesoriaEspecializada(3, "Asesoría en Python", 80000, especialista="Ing. Carlos Ruiz")
  # Ejecuta la instrucción indicada dentro del flujo del programa.
  sistema.agregar_servicio(s3)
 # Captura el tipo de excepción indicado para gestionar el error.
 except Exception as e:
  # Registra en el archivo de logs el evento o error producido.
  registrar_log(f"Op6 error: {e}", True)
  # Muestra en consola el mensaje o la información indicada.
  print(f"Op6 falló: {e}")

 # Op 7: Servicio INVÁLIDO
 # Inicia un bloque protegido para controlar posibles excepciones.
 try:
  # Calcula y asigna el valor correspondiente a la variable indicada.
  s_malo = ReservaSala(4, "Sala Mala", -1000, capacidad=0)
  # Ejecuta la instrucción indicada dentro del flujo del programa.
  sistema.agregar_servicio(s_malo)
 # Captura el tipo de excepción indicado para gestionar el error.
 except Exception as e:
  # Registra en el archivo de logs el evento o error producido.
  registrar_log(f"Op7 servicio inválido: {e}", True)
  # Muestra en consola el mensaje o la información indicada.
  print(f"Op7 - Servicio inválido capturado: {e}")

 # Op 8: Reserva EXITOSA
 # Inicia un bloque protegido para controlar posibles excepciones.
 try:
  # Ejecuta la instrucción indicada dentro del flujo del programa.
  sistema.crear_reserva(1, sistema.clientes[0], sistema.servicios[0], duracion=2)
 # Captura el tipo de excepción indicado para gestionar el error.
 except Exception as e:
  # Muestra en consola el mensaje o la información indicada.
  print(f"Op8 falló: {e}")

 # Op 9: Reserva FALLIDA duración 0
 # Inicia un bloque protegido para controlar posibles excepciones.
 try:
  # Ejecuta la instrucción indicada dentro del flujo del programa.
  sistema.crear_reserva(2, sistema.clientes[0], sistema.servicios[1], duracion=0)
 # Captura el tipo de excepción indicado para gestionar el error.
 except Exception as e:
  # Muestra en consola el mensaje o la información indicada.
  print(f"Op9 - Reserva fallida capturada: {e}")

 # Op 10: Reserva FALLIDA servicio no disponible + cancelar
 # Inicia un bloque protegido para controlar posibles excepciones.
 try:
  # Calcula y asigna el valor correspondiente a la variable indicada.
  sistema.servicios[1].disponible = False
  # Ejecuta la instrucción indicada dentro del flujo del programa.
  sistema.crear_reserva(3, sistema.clientes[1], sistema.servicios[1], duracion=3)
 # Captura el tipo de excepción indicado para gestionar el error.
 except Exception as e:
  # Muestra en consola el mensaje o la información indicada.
  print(f"Op10 - Servicio no disponible capturado: {e}")
 # Ejecuta este bloque siempre, haya ocurrido o no una excepción.
 finally:
  # Inicia un bloque protegido para controlar posibles excepciones.
  try:
   # Evalúa la condición para decidir si se ejecuta el bloque siguiente.
   if len(sistema.reservas) > 0:
    # Ejecuta la instrucción indicada dentro del flujo del programa.
    sistema.reservas[0].cancelar()
  # Captura el tipo de excepción indicado para gestionar el error.
  except Exception as e:
   # Muestra en consola el mensaje o la información indicada.
   print(f"Error al cancelar: {e}")

 # Muestra en consola el mensaje o la información indicada.
 print("\n--- Demostración métodos sobrecargados (calcular_costo) ---")
 # Calcula y asigna el valor correspondiente a la variable indicada.
 sala = sistema.servicios[0]
 # Muestra en consola el mensaje o la información indicada.
 print(f"Solo duración (2h): ${sala.calcular_costo(2):.2f}")
 # Muestra en consola el mensaje o la información indicada.
 print(f"Con impuesto 10%: ${sala.calcular_costo(2, impuesto=10):.2f}")
 # Muestra en consola el mensaje o la información indicada.
 print(f"Con impuesto 10% y descuento 5000: ${sala.calcular_costo(2, impuesto=10, descuento=5000):.2f}")

 # Muestra en consola el mensaje o la información indicada.
 print("\n Simulación terminada - El sistema SIGUE FUNCIONANDO aunque hubo errores")
 # Registra en el archivo de logs el evento o error producido.
 registrar_log("Simulación de 10 operaciones completada")

# Define la función principal que inicia y administra la ejecución del programa.
def main():
 # Muestra en consola el mensaje o la información indicada.
 print("="*60)
 # Muestra en consola el mensaje o la información indicada.
 print("SOFTWARE FJ - Sistema Integral de Gestión")
 # Muestra en consola el mensaje o la información indicada.
 print("Clientes, Servicios y Reservas | Sin Base de Datos")
 # Muestra en consola el mensaje o la información indicada.
 print("="*60)
 # Registra en el archivo de logs el evento o error producido.
 registrar_log("Inicio del sistema Software FJ")

 # Calcula y asigna el valor correspondiente a la variable indicada.
 sistema = SistemaFJ()
 # Ejecuta la instrucción indicada dentro del flujo del programa.
 simulacion_10_operaciones(sistema)

 # Repite el bloque mientras la condición indicada sea verdadera.
 while True:
  # Muestra en consola el mensaje o la información indicada.
  print("\n--- MENÚ ---")
  # Muestra en consola el mensaje o la información indicada.
  print("1. Ver todo (clientes, servicios, reservas)")
  # Muestra en consola el mensaje o la información indicada.
  print("2. Registrar cliente nuevo")
  # Muestra en consola el mensaje o la información indicada.
  print("3. Registrar servicio nuevo")
  # Muestra en consola el mensaje o la información indicada.
  print("4. Crear reserva nueva")
  # Muestra en consola el mensaje o la información indicada.
  print("5. Ver archivo de logs")
  # Muestra en consola el mensaje o la información indicada.
  print("0. Salir")
  # Inicia un bloque protegido para controlar posibles excepciones.
  try:
   # Solicita información al usuario mediante la consola.
   opcion = input("Elige una opción: ").strip()
   # Evalúa la condición para decidir si se ejecuta el bloque siguiente.
   if opcion == "1":
    # Ejecuta la instrucción indicada dentro del flujo del programa.
    sistema.mostrar_todo()
   # Evalúa una condición alternativa cuando las anteriores no se cumplieron.
   elif opcion == "2":
    # Inicia un bloque protegido para controlar posibles excepciones.
    try:
     # Calcula y asigna el valor correspondiente a la variable indicada.
     id_c = int(input("ID cliente: "))
     # Solicita información al usuario mediante la consola.
     nom = input("Nombre: ")
     # Solicita información al usuario mediante la consola.
     cor = input("Correo: ")
     # Solicita información al usuario mediante la consola.
     tel = input("Teléfono: ")
     # Solicita información al usuario mediante la consola.
     doc = input("Documento: ")
     # Calcula y asigna el valor correspondiente a la variable indicada.
     c = Cliente(id_c, nom, cor, tel, doc)
     # Ejecuta la instrucción indicada dentro del flujo del programa.
     sistema.agregar_cliente(c)
    # Captura el tipo de excepción indicado para gestionar el error.
    except Exception as e:
     # Registra en el archivo de logs el evento o error producido.
     registrar_log(f"Error registrando cliente por menú: {e} | Causa: {e.__cause__}", True)
     # Muestra en consola el mensaje o la información indicada.
     print(f" No se pudo registrar: {e}")
    # Ejecuta este bloque siempre, haya ocurrido o no una excepción.
    finally:
     # Muestra en consola el mensaje o la información indicada.
     print("-> Intento de registro terminado, el sistema sigue vivo")
   # Evalúa una condición alternativa cuando las anteriores no se cumplieron.
   elif opcion == "3":
    # Muestra en consola el mensaje o la información indicada.
    print("Tipos: 1=Sala, 2=Equipo, 3=Asesoría")
    # Solicita información al usuario mediante la consola.
    tipo = input("Tipo: ")
    # Inicia un bloque protegido para controlar posibles excepciones.
    try:
     # Calcula y asigna el valor correspondiente a la variable indicada.
     id_s = int(input("ID servicio: "))
     # Solicita información al usuario mediante la consola.
     nom = input("Nombre: ")
     # Calcula y asigna el valor correspondiente a la variable indicada.
     precio = float(input("Precio base: "))
     # Evalúa la condición para decidir si se ejecuta el bloque siguiente.
     if tipo == "1":
      # Calcula y asigna el valor correspondiente a la variable indicada.
      cap = int(input("Capacidad: "))
      # Calcula y asigna el valor correspondiente a la variable indicada.
      s = ReservaSala(id_s, nom, precio, cap)
     # Evalúa una condición alternativa cuando las anteriores no se cumplieron.
     elif tipo == "2":
      # Calcula y asigna el valor correspondiente a la variable indicada.
      stock = int(input("Stock: "))
      # Calcula y asigna el valor correspondiente a la variable indicada.
      s = AlquilerEquipo(id_s, nom, precio, stock)
     # Evalúa una condición alternativa cuando las anteriores no se cumplieron.
     elif tipo == "3":
      # Solicita información al usuario mediante la consola.
      esp = input("Especialista: ")
      # Calcula y asigna el valor correspondiente a la variable indicada.
      s = AsesoriaEspecializada(id_s, nom, precio, esp)
     # Ejecuta este bloque únicamente si el bloque try finalizó sin excepciones.
     else:
      # Lanza una excepción para informar que se presentó una condición no válida.
      raise DatosInvalidosError("Tipo de servicio no válido")
     # Ejecuta la instrucción indicada dentro del flujo del programa.
     sistema.agregar_servicio(s)
    # Captura el tipo de excepción indicado para gestionar el error.
    except Exception as e:
     # Registra en el archivo de logs el evento o error producido.
     registrar_log(f"Error registrando servicio: {e}", True)
     # Muestra en consola el mensaje o la información indicada.
     print(f" No se pudo registrar servicio: {e}")
   # Evalúa una condición alternativa cuando las anteriores no se cumplieron.
   elif opcion == "4":
    # Inicia un bloque protegido para controlar posibles excepciones.
    try:
     # Evalúa la condición para decidir si se ejecuta el bloque siguiente.
     if not sistema.clientes or not sistema.servicios:
      # Lanza una excepción para informar que se presentó una condición no válida.
      raise ReservaInvalidaError("Debe haber al menos 1 cliente y 1 servicio")
     # Muestra en consola el mensaje o la información indicada.
     print("Clientes:")
     # Recorre los elementos de la colección para procesarlos uno por uno.
     for i, c in enumerate(sistema.clientes):
      # Muestra en consola el mensaje o la información indicada.
      print(f"{i}: {c.describir()}")
     # Calcula y asigna el valor correspondiente a la variable indicada.
     ic = int(input("Índice cliente: "))
     # Muestra en consola el mensaje o la información indicada.
     print("Servicios:")
     # Recorre los elementos de la colección para procesarlos uno por uno.
     for i, s in enumerate(sistema.servicios):
      # Muestra en consola el mensaje o la información indicada.
      print(f"{i}: {s.describir()}")
     # Calcula y asigna el valor correspondiente a la variable indicada.
     isv = int(input("Índice servicio: "))
     # Calcula y asigna el valor correspondiente a la variable indicada.
     dur = int(input("Duración: "))
     # Calcula y asigna el valor correspondiente a la variable indicada.
     id_r = len(sistema.reservas) + 10
     # Ejecuta la instrucción indicada dentro del flujo del programa.
     sistema.crear_reserva(id_r, sistema.clientes[ic], sistema.servicios[isv], dur)
    # Captura el tipo de excepción indicado para gestionar el error.
    except Exception as e:
     # Registra en el archivo de logs el evento o error producido.
     registrar_log(f"Error creando reserva por menú: {e}", True)
     # Muestra en consola el mensaje o la información indicada.
     print(f" No se pudo crear reserva: {e}")
   # Evalúa una condición alternativa cuando las anteriores no se cumplieron.
   elif opcion == "5":
    # Inicia un bloque protegido para controlar posibles excepciones.
    try:
     # Abre el archivo indicado y garantiza su cierre al terminar el bloque.
     with open(ARCHIVO_LOGS, "r", encoding="utf-8") as f:
      # Muestra en consola el mensaje o la información indicada.
      print("\n--- LOGS ---")
      # Muestra en consola el mensaje o la información indicada.
      print(f.read())
    # Captura el tipo de excepción indicado para gestionar el error.
    except FileNotFoundError:
     # Muestra en consola el mensaje o la información indicada.
     print("Aún no hay logs")
   # Evalúa una condición alternativa cuando las anteriores no se cumplieron.
   elif opcion == "0":
    # Muestra en consola el mensaje o la información indicada.
    print("Gracias por usar Software FJ. ¡Chao!")
    # Registra en el archivo de logs el evento o error producido.
    registrar_log("Cierre del sistema")
    # Interrumpe el ciclo actual y continúa con la instrucción posterior al ciclo.
    break
   # Ejecuta este bloque únicamente si el bloque try finalizó sin excepciones.
   else:
    # Muestra en consola el mensaje o la información indicada.
    print("Opción no válida, intenta de nuevo")
  # Captura el tipo de excepción indicado para gestionar el error.
  except Exception as e:
   # Registra en el archivo de logs el evento o error producido.
   registrar_log(f"Error inesperado en menú principal: {e}\n{traceback.format_exc()}", True)
   # Muestra en consola el mensaje o la información indicada.
   print(f" Error inesperado pero el sistema sigue: {e}")

# Comprueba que el archivo se esté ejecutando directamente y no importando como módulo.
if __name__ == "__main__":
 # Ejecuta la instrucción indicada dentro del flujo del programa.
 main()

# ======================================================================
# ======================================================================

