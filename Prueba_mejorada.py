# -------------------------------------------------------------- #
#  Copyright (c) UMU Corporation. All rights reserved.
# ######################## PROGRAMACIÓN ORIENTADA A OBJETOS ####################### #
# ########################  ENTREGABLE 1  ####################### #


#### IMPLEMENTACIÓN CÓDIGO PARA GESTOR DE UNIVERSIDADES ####

# -------------------------------------------------------------- #

#### CLASES PARA LAS EXCEPCIONES Y ENUMERACIONES DEL CÓDIGO ####


from enum import Enum
from abc import ABCMeta, abstractmethod


class AsignaturaCreditosError(Exception):
    pass

class AsignaturaDepartamentoError(Exception):
    pass

class ProfesorAsignaturaError(Exception):
    pass

class EstudianteAsignaturaError(Exception):
    pass

class DniFormatoError(Exception):
    pass


class Sexo(Enum):
    M = 'Masculino'
    V = 'Femenino'

class Departamento(Enum):
    DIIC = 'DIIC'
    DITEC = 'DITEC'
    DIS = 'DIS'

# -------------------------------------------------------------- #

#### CLASES PARA LOS OBJETOS PERTENECIENTES AL ENUNCIADO CON SUS MÉTODOS CORRESPONDIENTES ####


class Persona:
    def __init__(self, nombre, dni, direccion, sexo):
        if not self._es_formato_dni_valido(dni):
            raise DniFormatoError("El formato del DNI no es válido.")
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

    def _es_formato_dni_valido(self, dni):
        # Verificar que el DNI tiene el formato correcto (por ejemplo, 8 dígitos)
        return len(dni) == 8 and dni.isdigit()


class MiembroDepartamento(Persona):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento):
        super().__init__(nombre, dni, direccion, sexo)
        self.id = id
        self.departamento = departamento 

    def devolver_departamento(self):
        return self.departamento

    def cambio_departamento(self, nuevo_departamento):
        self.departamento = nuevo_departamento

    def devolver_datos(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, DNI: {self.dni}, Dirección: {self.direccion}, Sexo: {self.sexo}, Departamento: {self.departamento}"


class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas = []

    def get_estudiante(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}, Dirección: {self.direccion}, Sexo: {self.sexo}, Asignaturas: {self.mostrar_asignaturas()}"

    def set_estudiante(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo

    def del_estudiante(self):
        self.nombre = None
        self.dni = None
        self.direccion = None
        self.sexo = None
        self.asignaturas = []

    def matricular(self, asignatura):
        try:
            if not isinstance(asignatura, Asignatura):
                raise EstudianteAsignaturaError("La asignatura proporcionada no es válida.")

            if asignatura.creditos > 6:
                raise EstudianteAsignaturaError("La asignatura tiene demasiados créditos para ser matriculada por un estudiante.")
            
            self.asignaturas.append(asignatura)

        except EstudianteAsignaturaError as e:
            print(f"Error al matricular estudiante: {str(e)}")

    def desmatricular(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)

    def mostrar_asignaturas(self):
        return [asignatura.nombre for asignatura in self.asignaturas]


class Asignatura:
    def __init__(self, nombre, codigo=None, creditos=None, departamento=None): #Si queremos aceptar en test: profe1.añadir_asignatura("Matemáticas"), tenemos q ponerle a nombre, creditos y departamento =None
        if creditos is not None and not isinstance(creditos, int):
            raise AsignaturaCreditosError("Los créditos de la asignatura deben ser un número entero.")
        
        if departamento is not None and departamento not in Departamento:
            raise AsignaturaDepartamentoError("El departamento de la asignatura no es válido.")
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.departamento = departamento

    def devolver_datos(self): # y departamento 
        return f"Nombre: {self.nombre}, Código: {self.codigo}, Créditos: {self.creditos}, Departamento: {self.departamento}"


class Investigador(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, id, departamento)
        self.area_investigacion = area_investigacion
    
    def get_investigador(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}, Dirección: {self.direccion}, Sexo: {self.sexo}, ID: {self.id}, Departamento: {self.departamento}, Área de Investigación: {self.area_investigacion}"

    def set_investigador(self, nombre, dni, direccion, sexo, id, departamento, area_investigacion):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo
        self.id = id
        self.departamento = departamento
        self.area_investigacion = area_investigacion

    def del_investigador(self):
        self.nombre = None
        self.dni = None
        self.direccion = None
        self.sexo = None
        self.id = None
        self.departamento = None
        self.area_investigacion = None

    def get_area_investigacion(self):
        return self.area_investigacion


class Profesor(MiembroDepartamento):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento):
        super().__init__(nombre, dni, direccion, sexo, id, departamento)
        self.asignaturas_impartidas = []
    
    def get_profesor(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}, Dirección: {self.direccion}, Sexo: {self.sexo}, ID: {self.id}, Departamento: {self.departamento}, Asignaturas Impartidas: {self.asignaturas_impartidas}" #Asignaturas Impartidas: {self.get_asignaturas_impartidas}

    def set_profesor(self, nombre, dni, direccion, sexo, id, departamento, asignaturas_impartidas):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.sexo = sexo
        self.id = id
        self.departamento = departamento
        self.asignaturas_impartidas = asignaturas_impartidas

    def del_profesor(self):
        self.nombre = None
        self.dni = None
        self.direccion = None
        self.sexo = None
        self.id = None
        self.departamento = None
        self.asignaturas_impartidas = None

    def añadir_asignatura(self, asignatura):
        try:

            if isinstance(asignatura, str):
                asignatura = Asignatura(asignatura)

            elif isinstance(asignatura, dict):
                asignatura = Asignatura(asignatura['nombre'], asignatura['codigo'], asignatura['creditos'], asignatura['departamento'])
            
            if asignatura.departamento != self.departamento:
                raise ProfesorAsignaturaError("El profesor no pertenece al mismo departamento que la asignatura.")
        
            self.asignaturas_impartidas.append(asignatura)
        
        except (AsignaturaCreditosError, AsignaturaDepartamentoError, ProfesorAsignaturaError) as e:
            print(f"Error al añadir asignatura: {str(e)}")



    def get_asignaturas_impartidas(self):
        return [asignatura.nombre for asignatura in self.asignaturas_impartidas]


class ProfesorTitular(Investigador, Profesor):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento, area_investigacion):
        Investigador.__init__(self, nombre, dni, direccion, sexo, id, departamento, area_investigacion)
        Profesor.__init__(self, nombre, dni, direccion, sexo, id, departamento)


class ProfesorAsociado(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, id, departamento):
        super().__init__(nombre, dni, direccion, sexo, id, departamento)
        self.asignaturas_impartidas = []


# -------------------------------------------------------------- #

#### INSTANCIAMIENTO DE LAS CLASES Y COMPROBACIÓN DE ERRORES ####


if __name__ == "__main__":
    # Crear instancias de Departamento
    departamento_DIIC = Departamento.DIIC
    departamento_DITEC = Departamento.DITEC

    # Crear instancias de Profesores
    profe1 = ProfesorTitular("Paco", "09224070N", "Av Libertad", Sexo.M, "ID001", departamento_DIIC, "Matemáticas")
    profe2 = ProfesorAsociado("Ana", "12345678B", "Calle Principal", Sexo.V, "ID002", departamento_DITEC)

    # Añadir asignaturas a los profesores
    profe1.añadir_asignatura("Matemáticas")
    profe1.añadir_asignatura(Asignatura("Física", "FIS101", 4, departamento_DIIC))
    profe2.añadir_asignatura({"nombre": "Lengua", "codigo": "INF101", "creditos": 3, "departamento": departamento_DITEC})

    # Mostrar las asignaturas impartidas por cada profesor
    print("Asignaturas impartidas por", profe1.nombre + ":")
    print(profe1.get_asignaturas_impartidas())

    print("\nAsignaturas impartidas por", profe2.nombre + ":")
    print(profe2.get_asignaturas_impartidas())

    # Cambiar departamento de un profesor
    profe1.cambio_departamento(departamento_DITEC)
    print("\nNuevo departamento de", profe1.nombre + ":", profe1.devolver_departamento())

    # Mostrar información de un estudiante
    estudiante1 = Estudiante("Maria", "98765432C", "Calle Secundaria", Sexo.V)
    estudiante1.matricular(Asignatura("Historia", "HIS101", 5, departamento_DITEC))
    print("\nInformación de", estudiante1.nombre + ":")
    print(estudiante1.get_estudiante())

    #Manejo de excepciones:
    try:
        asignatura_invalida = Asignatura("Física", creditos="cinco")  # Esto lanzará una excepción AsignaturaCreditosError
    except AsignaturaCreditosError as e:
        print(f"Error al crear la asignatura: {str(e)}")

    profesor = Profesor()
    try:
        profesor.añadir_asignatura("Matemáticas")  # Esto lanzará una excepción ProfesorAsignaturaError
    except ProfesorAsignaturaError as e:
        print(f"Error al añadir asignatura al profesor: {str(e)}")

    estudiante = Estudiante()
    try:
        estudiante.matricular("Química")  # Esto lanzará una excepción EstudianteAsignaturaError
    except EstudianteAsignaturaError as e:
        print(f"Error al matricular estudiante: {str(e)}")

    try:
        persona = Persona("Juan", "123456789", "Calle Principal", Sexo.M)  # Esto lanzará una excepción DniFormatoError
    except DniFormatoError as e:
        print(f"Error al crear la persona: {str(e)}")

